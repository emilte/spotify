from dataclasses import dataclass
from typing import Any, Literal

##############################################
#                   Types                    #
##############################################


class Type:
    show = 'show'
    user = 'user'
    album = 'album'
    track = 'track'
    artist = 'artist'
    episode = 'episode'
    playlist = 'playlist'


class AlbumType:
    album = 'album'
    single = 'single'
    compilation = 'compilation'


class Genre:
    alternative = 'alternative'
    samba = 'samba'
    ...


##############################################
#                Dataclasses                 #
##############################################


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
class CopyrightObject:
    available_markets: list[str]


@dataclass
class Restrictions:
    reason: str


@dataclass
class Followers:
    href: str | None
    total: int


@dataclass
class ExternalIds:
    isrc: str | None = None
    ean: str | None = None
    upc: str | None = None


@dataclass
class ExternalUrl:
    spotify: str


@dataclass
class ImageObject:
    height: int
    width: int
    url: str


@dataclass
class Thumbnail:
    url: str


@dataclass
class ResumePoint:
    fully_played: bool
    resume_position_ms: int


@dataclass
class Person:
    external_urls: ExternalUrl
    href: str
    id: str
    type: Literal['user']
    uri: str

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)


@dataclass
class SimplifiedArtistObject:
    external_urls: ExternalUrl
    href: str
    id: str
    name: str
    type: Literal['artist']
    uri: str

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)


@dataclass
class ArtistObject(SimplifiedArtistObject):
    """https://developer.spotify.com/documentation/web-api/reference/get-an-artist"""
    followers: Followers
    genres: list[str]
    images: list[ImageObject]
    popularity: int

    def __post_init__(self):
        super().__post_init__()
        self.external_urls = ExternalUrl(**self.external_urls)
        self.followers = Followers(**self.followers)
        self.images = [ImageObject(**data) for data in self.images]


@dataclass
class SimplifiedAlbumObject:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
    """
    album_type: AlbumType
    total_tracks: int
    available_markets: list[str]
    external_urls: ExternalUrl
    href: str
    id: str
    images: list[ImageObject]
    name: str
    release_date: str
    release_date_precision: str
    # restrictions: Restrictions
    type: Literal['album']
    uri: str
    artists: list[SimplifiedArtistObject]

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)
        self.images = [ImageObject(**data) for data in self.images]
        # self.restrictions = Restrictions(**self.restrictions)
        self.artists = [SimplifiedArtistObject(**data) for data in self.artists]


@dataclass
class TrackObject:
    """
    https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks
    https://developer.spotify.com/documentation/web-api/reference/get-playlist
    """
    album: SimplifiedAlbumObject
    artists: list[SimplifiedArtistObject]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    episode: bool  # undocumented?
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrl
    href: str
    id: str
    is_local: bool
    # restrictions: Restrictions
    name: str
    popularity: int
    preview_url: str
    track: bool
    track_number: int
    type: Literal['track']
    uri: str

    def __post_init__(self):
        self.album = SimplifiedAlbumObject(**self.album)
        self.artists = [SimplifiedArtistObject(**data) for data in self.artists]
        self.external_ids = ExternalIds(**self.external_ids)
        self.external_urls = ExternalUrl(**self.external_urls)
        # self.restrictions = Restrictions(**self.restrictions)


@dataclass
class Show:
    available_markets: list[str]
    copyrights: list[CopyrightObject]
    description: str
    html_description: str
    explicit: bool
    external_urls: ExternalUrl
    href: str
    id: str
    images: list[ImageObject]
    is_externally_hosted: bool
    languages: list[str]
    media_type: str
    name: str
    publisher: str
    type: Literal['show']
    uri: str
    total_episodes: int

    def __post_init__(self):
        self.copyrights = [CopyrightObject(**data) for data in self.copyrights]
        self.external_urls = ExternalUrl(**self.external_urls)
        self.images = [ImageObject(**data) for data in self.images]


@dataclass
class EpisodeObject:
    audio_preview_url: str | None
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrl
    href: str
    id: str
    images: list[ImageObject]
    is_externally_hosted: bool
    is_playable: bool
    language: str  # deprecated
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: ResumePoint
    type: Literal['episode']
    uri: str
    restrictions: Restrictions

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)
        self.images = [ImageObject(**data) for data in self.images]
        self.resume_point = ResumePoint(**self.resume_point)
        self.restrictions = Restrictions(**self.restrictions)


@dataclass
class Owner:
    external_urls: ExternalUrl
    # followers: Followers
    href: str
    id: str
    type: Literal['user']
    uri: str
    display_name: str | None

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)
        # self.followers = Followers(**self.followers)


@dataclass
class PlaylistTrackObject:
    added_at: str
    added_by: Person
    is_local: bool
    primary_color: Any | None  # undocumented?
    track: TrackObject | EpisodeObject
    video_thumbnail: Thumbnail  # undocumented?

    def __post_init__(self):
        self.added_by = Person(**self.added_by)
        if self.track['type'] == 'track':
            self.track = TrackObject(**self.track)
        elif self.track['type'] == 'episode':
            self.track = EpisodeObject(**self.track)
        self.video_thumbnail = Thumbnail(**self.video_thumbnail)


@dataclass
class PagedPlaylistTrackObject:
    href: str
    limit: int
    next: str | None
    offset: int
    previous: str | None
    total: int
    items: list[PlaylistTrackObject]

    def __post_init__(self):
        self.items = [PlaylistTrackObject(**data) for data in self.items]


@dataclass
class AlbumObject(SimplifiedAlbumObject):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-an-album
    """
    tracks: PagedPlaylistTrackObject
    copyrights: list[CopyrightObject]
    external_ids: ExternalIds
    genres: list[str]
    label: str
    popularity: int

    def __post_init__(self):
        super().__post_init__()
        self.tracks = PagedPlaylistTrackObject(**self.tracks)
        self.copyrights = [CopyrightObject(**data) for data in self.copyrights]
        self.external_ids = ExternalIds(**self.external_ids)


@dataclass
class SavedAlbumObject(AlbumObject):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-users-saved-albums
    """
    added_at: str
    album: AlbumObject

    def __post_init__(self):
        super().__post_init__()
        self.album = PagedPlaylistTrackObject(**self.album)


@dataclass
class TrackObject2:
    href: str
    total: int


@dataclass
class SimplifiedPlaylistObject:
    """
    https://developer.spotify.com/documentation/web-api/reference/search
    https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
    """
    collaborative: bool
    description: str | None
    external_urls: ExternalUrl
    href: str
    id: str
    images: list[ImageObject]
    name: str
    owner: Owner
    public: bool
    snapshot_id: str
    tracks: PagedPlaylistTrackObject
    # tracks: TrackObject2
    type: Literal['playlist']
    uri: str

    def __post_init__(self):
        self.external_urls = ExternalUrl(**self.external_urls)
        print()
        print()
        print()
        print(self)
        print()
        print(self.images)
        print()
        print()
        print()
        print()
        self.images = [ImageObject(**data) for data in self.images]
        self.owner = Owner(**self.owner)
        print(1, self.tracks)
        self.tracks = PagedPlaylistTrackObject(**self.tracks)
        # self.tracks = TrackObject2(**self.tracks)


@dataclass
class PlaylistObject(SimplifiedPlaylistObject):
    """
    https://developer.spotify.com/documentation/web-api/reference/get-playlist
    """
    followers: Followers
    primary_color: str | None  # undocumented?

    def __post_init__(self):
        super().__post_init__()
        self.followers = Followers(**self.followers)
