from time import sleep
from datetime import datetime, timedelta
from requests.exceptions import ReadTimeout

from utils import Scope
from spotipy_client import SpotipyClient
from spotipy.exceptions import SpotifyException

USER = 'emiltelstad'
POLL_DELAY_S = 3
MID_PAUSE_S = 5
MAX_BACKOFF_DELAY_S = 20
BACKOFF_INCREMENT_S = 1

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
    has_paused = False
    current_backoff_delay = POLL_DELAY_S

    while True:

        # Prevent program from running forever.
        current_dt = datetime.now()
        if start_dt - current_dt > timedelta(hours=2):
            exit('Program exceeded run limit.')

        try:
            playback_state = sp.current_playback()
            current_song = playback_state.item.uri

            if current_song != previous_song:
                # New song detected, reset states.
                previous_song = current_song
                has_paused = False
                current_backoff_delay = POLL_DELAY_S

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
            progress_percent = int((progress_ms / total_ms) * 100)
            remaining_s = total_s - progress_s

            # Detect when song is close to ending.
            if remaining_s <= POLL_DELAY_S * 3:
                # Song almost done, pause when 1 second remaining.
                sleep(max(remaining_s - 1, 0))
                sp.pause_playback()
                has_paused = True

            # If over halfway and pause has not occured for this song yet.
            if progress_percent >= 50 and has_paused is False:
                sp.pause_playback()
                has_paused = True
                sleep(MID_PAUSE_S)
                sp.start_playback()

            # Show progress of current song.
            print(f'|{"="*progress_percent:<100}|', end='\r')

        except SpotifyException:
            # Backoff max 20 sec to reduce too much polling.
            current_backoff_delay = min(current_backoff_delay + BACKOFF_INCREMENT_S, MAX_BACKOFF_DELAY_S)
            print(current_backoff_delay)
            pass
        except ReadTimeout:
            # This could happen if slow internet connection etc.
            pass

        # Wait for next poll.
        sleep(current_backoff_delay)
