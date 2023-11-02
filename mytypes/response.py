from dataclasses import dataclass
from typing import Any

from mytypes.types import (
    AlbumObject,
    TrackObject,
    ArtistObject,
    SavedAlbumObject,
    PlaylistTrackObject,
    SimplifiedAlbumObject,
    SimplifiedPlaylistObject,
)


@dataclass
class Page:
    href: str
    limit: int
    next: str | None
    offset: int
    previous: str | None
    total: int
    items: Any


@dataclass
class PagedPlaylistTrackObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
    https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks
    """
    items: list[PlaylistTrackObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [PlaylistTrackObject(**data) for data in self.items]


@dataclass
class PagedSimplifiedPlaylistObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists
    https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
    """
    items: list[SimplifiedPlaylistObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [SimplifiedPlaylistObject(**data) for data in self.items]


@dataclass
class PagedSetSimplifiedPlaylistObject:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-featured-playlists
    https://developer.spotify.com/documentation/web-api/reference/get-a-categories-playlists
    """
    message: str
    playlists: list[PagedSimplifiedPlaylistObject]

    def __post_init__(self):
        self.playlists = [PagedSimplifiedPlaylistObject(**data) for data in self.playlists]


@dataclass
class SetOfAlbumObjects:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums
    """
    albums: list[AlbumObject]

    def __post_init__(self):
        self.albums = [AlbumObject(**data) for data in self.albums]


@dataclass
class PagedSavedAlbumObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-users-saved-albums
    """
    items: list[SavedAlbumObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [SavedAlbumObject(**data) for data in self.items]


@dataclass
class SetOfArtistObjects:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists
    """
    artists: list[ArtistObject]

    def __post_init__(self):
        self.artists = [ArtistObject(**data) for data in self.artists]


@dataclass
class PagedSimplifiedAlbumObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
    """
    items: list[SimplifiedAlbumObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [SimplifiedAlbumObject(**data) for data in self.items]


@dataclass
class SetOfTracks:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks
    """
    tracks: list[TrackObject]

    def __post_init__(self):
        self.tracks = [TrackObject(**data) for data in self.tracks]


@dataclass
class PagedTrackObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/search
    """
    items: list[TrackObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [TrackObject(**data) for data in self.items]


@dataclass
class PagedArtistObject(Page):
    """
    https://developer.spotify.com/documentation/web-api/reference/search
    """
    items: list[ArtistObject]

    def __post_init__(self):
        super().__post_init__()
        self.items = [ArtistObject(**data) for data in self.items]


# @dataclass
# class PagedSimplifiedShowObject(Page):
#     """
#     https://developer.spotify.com/documentation/web-api/reference/search
#     """
#     items: list[SimplifiedShowObject]

#     def __post_init__(self):
#         self.items = [SimplifiedShowObject(**data) for data in self.items]


@dataclass
class SearchResponse:
    """
    https://developer.spotify.com/documentation/web-api/reference/search
    """
    tracks: PagedTrackObject
    artists: PagedArtistObject
    albums: PagedSimplifiedAlbumObject
    playlists: PagedSimplifiedPlaylistObject

    # shows: PagedSimplifiedShowObject
    # episodes: PagedSimplifiedEpisodeObject
    # audiobooks: PagedSimplifiedAudiobookObject

    def __post_init__(self):
        self.tracks = PagedTrackObject(**self.tracks)
        self.artists = PagedArtistObject(**self.artists)
        self.albums = PagedSimplifiedAlbumObject(**self.albums)
        self.playlists = PagedSimplifiedPlaylistObject(**self.playlists)
        # self.shows = PagedSimplifiedShowObject(**self.shows)
        # self.episodes = PagedSimplifiedEpisodeObject(**self.episodes)
        # self.audiobooks = PagedSimplifiedAudiobookObject(**self.audiobooks)
