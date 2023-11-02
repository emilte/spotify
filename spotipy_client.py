from typing import Any, Iterable
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from mytypes.response import PagedSimplifiedPlaylistObject

from mytypes.types import ImageObject, PlaylistObject


class SpotipyClient:
    """
    Env vars must be set:
    SPOTIPY_CLIENT_ID=...
    SPOTIPY_CLIENT_SECRET=...
    SPOTIPY_REDIRECT_URI=...
    """

    def __init__(self) -> None:
        self.auth_manager = SpotifyClientCredentials()
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.sp.play

    def playlist(
        self,
        playlist_id: str,
        fields: Iterable[str] = None,
        market: str | None = None,
        additional_types: Iterable[str] = ("track", ),
    ) -> PlaylistObject:
        """ Gets playlist by id.

            Parameters:
                - playlist - the id of the playlist
                - fields - which fields to return
                - market - An ISO 3166-1 alpha-2 country code or the
                           string from_token.
                - additional_types - list of item types to return.
                                     valid types are: track and episode
        """
        return self.sp.playlist(
            playlist_id=playlist_id,
            fields=fields,
            market=market,
            additional_types=additional_types,
        )

    def track(
        self,
        track_id: str,
        market: str | None = None,
    ):
        """ returns a single track given the track's ID, URI or URL

            Parameters:
                - track_id - a spotify URI, URL or ID
                - market - an ISO 3166-1 alpha-2 country code.
        """
        return self.sp.track(track_id=track_id, market=market)

    def tracks(
        self,
        tracks: Iterable[str],
        market: str | None = None,
    ):
        """ returns a list of tracks given a list of track IDs, URIs, or URLs

            Parameters:
                - tracks - a list of spotify URIs, URLs or IDs. Maximum: 50 IDs.
                - market - an ISO 3166-1 alpha-2 country code.
        """
        return self.sp.tracks(tracks=tracks, market=market)

    def artist(
        self,
        artist_id: str,
    ):
        """ returns a single artist given the artist's ID, URI or URL

            Parameters:
                - artist_id - an artist ID, URI or URL
        """
        return self.sp.artist(artist_id=artist_id)

    def artists(
        self,
        artists: Iterable[str],
    ):
        """ returns a list of artists given the artist IDs, URIs, or URLs

            Parameters:
                - artists - a list of  artist IDs, URIs or URLs
        """
        return self.sp.artists(artists=artists)

    def artist_albums(
        self,
        artist_id: str,
        album_type=None,
        country=None,
        limit=20,
        offset: int = 0,
    ):
        """ Get Spotify catalog information about an artist's albums

            Parameters:
                - artist_id - the artist ID, URI or URL
                - album_type - 'album', 'single', 'appears_on', 'compilation'
                - country - limit the response to one particular country.
                - limit  - the number of albums to return
                - offset - the index of the first album to return
        """

        return self.sp.artist_albums(
            artist_id=artist_id,
            album_type=album_type,
            country=country,
            limit=limit,
            offset=offset,
        )

    def artist_top_tracks(
        self,
        artist_id: str,
        country="US",
    ):
        """ Get Spotify catalog information about an artist's top 10 tracks
            by country.

            Parameters:
                - artist_id - the artist ID, URI or URL
                - country - limit the response to one particular country.
        """

        return self.sp.artist_top_tracks(artist_id=artist_id, country=country)

    def artist_related_artists(
        self,
        artist_id: str,
    ):
        """ Get Spotify catalog information about artists similar to an
            identified artist. Similarity is based on analysis of the
            Spotify community's listening history.

            Parameters:
                - artist_id - the artist ID, URI or URL
        """
        return self.sp.artist_related_artists(artist_id=artist_id)

    def album(
        self,
        album_id: str,
        market: str | None = None,
    ):
        """ returns a single album given the album's ID, URIs or URL

            Parameters:
                - album_id - the album ID, URI or URL
                - market - an ISO 3166-1 alpha-2 country code
        """
        return self.sp.album(album_id=album_id, market=market)

    def album_tracks(
        self,
        album_id: str,
        limit: int = 50,
        offset: int = 0,
        market: str | None = None,
    ):
        """ Get Spotify catalog information about an album's tracks

            Parameters:
                - album_id - the album ID, URI or URL
                - limit  - the number of items to return
                - offset - the index of the first item to return
                - market - an ISO 3166-1 alpha-2 country code.

        """

        return self.sp.album_tracks(album_id=album_id, limit=limit, offset=offset, market=market)

    def albums(
        self,
        albums: list[str],
        market: str | None = None,
    ):
        """ returns a list of albums given the album IDs, URIs, or URLs

            Parameters:
                - albums - a list of  album IDs, URIs or URLs
                - market - an ISO 3166-1 alpha-2 country code
        """

        return self.sp.albums(albums=albums, market=market)

    def show(
        self,
        show_id: str,
        market: str | None = None,
    ):
        """ returns a single show given the show's ID, URIs or URL

            Parameters:
                - show_id - the show ID, URI or URL
                - market - an ISO 3166-1 alpha-2 country code.
                           The show must be available in the given market.
                           If user-based authorization is in use, the user's country
                           takes precedence. If neither market nor user country are
                           provided, the content is considered unavailable for the client.
        """

        return self.sp.show(show_id=show_id, market=market)

    def shows(
        self,
        shows: Iterable[str],
        market: str | None = None,
    ):
        """ returns a list of shows given the show IDs, URIs, or URLs

            Parameters:
                - shows - a list of show IDs, URIs or URLs
                - market - an ISO 3166-1 alpha-2 country code.
                           Only shows available in the given market will be returned.
                           If user-based authorization is in use, the user's country
                           takes precedence. If neither market nor user country are
                           provided, the content is considered unavailable for the client.
        """

        return self.sp.shows(shows=shows, market=market)

    def show_episodes(
        self,
        show_id: str,
        limit: int = 50,
        offset: int = 0,
        market: str | None = None,
    ):
        """ Get Spotify catalog information about a show's episodes

            Parameters:
                - show_id - the show ID, URI or URL
                - limit  - the number of items to return
                - offset - the index of the first item to return
                - market - an ISO 3166-1 alpha-2 country code.
                           Only episodes available in the given market will be returned.
                           If user-based authorization is in use, the user's country
                           takes precedence. If neither market nor user country are
                           provided, the content is considered unavailable for the client.
        """

        return self.sp.show_episodes(show_id=show_id, limit=limit, offset=offset, market=market)

    def episode(
        self,
        episode_id: str,
        market: str | None = None,
    ):
        """ returns a single episode given the episode's ID, URIs or URL

            Parameters:
                - episode_id - the episode ID, URI or URL
                - market - an ISO 3166-1 alpha-2 country code.
                           The episode must be available in the given market.
                           If user-based authorization is in use, the user's country
                           takes precedence. If neither market nor user country are
                           provided, the content is considered unavailable for the client.
        """

        return self.sp.episode(episode_id=episode_id, market=market)

    def episodes(
        self,
        episodes,
        market: str | None = None,
    ):
        """ returns a list of episodes given the episode IDs, URIs, or URLs

            Parameters:
                - episodes - a list of episode IDs, URIs or URLs
                - market - an ISO 3166-1 alpha-2 country code.
                           Only episodes available in the given market will be returned.
                           If user-based authorization is in use, the user's country
                           takes precedence. If neither market nor user country are
                           provided, the content is considered unavailable for the client.
        """

        return self.sp.episodes()

    def search(
        self,
        q,
        limit=10,
        offset: int = 0,
        type="track",
        market: str | None = None,
    ):
        """ searches for an item

            Parameters:
                - q - the search query (see how to write a query in the
                      official documentation https://developer.spotify.com/documentation/web-api/reference/search/)  # noqa
                - limit - the number of items to return (min = 1, default = 10, max = 50). The limit is applied
                          within each type, not on the total response.
                - offset - the index of the first item to return
                - type - the types of items to return. One or more of 'artist', 'album',
                         'track', 'playlist', 'show', and 'episode'.  If multiple types are desired,
                         pass in a comma separated string; e.g., 'track,album,episode'.
                - market - An ISO 3166-1 alpha-2 country code or the string
                           from_token.
        """
        return self.sp.search()

    def search_markets(
        self,
        q,
        limit=10,
        offset: int = 0,
        type="track",
        markets=None,
        total=None,
    ):
        """ (experimental) Searches multiple markets for an item

            Parameters:
                - q - the search query (see how to write a query in the
                      official documentation https://developer.spotify.com/documentation/web-api/reference/search/)  # noqa
                - limit  - the number of items to return (min = 1, default = 10, max = 50). If a search is to be done on multiple
                            markets, then this limit is applied to each market. (e.g. search US, CA, MX each with a limit of 10).
                            If multiple types are specified, this applies to each type.
                - offset - the index of the first item to return
                - type - the types of items to return. One or more of 'artist', 'album',
                         'track', 'playlist', 'show', or 'episode'. If multiple types are desired, pass in a comma separated string.
                - markets - A list of ISO 3166-1 alpha-2 country codes. Search all country markets by default.
                - total - the total number of results to return across multiple markets and types.
        """
        return self.sp.search_markets()

    def user(
        self,
        user: str,
    ):
        """ Gets basic profile information about a Spotify User

            Parameters:
                - user - the id of the usr
        """
        return self.sp.recommendations()

    def current_user_playlists(
        self,
        limit: int = 50,
        offset: int = 0,
    ):
        """ Get current user playlists without required getting his profile
            Parameters:
                - limit  - the number of items to return
                - offset - the index of the first item to return
        """
        return self.sp.current_user_playlists(limit=limit, offset=offset)

    def playlist(
        self,
        playlist_id: str,
        fields=None,
        market: str | None = None,
        additional_types: Iterable[str] = ("track", ),
    ):
        """ Gets playlist by id.

            Parameters:
                - playlist - the id of the playlist
                - fields - which fields to return
                - market - An ISO 3166-1 alpha-2 country code or the
                           string from_token.
                - additional_types - list of item types to return.
                                     valid types are: track and episode
        """
        return self.sp.playlist(
            playlist_id=playlist_id,
            fields=fields,
            market=market,
            additional_types=additional_types,
        )

    def playlist_items(
        self,
        playlist_id: str,
        fields: list[str] | None = None,
        limit: int = 100,
        offset: int = 0,
        market: str | None = None,
        additional_types: Iterable[str] = ("track", "episode"),
    ):
        """ Get full details of the tracks and episodes of a playlist.
        
        https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks

            Parameters:
                - playlist_id - the playlist ID, URI or URL
                - fields - which fields to return
                - limit - the maximum number of tracks to return
                - offset - the index of the first track to return
                - market - an ISO 3166-1 alpha-2 country code.
                - additional_types - list of item types to return.
                                     valid types are: track and episode
        """
        return self.sp.playlist_items(
            playlist_id=playlist_id,
            fields=fields,
            limit=limit,
            offset=offset,
            market=market,
            additional_types=additional_types,
        )

    def playlist_cover_image(
        self,
        playlist_id: str,
    ) -> list[ImageObject]:
        """ Get cover image of a playlist.
        
        https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover

            Parameters:
                - playlist_id - the playlist ID, URI or URL
        """#
        return self.sp.playlist_cover_image(playlist_id=playlist_id)

    def playlist_upload_cover_image(
        self,
        playlist_id: str,
        image_b64: str,
    ) -> str:
        """ Replace the image used to represent a specific playlist
        
        https://developer.spotify.com/documentation/web-api/reference/upload-custom-playlist-cover

            Parameters:
                - playlist_id - the id of the playlist
                - image_b64 - image data as a Base64 encoded JPEG image string
                    (maximum payload size is 256 KB)
        """
        return self.sp.playlist_upload_cover_image(playlist_id=playlist_id, image_b64=image_b64)

    def user_playlists(
        self,
        user: str,
        limit: int = 50,
        offset: int = 0,
    ) -> PagedSimplifiedPlaylistObject:
        """ Gets playlists of a user
        
        https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists

            Parameters:
                - user - the id of the usr
                - limit  - the number of items to return
                - offset - the index of the first item to return
        """#
        return self.sp.user_playlists(user=user, limit=limit, offset=offset)

    def user_playlist_create(
        self,
        user: str,
        name: str,
        public: bool = True,
        collaborative: bool = False,
        description: str = "",
    ):
        """ Creates a playlist for a user

            Parameters:
                - user - the id of the user
                - name - the name of the playlist
                - public - is the created playlist public
                - collaborative - is the created playlist collaborative
                - description - the description of the playlist
        """
        return self.sp.user_playlist_create(
            user=user,
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        )

    def user_playlist_add_tracks(
        self,
        user: str,
        playlist_id: str,
        tracks: Iterable[str],
        position=None,
    ):
        """ Adds tracks to a playlist

            Parameters:
                - user - the id of the user
                - playlist_id - the id of the playlist
                - tracks - a list of track URIs, URLs or IDs
                - position - the position to add the tracks
        """
        return self.sp.user_playlist_add_tracks()

    def user_playlist_replace_tracks(
        self,
        user: str,
        playlist_id: str,
        tracks: Iterable[str],
    ):
        """ Replace all tracks in a playlist for a user

            Parameters:
                - user - the id of the user
                - playlist_id - the id of the playlist
                - tracks - the list of track ids to add to the playlist
        """
        return self.sp.user_playlist_replace_tracks()

    def user_playlist_reorder_tracks(
        self,
        user: str,
        playlist_id: str,
        range_start,
        insert_before,
        range_length=1,
        snapshot_id: str | None = None,
    ):
        """ Reorder tracks in a playlist from a user

            Parameters:
                - user - the id of the user
                - playlist_id - the id of the playlist
                - range_start - the position of the first track to be reordered
                - range_length - optional the number of tracks to be reordered
                                 (default: 1)
                - insert_before - the position where the tracks should be
                                  inserted
                - snapshot_id - optional playlist's snapshot ID
        """
        return self.sp.user_playlist_reorder_tracks()

    def playlist_change_details(
        self,
        playlist_id: str,
        name=None,
        public=None,
        collaborative=None,
        description=None,
    ):
        """ Changes a playlist's name and/or public/private state,
            collaborative state, and/or description

            Parameters:
                - playlist_id - the id of the playlist
                - name - optional name of the playlist
                - public - optional is the playlist public
                - collaborative - optional is the playlist collaborative
                - description - optional description of the playlist
        """

        return self.sp.playlist_change_details()

    def current_user_unfollow_playlist(
        self,
        playlist_id: str,
    ):
        """ Unfollows (deletes) a playlist for the current authenticated
            user

            Parameters:
                - name - the name of the playlist
        """
        return self.sp.current_user_unfollow_playlist()

    def playlist_add_items(
        self,
        playlist_id: str,
        items,
        position=None,
    ):
        """ Adds tracks/episodes to a playlist

            Parameters:
                - playlist_id - the id of the playlist
                - items - a list of track/episode URIs or URLs
                - position - the position to add the tracks
        """
        return self.sp.playlist_add_items()

    def playlist_replace_items(
        self,
        playlist_id: str,
        items,
    ):
        """ Replace all tracks/episodes in a playlist

            Parameters:
                - playlist_id - the id of the playlist
                - items - list of track/episode ids to comprise playlist
        """
        return self.sp.playlist_replace_items()

    def playlist_reorder_items(
        self,
        playlist_id: str,
        range_start,
        insert_before,
        range_length=1,
        snapshot_id: str | None = None,
    ):
        """ Reorder tracks in a playlist

            Parameters:
                - playlist_id - the id of the playlist
                - range_start - the position of the first track to be reordered
                - range_length - optional the number of tracks to be reordered
                                 (default: 1)
                - insert_before - the position where the tracks should be
                                  inserted
                - snapshot_id - optional playlist's snapshot ID
        """
        return self.sp.playlist_reorder_items()

    def playlist_remove_all_occurrences_of_items(
        self,
        playlist_id: str,
        items,
        snapshot_id: str | None = None,
    ):
        """ Removes all occurrences of the given tracks/episodes from the given playlist

            Parameters:
                - playlist_id - the id of the playlist
                - items - list of track/episode ids to remove from the playlist
                - snapshot_id - optional id of the playlist snapshot

        """

        return self.sp.playlist_remove_all_occurrences_of_items()

    def playlist_remove_specific_occurrences_of_items(
        self,
        playlist_id: str,
        items,
        snapshot_id: str | None = None,
    ):
        """ Removes all occurrences of the given tracks from the given playlist

            Parameters:
                - playlist_id - the id of the playlist
                - items - an array of objects containing Spotify URIs of the
                    tracks/episodes to remove with their current positions in
                    the playlist.  For example:
                        [  { "uri":"4iV5W9uYEdYUVa79Axb7Rh", "positions":[2] },
                        { "uri":"1301WleyT98MSxVHPZCA6M", "positions":[7] } ]
                - snapshot_id - optional id of the playlist snapshot
        """
        return self.sp.playlist_remove_specific_occurrences_of_items()

    def current_user_follow_playlist(
        self,
        playlist_id: str,
    ):
        """
        Add the current authenticated user as a follower of a playlist.

        Parameters:
            - playlist_id - the id of the playlist

        """
        return self.sp.current_user_follow_playlist()

    def playlist_is_following(
        self,
        playlist_id: str,
        user_ids,
    ):
        """
        Check to see if the given users are following the given playlist

        Parameters:
            - playlist_id - the id of the playlist
            - user_ids - the ids of the users that you want to check to see
                if they follow the playlist. Maximum: 5 ids.

        """
        return self.sp.playlist_is_following()

    def me(self, ):
        return self.sp.me()

    def current_user(self, ):
        return self.sp.current_user()

    def current_user_playing_track(self, ):
        return self.sp.current_user_playing_track()

    def current_user_saved_albums(
        self,
        limit=20,
        offset: int = 0,
        market: str | None = None,
    ):
        return self.sp.current_user_saved_albums()

    def current_user_saved_albums_add(
        self,
        albums=[],
    ):
        return self.sp.current_user_saved_albums_add()

    def current_user_saved_albums_delete(
        self,
        albums=[],
    ):
        return self.sp.current_user_saved_albums_delete()

    def current_user_saved_albums_contains(
        self,
        albums=[],
    ):
        return self.sp.current_user_saved_albums_contains()

    def current_user_saved_tracks(
        self,
        limit=20,
        offset: int = 0,
        market: str | None = None,
    ):
        return self.sp.current_user_saved_tracks()

    def current_user_saved_tracks_add(
        self,
        tracks=None,
    ):
        return self.sp.current_user_saved_tracks_add()

    def current_user_saved_tracks_delete(
        self,
        tracks=None,
    ):
        return self.sp.current_user_saved_tracks_delete()

    def current_user_saved_tracks_contains(
        self,
        tracks=None,
    ):
        return self.sp.current_user_saved_tracks_contains()

    def current_user_saved_episodes(
        self,
        limit=20,
        offset: int = 0,
        market: str | None = None,
    ):
        return self.sp.current_user_saved_episodes()

    def current_user_saved_episodes_add(
        self,
        episodes=None,
    ):
        return self.sp.current_user_saved_episodes_add()

    def current_user_saved_episodes_delete(
        self,
        episodes=None,
    ):
        return self.sp.current_user_saved_episodes_delete()

    def current_user_saved_episodes_contains(
        self,
        episodes=None,
    ):
        return self.sp.current_user_saved_episodes_contains()

    def current_user_saved_shows(
        self,
        limit=20,
        offset: int = 0,
        market: str | None = None,
    ):
        return self.sp.current_user_saved_shows()

    def current_user_saved_shows_add(
        self,
        shows: Iterable[str] = [],
    ):
        return self.sp.current_user_saved_shows_add()

    def current_user_saved_shows_delete(
        self,
        shows: Iterable[str] = [],
    ):
        """ Remove one or more shows from the current user's
            "Your Music" library.

            Parameters:
                - shows - a list of show URIs, URLs or IDs
        """#
        return self.sp.current_user_saved_shows_delete(shows=shows)

    def current_user_saved_shows_contains(
        self,
        shows: Iterable[str] = [],
    ):
        """ Check if one or more shows is already saved in
            the current Spotify user's “Your Music” library.

            Parameters:
                - shows - a list of show URIs, URLs or IDs
        """#
        return self.sp.current_user_saved_shows_contains(shows=shows)

    def current_user_followed_artists(
        self,
        limit=20,
        after=None,
    ):
        return self.sp.current_user_followed_artists()

    def current_user_following_artists(
        self,
        ids=None,
    ):
        return self.sp.current_user_following_artists()

    def current_user_following_users(
        self,
        ids=None,
    ):
        return self.sp.current_user_following_users()

    def current_user_top_artists(
        self,
        limit=20,
        offset: int = 0,
        time_range="medium_term",
    ):
        return self.sp.current_user_top_artists()

    def current_user_top_tracks(
        self,
        limit=20,
        offset: int = 0,
        time_range="medium_term",
    ):
        return self.sp.current_user_top_tracks()

    def current_user_recently_played(
        self,
        limit: int = 50,
        after=None,
        before=None,
    ):
        return self.sp.current_user_recently_played()

    def user_follow_artists(
        self,
        ids=[],
    ):
        return self.sp.user_follow_artists()

    def user_follow_users(
        self,
        ids=[],
    ):
        return self.sp.user_follow_users()

    def user_unfollow_artists(
        self,
        ids=[],
    ):
        return self.sp.user_unfollow_artists()

    def user_unfollow_users(
        self,
        ids=[],
    ):
        return self.sp.user_unfollow_users()

    def featured_playlists(
        self,
        locale=None,
        country=None,
        timestamp=None,
        limit=20,
        offset: int = 0,
    ):
        return self.sp.featured_playlists()

    def new_releases(
        self,
        country=None,
        limit=20,
        offset: int = 0,
    ):
        return self.sp.new_releases()

    def category(
        self,
        category_id,
        country=None,
        locale=None,
    ):
        return self.sp.category()

    def categories(
        self,
        country=None,
        locale=None,
        limit=20,
        offset: int = 0,
    ):
        return self.sp.categories()

    def category_playlists(
        self,
        category_id=None,
        country=None,
        limit=20,
        offset: int = 0,
    ):
        return self.sp.category_playlists()

    def recommendations(self):
        return self.sp.recommendations()

    def recommendation_genre_seeds(self):
        return self.sp.recommendation_genre_seeds()

    def audio_analysis(
        self,
        track_id: str,
    ):
        """ Get audio analysis for a track based upon its Spotify ID
            Parameters:
                - track_id - a track URI, URL or ID
        """
        return self.sp.audio_analysis(track_id=track_id)

    def audio_features(
        self,
        tracks=[],
    ):
        """ Get audio features for one or multiple tracks based upon their Spotify IDs
            Parameters:
                - tracks - a list of track URIs, URLs or IDs, maximum: 100 ids
        """
        return self.sp.audio_features(tracks=tracks)

    def devices(self, ):
        """ Get a list of user's available devices."""
        return self.sp.devices()

    def current_playback(
        self,
        market: str | None = None,
        additional_types=None,
    ):
        """ Get information about user's current playback.

            Parameters:
                - market - an ISO 3166-1 alpha-2 country code.
                - additional_types - `episode` to get podcast track information
        """
        return self.sp.current_playback()

    def currently_playing(
        self,
        market: str | None = None,
        additional_types=None,
    ):
        """ Get user's currently playing track.

            Parameters:
                - market - an ISO 3166-1 alpha-2 country code.
                - additional_types - `episode` to get podcast track information
        """
        return self.sp.currently_playing()

    def transfer_playback(
        self,
        device_id,
        force_play=True,
    ):
        """ Transfer playback to another device.
            Note that the API accepts a list of device ids, but only
            actually supports one.

            Parameters:
                - device_id - transfer playback to this device
                - force_play - true: after transfer, play. false:
                               keep current state.
        """
        return self.sp.transfer_playback()

    def start_playback(self, ) -> Any:
        return self.sp.start_playback()

    def pause_playback(self):
        return self.sp.pause_playback()

    def next_track(
        self,
        device_id=None,
    ):
        """ Skip user's playback to next track.

            Parameters:
                - device_id - device target for playback
        """
        return self.sp.next_track()

    def previous_track(
        self,
        device_id=None,
    ):
        """ Skip user's playback to previous track.

            Parameters:
                - device_id - device target for playback
        """
        return self.sp.previous_track()

    def seek_track(
        self,
        position_ms,
        device_id=None,
    ):
        """ Seek to position in current track.

            Parameters:
                - position_ms - position in milliseconds to seek to
                - device_id - device target for playback
        """
        return self.sp.seek_track()

    def repeat(
        self,
        state,
        device_id=None,
    ):
        """ Set repeat mode for playback.

            Parameters:
                - state - `track`, `context`, or `off`
                - device_id - device target for playback
        """
        return self.sp.repeat()

    def volume(
        self,
        volume_percent,
        device_id=None,
    ):
        """ Set playback volume.

            Parameters:
                - volume_percent - volume between 0 and 100
                - device_id - device target for playback
        """
        return self.sp.volume()

    def shuffle(
        self,
        state,
        device_id=None,
    ):
        """ Toggle playback shuffling.

            Parameters:
                - state - true or false
                - device_id - device target for playback
        """
        return self.sp.shuffle()

    def queue(self, ):
        """ Gets the current user's queue """
        return self.sp.queue()

    def add_to_queue(
        self,
        uri,
        device_id=None,
    ):
        """ Adds a song to the end of a user's queue

            If device A is currently playing music and you try to add to the queue
            and pass in the id for device B, you will get a
            'Player command failed: Restriction violated' error
            I therefore recommend leaving device_id as None so that the active device is targeted

            :param uri: song uri, id, or url
            :param device_id:
                the id of a Spotify device.
                If None, then the active device is used.

        """

        return self.sp.add_to_queue()

    def available_markets(self, ):
        """ Get the list of markets where Spotify is available.
            Returns a list of the countries in which Spotify is available, identified by their
            ISO 3166-1 alpha-2 country code with additional country codes for special territories.
        """
        return self.sp.available_markets()
