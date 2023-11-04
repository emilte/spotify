from time import sleep
from utils import Scope
from spotipy_client import SpotipyClient
from spotipy.exceptions import SpotifyException

USER = 'emiltelstad'
POLL_DELAY = 3
PAUSE = 5

if __name__ == '__main__':

    sp = SpotipyClient(
        username=USER,
        scope=[
            Scope.user_read_playback_state,
            Scope.user_read_playback_position,
            Scope.user_modify_playback_state,
        ],
    )

    current = None
    prev = None
    has_paused = False

    while True:
        try:
            playback_state = sp.current_playback()

            # Handle no current ongoing session.
            if playback_state is None:
                sleep(POLL_DELAY)
                continue

            current = playback_state.item.uri

            if current != prev:
                # New song detected, reset states.
                prev = current
                has_paused = False

            # Calculate progress.
            progress_ms = playback_state.progress_ms
            total_ms = playback_state.item.duration_ms
            progress_s = progress_ms / 1000
            total_s = total_ms / 1000
            progress_percent = int((progress_ms / total_ms) * 100)
            remaining_s = total_s - progress_s

            # Detect when song is close to ending.
            if remaining_s <= POLL_DELAY * 3:
                # Song almost done, pause when 1 second remaining.
                sleep(max(remaining_s - 1, 0))
                sp.custom_toggle_playback(force='pause')
                has_paused = True

            # If over halfway and pause has not occured for this song yet.
            if progress_percent >= 50 and has_paused is False:
                sp.custom_toggle_playback(force='pause')
                sleep(PAUSE)
                sp.custom_toggle_playback(force='start')
                has_paused = True

            # Show progress of current song.
            print(f'|{"="*progress_percent:<100}|', end='\r')

        except SpotifyException:
            pass

        sleep(POLL_DELAY)
