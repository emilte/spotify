"""
The Atheist Experience.
Copy all episodes into playlist.
"""
import math
from mytypes.types import PagedSimplifiedEpisodeObject, Show, SimplifiedEpisodeObject

from utils import Scope
from spotipy_client import SpotipyClient

USER = 'emiltelstad'
PODCAST = 'https://open.spotify.com/show/770WPA1HnBVJ3b2gzliMDJ?si=3d98ab3e37e6416a'

if __name__ == '__main__':

    sp = SpotipyClient(
        username=USER,
        scope=[Scope.playlist_modify_private, Scope.playlist_modify_public],
    )

    show: Show = sp.show(show_id=PODCAST)
    pl = sp.user_playlist_create(name='TAE episodes', public=False, user=USER)

    limit = 50  # Max episode retrieval per page.

    # Minimum loops required to find all songs with bucket size of `limit`.
    l = math.ceil(show.total_episodes / 50)

    episodes: list[SimplifiedEpisodeObject] = []

    # Find all songs.
    for offset in range(l):
        paged_episodes: PagedSimplifiedEpisodeObject = sp.show_episodes(
            show_id=PODCAST,
            limit=limit,
            offset=limit * offset,
        )
        episodes.extend(paged_episodes.items)

    # Sort.
    episodes_by_release_date = sorted(episodes, key=lambda item: item.release_date)

    # Extract uris.
    episode_uris = [item.uri for item in episodes_by_release_date]

    m = 100  # Max add limit.

    # Minimum loops required to add all songs with bucket size of `m`.
    add_loops = math.ceil((len(episodes_by_release_date) / 100))

    # Add all songs.
    for i in range(add_loops):
        lower_i = m * i
        upper_i = m * (i + 1)
        sp.playlist_add_items(playlist_id=pl.uri, items=episode_uris[lower_i:upper_i])
