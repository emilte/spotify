import os
from utils import Scope
from mytypes.types import AudioFeaturesObject, PlaylistObject
from spotipy_client import SpotipyClient


def bpm_sorter(audio_feature: AudioFeaturesObject, threshold: int | None = None) -> float:
    bpm = audio_feature.tempo
    if threshold is not None and audio_feature.tempo >= threshold:
        bpm /= 2
    return bpm


def duplicate_playlist_sorted_by_bpm(
    client: SpotipyClient,
    playlist: str,
    name: str = '',
    threshold: int | None = None,
    dry_run: bool | int = False,
) -> None:

    playlist: PlaylistObject = client.playlist(playlist_id=playlist)

    songs_by_uris = {item.track.uri: item.track for item in playlist.tracks.items}

    audio_features: list[AudioFeaturesObject] = client.audio_features(tracks=songs_by_uris.keys())

    sorted_audio_features = sorted(
        audio_features,
        key=lambda s: bpm_sorter(audio_feature=s, threshold=threshold),
    )
    sorted_audio_features_uris = [item.uri for item in sorted_audio_features]

    for i in sorted_audio_features:
        print(i.tempo, songs_by_uris[i.uri].name)

    plname = name or f'{playlist.name} - by bpm'
    if not dry_run:
        new_pl: PlaylistObject = client.user_playlist_create(user=user, name=plname)
        client.playlist_add_items(playlist_id=new_pl.uri, items=sorted_audio_features_uris)
    print(f'Created playlist: {plname}')


if __name__ == '__main__':
    scopes = [Scope.playlist_modify_private, Scope.playlist_modify_public]

    slow_wcs_playlist, slow_t = 'https://open.spotify.com/playlist/0w0YxOMjvKUFS215VPIK6X?si=af0f0880708744c8', 100
    inputpl = 'https://open.spotify.com/playlist/5ISmAZvdFQob5nEZgH9ufI?si=4ee7af478b0b4a38'
    test = 'https://open.spotify.com/playlist/0zTGrbhMKJcOnCnAn55vGZ?si=34295a468ad74e65'
    fast_wcs = 'https://open.spotify.com/playlist/5lTsNph8TgIrTR7znoGfGk?si=49125ed39fe7483e'
    user = os.environ['USER']

    sp = SpotipyClient(username=user, scope=scopes)

    USING_PL = slow_wcs_playlist
    THRESHOLD = None
    # THRESHOLD = 170
    THRESHOLD = slow_t
    DRY_RUN = 1

    duplicate_playlist_sorted_by_bpm(client=sp, playlist=USING_PL, threshold=THRESHOLD, dry_run=DRY_RUN)
