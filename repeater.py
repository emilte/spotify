import os
from time import sleep
from datetime import datetime

from requests import ReadTimeout
from spotipy.exceptions import SpotifyException

from utils import Scope
from spotipy_client import SpotipyClient

url = "https://api.spotify.com"

REPEAT = 2

USER = os.environ['USER']

POLL_DELAY_S = 2

if __name__ == '__main__':

    sp = SpotipyClient(
        username=USER,
        scope=[
            Scope.user_read_playback_state,
            Scope.user_read_playback_position,
            Scope.user_modify_playback_state,
        ],
    )

    start_dt = datetime.now()
    previous_song = None
    count = 1

    sp.repeat(state='track')

    while True:

        try:
            print(count, end='\r')
            sp = SpotipyClient(username=USER, scope=Scope.user_modify_playback_state)
            playback_state = sp.current_playback()

            current_song = playback_state.item.uri

            if current_song != previous_song:
                # New song detected, reset states.
                previous_song = current_song
                sp.repeat(state='track')
                count = 1

            if count >= REPEAT:
                sp.repeat(state='off')

            # Handle no current ongoing session.
            is_player_inactive = playback_state is None or playback_state.is_playing is False
            if is_player_inactive:
                # Raise error to skip to the except block.
                raise SpotifyException(http_status=None, code=None, msg='Waiting for player to start')

            # Calculate progress.
            progress_ms = playback_state.progress_ms
            total_ms = playback_state.item.duration_ms
            progress_s = progress_ms / 1000
            total_s = total_ms / 1000
            remaining_s = total_s - progress_s

            # Detect when song is close to ending.
            if remaining_s <= max(POLL_DELAY_S * 3, 5):
                # Song almost done, pause when 1 second remaining.
                sleep(max(remaining_s - 2, 0))
                count += 1

        except SpotifyException:
            pass
        except ReadTimeout:
            # This could happen if slow internet connection etc.
            pass

        # Wait for next poll.
        sleep(POLL_DELAY_S)
