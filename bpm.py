from mytypes.types import AudioFeaturesObject, PlaylistObject
from spotipy_client import SpotipyClient

url = "https://api.spotify.com"


class Scope:
    playlist_modify_public = 'playlist-modify-public'
    playlist_modify_private = 'playlist-modify-private'


def scope_builder(*scopes):
    return ' '.join(scopes)


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
):

    playlist: PlaylistObject = client.playlist(playlist_id=USING_PL)

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
        new_pl: PlaylistObject = client.user_playlist_create(user=emil, name=plname)
        client.playlist_add_items(playlist_id=new_pl.uri, items=sorted_audio_features_uris)
    print(f'Created playlist: {plname}')


if __name__ == '__main__':
    scopes = scope_builder(Scope.playlist_modify_private, Scope.playlist_modify_public)

    slow_wcs_playlist = 'https://open.spotify.com/playlist/0w0YxOMjvKUFS215VPIK6X?si=af0f0880708744c8'
    inputpl = 'https://open.spotify.com/playlist/5ISmAZvdFQob5nEZgH9ufI?si=4ee7af478b0b4a38'
    test = 'https://open.spotify.com/playlist/0zTGrbhMKJcOnCnAn55vGZ?si=34295a468ad74e65'
    fast_wcs = 'https://open.spotify.com/playlist/5lTsNph8TgIrTR7znoGfGk?si=49125ed39fe7483e'
    emil = 'emiltelstad'

    sp = SpotipyClient(username=emil, scope=scopes)

    USING_PL = fast_wcs
    THRESHOLD = None
    THRESHOLD = 170
    DRY_RUN = 0

    duplicate_playlist_sorted_by_bpm(client=sp, playlist=USING_PL, threshold=THRESHOLD, dry_run=DRY_RUN)
