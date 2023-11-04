import os
from datetime import datetime

from utils import Scope
from spotipy_client import SpotipyClient

ENV_PREFIX = 'DW_'
L = len(ENV_PREFIX)
DATE_FMT = '%d-%m-%Y'
USER = 'emiltelstad'


def duplicate_discover_weekly(client: SpotipyClient, name: str, playlist_id: str) -> None:

    # Copy Discover Weekly songs.
    paged_items = client.playlist_items(playlist_id=playlist_id)
    item_uris = [item.track.uri for item in paged_items.items]

    # Create playlist and add songs.
    playlist = client.user_playlist_create(user=USER, name=name, public=False)
    client.playlist_add_items(items=item_uris, playlist_id=playlist.uri)


if __name__ == '__main__':

    DWS = {k: v for k, v in os.environ.items() if k.startswith(ENV_PREFIX)}
    date = datetime.now().date().strftime(DATE_FMT)
    sp = SpotipyClient(
        username=USER,
        scope=[Scope.playlist_modify_private, Scope.playlist_modify_public],
    )

    for env_name, pl_id in DWS.items():

        name = env_name[L:].title()
        plname = f'dw {name} - {date}'

        duplicate_discover_weekly(client=sp, name=plname, playlist_id=pl_id)
