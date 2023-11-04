from enum import Enum
from time import sleep
from typing import Literal
from utils import Scope
from spotipy_client import SpotipyClient
from spotipy.exceptions import SpotifyException

USER = 'emiltelstad'
# PL = 'https://open.spotify.com/playlist/3fQXXh9F7O7TeEfSaLd2dJ?si=6dd315f0f68e4725'
PL = 'https://open.spotify.com/playlist/2f0OPF3Yt1qL5OXq4lumaZ?si=e384c153d1964b51'

if __name__ == '__main__':

    is_playing = False

    sp = SpotipyClient(
        username=USER,
        scope=[
            Scope.playlist_read_collaborative,
            Scope.playlist_read_private,
            Scope.user_read_playback_state,
            Scope.user_read_playback_position,
            Scope.user_modify_playback_state,
        ],
    )

    playlist = sp.playlist(playlist_id=PL)
    track_uris = {t.track.uri: t.track for t in playlist.tracks.items}

    features = sp.audio_features(tracks=track_uris.keys())
    af = {i.uri: i for i in features}

    print(f"{'nr':^10} {'Song':<50} {'Artists'}")
    for n, i in enumerate(playlist.tracks.items, 1):
        # truncated_name = i.track.name[:30] + (i.track.name[30:] and '...')
        truncated_name = i.track.name
        artists = ', '.join([a.name for a in i.track.artists])
        print(f'{n:^10} {truncated_name:<60} {artists}')

    current = None
    prev = None
    has_paused = False
    delay = 2

    while True:
        sleep(delay)
        try:
            playback_state = sp.current_playback()

            current = playback_state.item.uri
            if current != prev:
                prev = current
                has_paused = False

            progress_ms = playback_state.progress_ms
            progress_s = progress_ms / 1000
            total_ms = playback_state.item.duration_ms
            total_s = total_ms / 1000
            pros = int((progress_s / total_s) * 100)

            if pros >= 50 and has_paused is False:
                # is_playing = sp.pause_playback()
                is_playing = sp.custom_toggle_playback(force='pause')
                sleep(4)
                # is_playing = sp.start_playback()
                is_playing = sp.custom_toggle_playback(force='start')
                has_paused = True

            remaining_s = total_s - progress_s
            print(remaining_s)
            if remaining_s <= delay * 3:
                sleep(max(remaining_s - 1, 0))
                # is_playing = sp.pause_playback()
                is_playing = sp.custom_toggle_playback(force='pause')

            # print(progress_s, total_s, pros)
            print(f'|{"="*pros:<100}|', end='\r')

        except SpotifyException:
            pass
