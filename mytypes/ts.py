from dataclasses import dataclass
# Release comments:
# -----------------

# The audio analysis object is not yet in the Object Model at Spotify, therefore it is typed as any in this file.

# TrackObjects and AlbumObjects is specified in the docs as always having the available_markets property,
# but when it is sent in https://developer.spotify.com/web-api/console/get-current-user-saved-tracks
# the available_markets are missing. Therefore it is marked as optional in this source code.

#
# Parameter Objects for searching
#


    # Object for search parameters for searching for tracks, playlists, artists or albums.
    # See: [Search for an item](https://developer.spotify.com/web-api/search-item/)
    # *
    # `q` and `type` are required in the API. Previous versions of the type declarations marked them
    # as optional in order for external libraries to "implement them as function call parameters instead".
    # Now, the type declaration shall mark them as required. If necessary, one can consider this to be a
    # "breaking change". In that case, one can use TypeScript's built-in utility type `Omit<T, K>`.
    # For example, one can remove the `q` and `type` by annotating the type
    # as `Omit<SpotifyApi.SearchForItemParameterObject, "q" | "type">`.

@dataclass
class SearchForItemParameterObject:

        # The search query's keywords (and optional field filters and operators).
    
    q: str

        # A comma-separated list of item types to search across. Valid types are: `album`, `artist`, `playlist`, and `track`.
        # Search results include hits from all the specified item types.
        # For example: `q=name:abacab&type=album,track` returns both albums and tracks with `“abacab”` included in their name.
    
    type: str

        # An [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or the str `from_token`.
        # If a country code is specified, only artists, albums, and tracks with content that is playable in that market is returned.
    
    market: str | None

        # The maximum number of results to return.
        # Default: `20`. Minimum: `1`. Maximum: `50`.
    
    limit: int | None

        # The index of the first result to return.
        # Default: `0` (first result). Maximum offset (including limit): `2,000`.
        # Use with limit to get the next page of search results.
    
    offset: int | None

        # Possible values: `audio`.
        # If `include_external=audio` is specified, the response will include any relevant audio content that is hosted externally.
        # By default external content is filtered out from responses.
    
    include_external: str | None



    # Object for use in Recommendations Based on Seeds.
    # See: [Recommendations Based on Seeds](https://developer.spotify.com/web-api/get-recommendations/)
    *
    # [max_*] - Multiple values. For each tunable track attribute, a hard ceiling on the selected track attribute’s value can be provided. See tunable track attributes below for the list of available options. For example, max_instrumentalness=0.35 would filter out most tracks that are likely to be instrumental.
    # [min_*] - Multiple values. For each tunable track attribute, a hard floor on the selected track attribute’s value can be provided. See tunable track attributes below for the list of available options. For example, min_tempo=140 would restrict results to only those tracks with a tempo of greater than 140 beats per minute.
    # [target_*] - Multiple values. For each of the tunable track attributes (below) a target value may be provided. Tracks with the attribute values nearest to the target values will be preferred. For example, you might request target_energy=0.6 and target_danceability=0.8. All target values will be weighed equally in ranking results.

@dataclass
class RecommendationsOptionsObject:
#  The target size of the list of recommended tracks. For seeds with unusually small pools or when highly restrictive filtering is applied, it may be impossible to generate the requested number of recommended tracks. Debugging information for such cases is available in the response. Default: 20. Minimum: 1. Maximum: 100. 
    limit: int | None
#  An ISO 3166-1 alpha-2 country code. Provide this parameter if you want to apply Track Relinking. Because min_*, max_# and target_# are applied to pools before relinking, the generated results may not precisely match the filters applied. Original, non-relinked tracks are available via the linked_from attribute of the relinked track response. 
    market: str | None
    max_acousticness: int | None
    max_danceability: int | None
    max_duration_ms: int | None
    max_energy: int | None
    max_instrumentalness: int | None
    max_key: int | None
    max_liveness: int | None
    max_loudness: int | None
    max_mode: int | None
    max_popularity: int | None
    max_speechiness: int | None
    max_tempo: int | None
    max_time_signature: int | None
    max_valence: int | None
    min_acousticness: int | None
    min_danceability: int | None
    min_duration_ms: int | None
    min_energy: int | None
    min_instrumentalness: int | None
    min_key: int | None
    min_liveness: int | None
    min_loudness: int | None
    min_mode: int | None
    min_popularity: int | None
    min_speechiness: int | None
    min_tempo: int | None
    min_time_signature: int | None
    min_valence: int | None
#  A comma separated list of Spotify IDs for seed artists. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. 
    seed_artists: list[str] | str | None # Array of strings or Comma separated str
#  A comma separated list of any genres in the set of available genre seeds. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. 
    seed_genres: list[str] | str | None # Array of strings or Comma separated str
#  A comma separated list of Spotify IDs for a seed track. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. 
    seed_tracks: list[str] | str | None # Array of strings or Comma separated str
    target_acousticness: int | None
    target_danceability: int | None
    target_duration_ms: int | None
    target_energy: int | None
    target_instrumentalness: int | None
    target_key: int | None
    target_liveness: int | None
    target_loudness: int | None
    target_mode: int | None
    target_popularity: int | None
    target_speechiness: int | None
    target_tempo: int | None
    target_time_signature: int | None
    target_valence: int | None


@dataclass
class RecentlyPlayedParameterObject:
    limit: int | None
    after: int | None
    before: int | None


@dataclass
class TransferPlaybackParameterObject:
    play: bool | None


@dataclass
class TrackRelinkingParameterObject:
    market: str | None


@dataclass
class DeviceSpecificParameterObject:
    device_id: str | None
    context_uri: str | None
    position_ms: int | None
    uris: list[str] | None
    offset: int | None


@dataclass
class PlayParameterObject:
    device_id: str | None
    context_uri: str | None
    uris: list[str] | None
    offset: ...
        # | {
        #     position: int | None
        #     uri: str | None
        
        # | None
    position_ms: int | None


@dataclass
class RestrictionsObject:
    reason: str


#
# Responses from the Spotify Web API in the same order as in the API endpoint docs seen here:
# [API Endpoint Reference](https://developer.spotify.com/web-api/endpoint-reference/)
#

# Generic interfaces for re-use:


    # Void Response

@dataclass
class VoidResponse :


    # Response with Playlist Snapshot

@dataclass
class PlaylistSnapshotResponse:
    snapshot_id: str


# Spotify API Endpoints:


    # Get an Album
    *
    # GET /v1/albums/{id
    # https://developer.spotify.com/web-api/get-album/

@dataclass
class SingleAlbumResponse extends AlbumObjectFull :


    # Get Several Albums
    *
    # GET /v1/albums?ids={ids
    # https://developer.spotify.com/web-api/get-several-albums/

@dataclass
class MultipleAlbumsResponse:
    albums: list[AlbumObjectFull]



    # Get an Album’s Tracks
    *
    # GET /v1/albums/{id/tracks
    # https://developer.spotify.com/web-api/get-albums-tracks/

@dataclass
class AlbumTracksResponse extends PagingObject<TrackObjectSimplified> :


    # Get an Artist
    *
    # GET /v1/artists/{id
    # https://developer.spotify.com/web-api/get-artist/

@dataclass
class SingleArtistResponse extends ArtistObjectFull :


    # Get Several Artists
    *
    # /v1/artists?ids={ids
    # https://developer.spotify.com/web-api/get-several-artists/

@dataclass
class MultipleArtistsResponse:
    artists: ArtistObjectFull[]



    # Get an Artist’s Albums
    *
    # GET /v1/artists/{id/albums
    # https://developer.spotify.com/web-api/get-artists-albums/

@dataclass
class ArtistsAlbumsResponse extends PagingObject<AlbumObjectSimplified> :


    # Get an Artist’s Top Tracks
    *
    # GET /v1/artists/{id/top-tracks
    # https://developer.spotify.com/web-api/get-artists-top-tracks/

@dataclass
class ArtistsTopTracksResponse:
    tracks: TrackObjectFull[]



    # Get an Artist’s Related Artists
    *
    # GET /v1/artists/{id/related-artists
    # https://developer.spotify.com/web-api/get-related-artists/

@dataclass
class ArtistsRelatedArtistsResponse:
    artists: ArtistObjectFull[]



    # Get Audio Analysis for a Track
    *
    # GET /v1/audio-analysis/{id
    # https://developer.spotify.com/web-api/get-audio-analysis/
    *
    # At the time of typing, the Audio Analysis Object is absent from the Object Model, so it is typed as any.
    # Object Model: https://developer.spotify.com/web-api/object-model/

@dataclass
class AudioAnalysisResponse extends AudioAnalysisObject :


    # Get audio features for a track
    *
    # GET /v1/audio-features/{id
    # https://developer.spotify.com/web-api/get-audio-features/

@dataclass
class AudioFeaturesResponse extends AudioFeaturesObject :


    # Get audio features for several tracks
    *
    # GET /v1/audio-features?ids={ids
    # https://developer.spotify.com/get-several-audio-features/

@dataclass
class MultipleAudioFeaturesResponse:
    audio_features: AudioFeaturesObject[]



    # Get a list of featured playlists
    *
    # GET /v1/browse/featured-playlists
    # https://developer.spotify.com/web-api/get-list-featured-playlists/

@dataclass
class ListOfFeaturedPlaylistsResponse:
    message: str | None
    playlists: PagingObject<PlaylistObjectSimplified>



    # Get a list of new releases
    *
    # GET /v1/browse/new-releases
    # https://developer.spotify.com/web-api/get-list-new-releases/

@dataclass
class ListOfNewReleasesResponse:
    message: str | None
    albums: PagingObject<AlbumObjectSimplified>



    # Get a list of categories
    *
    # GET /v1/browse/categories
    # https://developer.spotify.com/web-api/get-list-categories/

@dataclass
class MultipleCategoriesResponse:
    categories: PagingObject<CategoryObject>



    # Get a category
    *
    # GET /v1/browse/categories/{id
    # https://developer.spotify.com/web-api/get-category/

@dataclass
class SingleCategoryResponse extends CategoryObject :


    # Get a categorys playlists
    *
    # GET /v1/browse/categories/{id/playlists
    # https://developer.spotify.com/web-api/get-categorys-playlists/

@dataclass
class CategoryPlaylistsResponse:
    playlists: PagingObject<PlaylistObjectSimplified>


    # Get a categorys playlists
    *
    # GET /v1/browse/categories/{id/playlists
    # https://developer.spotify.com/web-api/get-categorys-playlists/
    # @deprecated Use `CategoryPlaylistsResponse` instead

@dataclass
class CategoryPlaylistsReponse extends CategoryPlaylistsResponse :


    # Get Playlist Cover Image
    *
    # GET /v1/playlists/playlist_id/image
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlist-cover

@dataclass
class PlaylistCoverImageResponse extends Array<ImageObject> :


    # Get Current User’s Profile
    *
    # GET /v1/me
    # https://developer.spotify.com/web-api/get-current-users-profile/

@dataclass
class CurrentUsersProfileResponse extends UserObjectPrivate :


    # Get User’s Followed Artists
    *
    # GET /v1/me/following
    # https://developer.spotify.com/web-api/get-followed-artists/

@dataclass
class UsersFollowedArtistsResponse:
    artists: CursorBasedPagingObject<ArtistObjectFull>



    # Follow artists or users
    *
    # PUT /v1/me/following
    # https://developer.spotify.com/web-api/follow-artists-users/

@dataclass
class FollowArtistsOrUsersResponse extends VoidResponse :


    # Unfollow artists or users
    *
    # DELETE /v1/me/following
    # https://developer.spotify.com/web-api/unfollow-artists-users/

@dataclass
class UnfollowArtistsOrUsersResponse extends VoidResponse :


    # Check if User Follows Users or Artists
    *
    # GET /v1/me/following/contains
    # https://developer.spotify.com/web-api/check-current-user-follows/

@dataclass
class UserFollowsUsersOrArtistsResponse extends Array<bool> :


    # Follow a Playlist
    *
    # PUT /v1/users/{owner_id/playlists/{playlist_id/followers
    # https://developer.spotify.com/web-api/follow-playlist/

@dataclass
class FollowPlaylistResponse extends VoidResponse :

    # Follow a Playlist
    *
    # PUT /v1/users/{owner_id/playlists/{playlist_id/followers
    # https://developer.spotify.com/web-api/follow-playlist/
    # @deprecated Use `FollowPlaylistResponse` instead

@dataclass
class FollowPlaylistReponse extends FollowPlaylistResponse :


    # Unfollow a Playlist
    *
    # DELETE /v1/users/{owner_id/playlists/{playlist_id/followers
    # https://developer.spotify.com/web-api/unfollow-playlist/

@dataclass
class UnfollowPlaylistResponse extends VoidResponse :

    # Unfollow a Playlist
    *
    # DELETE /v1/users/{owner_id/playlists/{playlist_id/followers
    # https://developer.spotify.com/web-api/unfollow-playlist/
    # @deprecated Use `UnfollowPlaylistResponse` instead

@dataclass
class UnfollowPlaylistReponse extends UnfollowPlaylistResponse :


    # Save tracks for user
    *
    # PUT /v1/me/tracks?ids={ids
    # https://developer.spotify.com/web-api/save-tracks-user/

@dataclass
class SaveTracksForUserResponse extends VoidResponse :


    # Get user's saved tracks
    *
    # GET /v1/me/tracks
    # https://developer.spotify.com/web-api/get-users-saved-tracks/

@dataclass
class UsersSavedTracksResponse extends PagingObject<SavedTrackObject> :


    # Remove User’s Saved Tracks
    *
    # DELETE /v1/me/tracks?ids={ids
    # https://developer.spotify.com/web-api/remove-tracks-user/

@dataclass
class RemoveUsersSavedTracksResponse extends VoidResponse :


    # Check User’s Saved Tracks
    *
    # GET /v1/me/tracks/contains?ids={ids
    # https://developer.spotify.com/web-api/check-users-saved-tracks/

@dataclass
class CheckUsersSavedTracksResponse extends Array<bool> :


    # Save albums for user
    *
    # PUT /v1/me/albums?ids={ids
    # https://developer.spotify.com/web-api/save-albums-user/

@dataclass
class SaveAlbumsForUserResponse extends VoidResponse :


    # Get user's saved albums
    *
    # GET /v1/me/albums
    # https://developer.spotify.com/web-api/get-users-saved-albums/

@dataclass
class UsersSavedAlbumsResponse extends PagingObject<SavedAlbumObject> :


    # Remove Albums for Current User
    *
    # DELETE /v1/me/albums?ids={ids
    # https://developer.spotify.com/web-api/remove-albums-user/

@dataclass
class RemoveAlbumsForUserResponse extends VoidResponse :


    # Check user's saved albums
    *
    # GET /v1/me/albums/contains?ids={ids
    # https://developer.spotify.com/web-api/check-users-saved-albums/

@dataclass
class CheckUserSavedAlbumsResponse extends Array<bool> :


    # Get user's saved shows
    *
    # GET /v1/me/shows
    # https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-users-saved-shows

type UsersSavedShowsResponse = PagingObject<SavedShowObject>


    # Save Shows for Current User
    *
    # PUT /v1/me/shows
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/save-shows-user

@dataclass
class SaveShowsForUserResponse extends VoidResponse :


    # Remove User's Saved Shows
    *
    # DELETE /v1/me/shows
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-shows-user

@dataclass
class RemoveShowsForUserResponse extends VoidResponse :


    # Check User's Saved Shows
    *
    # GET /v1/me/shows/contains
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-shows

@dataclass
class CheckUserSavedShowsResponse extends Array<bool> :


    # Get User's Saved Episodes
    *
    # GET /v1/me/episodes
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-episodes

type UsersSavedEpisodesResponse = PagingObject<SavedEpisodeObject>


    # Save Episodes for Current User
    *
    # PUT /v1/me/episodes
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/save-episodes-user

@dataclass
class SaveEpisodesForUserResponse extends VoidResponse :


    # Remove User's Saved Episodes
    *
    # DELETE /v1/me/episodes
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-episodes-user

@dataclass
class RemoveEpisodesForUserResponse extends VoidResponse :


    # Check User's Saved Episodes
    *
    # GET /v1/me/shows/episodes
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-episodes

@dataclass
class CheckUserSavedEpisodesResponse extends Array<bool> :


    # Get a User’s Top Artists and Tracks (Note: This is only Artists)
    *
    # GET /v1/me/top/{type
    # https://developer.spotify.com/web-api/get-users-top-artists-and-tracks/

@dataclass
class UsersTopArtistsResponse extends PagingObject<ArtistObjectFull> :


    # Get a User’s Top Artists and Tracks (Note: This is only Tracks)
    *
    # GET /v1/me/top/{type
    # https://developer.spotify.com/web-api/get-users-top-artists-and-tracks/

@dataclass
class UsersTopTracksResponse extends PagingObject<TrackObjectFull> :


    # Get a User’s Recently Played Tracks
    *
    # GET /v1/me/player/recently-played
    # https://developer.spotify.com/web-api/get-users-top-artists-and-tracks/

@dataclass
class UsersRecentlyPlayedTracksResponse extends CursorBasedPagingObject<PlayHistoryObject> :


    # Add an item to the end of the user’s current playback queue.
    *
    # POST /v1/me/player/queue
    # https://developer.spotify.com/documentation/web-api/reference/player/add-to-queue/

@dataclass
class AddToQueueResponse extends VoidResponse :


    # Get the list of objects that make up the user's queue.
    *
    # GET /v1/me/player/queue
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-queue

@dataclass
class UsersQueueResponse:
    currently_playing: TrackObjectFull | EpisodeObjectFull
    queue: Array<TrackObjectFull | EpisodeObjectFull>



    # Get recommendations based on seeds
    *
    # GET /v1/recommendations
    # https://developer.spotify.com/get-recommendations/

@dataclass
class RecommendationsFromSeedsResponse extends RecommendationsObject :


    # Get available genre seeds
    *
    # GET /v1/recommendations/available-genre-seeds
    # https://developer.spotify.com/web-api/get-recommendations/#available-genre-seeds

@dataclass
class AvailableGenreSeedsResponse:
    genres: list[str]



    # Get Available Markets
    *
    # GET /v1/markets
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-available-markets

@dataclass
class AvailableMarketsResponse:
    markets: list[str]



    # Search for an album
    *
    # GET /v1/search?type=album
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class AlbumSearchResponse:
    albums: PagingObject<AlbumObjectSimplified>



    # Search for an artist
    *
    # GET /v1/search?type=artist
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class ArtistSearchResponse:
    artists: PagingObject<ArtistObjectFull>



    # Search for a playlist
    *
    # GET /v1/search?type=playlist
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class PlaylistSearchResponse:
    playlists: PagingObject<PlaylistObjectSimplified>



    # Search for a track
    *
    # GET /v1/search?type=track
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class TrackSearchResponse:
    tracks: PagingObject<TrackObjectFull>



    # Search for a show
    *
    # GET /v1/search?type=show
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class ShowSearchResponse:
    shows: PagingObject<ShowObjectSimplified>



    # Search for a episode
    *
    # GET /v1/search?type=episode
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class EpisodeSearchResponse:
    episodes: PagingObject<EpisodeObjectSimplified>



    # Search for artists/albums/tracks/playlists/show/episode
    *
    # GET /v1/search
    # https://developer.spotify.com/web-api/search-item/

@dataclass
class SearchRespon:
    extends
        Partial<ArtistSearchResponse>,
        Partial<AlbumSearchResponse>,
        Partial<TrackSearchResponse>,
        Partial<PlaylistSearchResponse>,
        Partial<ShowSearchResponse>,
        Partial<EpisodeSearchResponse>
{


    # Get an Show
    *
    # GET /v1/shows/{id
    # https://developer.spotify.com/web-api/get-show/

type SingleShowResponse = ShowObject


    # Get Several Shows
    *
    # GET /v1/shows?ids={ids
    # https://developer.spotify.com/documentation/web-api/reference/shows/get-several-shows/

@dataclass
class MultipleShowsResponse:
    shows: ShowObjectSimplified[]



    # Get an Shows’s Episodes
    *
    # GET /v1/shows/{id/episodes
    # https://developer.spotify.com/documentation/web-api/reference/shows/get-shows-episodes/

type ShowEpisodesResponse = PagingObject<EpisodeObjectSimplified>


    # Get an Episode
    *
    # GET /v1/episodes/{id
    # https://developer.spotify.com/documentation/web-api/reference/episodes/get-an-episode/

type SingleEpisodeResponse = EpisodeObject


    # Get Several Episodes
    *
    # GET /v1/episodes?ids={ids
    # https://developer.spotify.com/documentation/web-api/reference/episodes/get-several-episodes/

@dataclass
class MultipleEpisodesResponse:
    episodes: EpisodeObject[]



    # Get a track
    *
    # GET /v1/tracks/{id
    # https://developer.spotify.com/web-api/get-track/

@dataclass
class SingleTrackResponse extends TrackObjectFull :


    # Get multiple tracks
    *
    # GET /v1/tracks?ids={ids
    # https://developer.spotify.com/web-api/get-several-tracks/

@dataclass
class MultipleTracksResponse:
    tracks: TrackObjectFull[]



    # Get user profile
    *
    # GET /v1/users/{user_id
    # https://developer.spotify.com/web-api/get-users-profile/

@dataclass
class UserProfileResponse extends UserObjectPublic :


    # Get a list of a user's playlists
    *
    # GET /v1/users/{user_id/playlists
    # https://developer.spotify.com/web-api/get-list-users-playlists/

@dataclass
class ListOfUsersPlaylistsResponse extends PagingObject<PlaylistObjectSimplified> :


    # Get a list of the current user's playlists
    *
    # GET /v1/me/playlists
    # https://developer.spotify.com/web-api/get-list-users-playlists/

@dataclass
class ListOfCurrentUsersPlaylistsResponse extends PagingObject<PlaylistObjectSimplified> :


    # Get a playlist
    *
    # GET /v1/users/{user_id/playlists/{playlist_id
    # https://developer.spotify.com/web-api/get-playlist/

@dataclass
class SinglePlaylistResponse extends PlaylistObjectFull :


    # Get a playlist's tracks
    *
    # GET /v1/users/{user_id/playlists/{playlist_id/tracks
    # https://developer.spotify.com/web-api/get-playlists-tracks/

@dataclass
class PlaylistTrackResponse extends PagingObject<PlaylistTrackObject> :


    # Create a Playlist
    *
    # POST /v1/users/{user_id/playlists
    # https://developer.spotify.com/web-api/create-playlist/

@dataclass
class CreatePlaylistResponse extends PlaylistObjectFull :


    # Change a Playlist’s Details
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id
    # https://developer.spotify.com/web-api/change-playlist-details/

@dataclass
class ChangePlaylistDetailsResponse extends VoidResponse :

    # Change a Playlist’s Details
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id
    # https://developer.spotify.com/web-api/change-playlist-details/
    # @deprecated Use `ChangePlaylistDetailsResponse` instead

@dataclass
class ChangePlaylistDetailsReponse extends ChangePlaylistDetailsResponse :


    # Add Tracks to a Playlist
    *
    # POST /v1/users/{user_id/playlists/{playlist_id/tracks
    # https://developer.spotify.com/web-api/add-tracks-to-playlist/

@dataclass
class AddTracksToPlaylistResponse extends PlaylistSnapshotResponse :


    # Remove Tracks from a Playlist
    *
    # DELETE /v1/users/{user_id/playlists/{playlist_id/tracks
    # https://developer.spotify.com/web-api/remove-tracks-playlist/

@dataclass
class RemoveTracksFromPlaylistResponse extends PlaylistSnapshotResponse :


    # Reorder a Playlist’s Tracks
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id/tracks
    # https://developer.spotify.com/web-api/reorder-playlists-tracks/

@dataclass
class ReorderPlaylistTracksResponse extends PlaylistSnapshotResponse :


    # Replace a Playlist’s Tracks
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id/tracks
    # https://developer.spotify.com/web-api/replace-playlists-tracks/

@dataclass
class ReplacePlaylistTracksResponse extends PlaylistSnapshotResponse :


    # Upload a Custom Playlist Cover Image
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id/images
    # https://developer.spotify.com/web-api/upload-a-custom-playlist-cover-image/

@dataclass
class UploadCustomPlaylistCoverImageResponse extends VoidResponse :

    # Upload a Custom Playlist Cover Image
    *
    # PUT /v1/users/{user_id/playlists/{playlist_id/images
    # https://developer.spotify.com/web-api/upload-a-custom-playlist-cover-image/
    # @deprecated Use `UploadCustomPlaylistCoverImageResponse` instead

@dataclass
class UploadCustomPlaylistCoverImageReponse extends UploadCustomPlaylistCoverImageResponse :


    # Check if Users Follow a Playlist
    *
    # GET /v1/users/{user_id/playlists/{playlist_id/followers/contains
    # https://developer.spotify.com/web-api/check-user-following-playlist/

@dataclass
class UsersFollowPlaylistResponse extends Array<bool> :

    # Check if Users Follow a Playlist
    *
    # GET /v1/users/{user_id/playlists/{playlist_id/followers/contains
    # https://developer.spotify.com/web-api/check-user-following-playlist/
    # @deprecated Use `UsersFollowPlaylistResponse` instead

@dataclass
class UsersFollowPlaylistReponse extends UsersFollowPlaylistResponse :

@dataclass
class UserDevicesResponse:
    devices: UserDevice[]


@dataclass
class CurrentPlaybackResponse extends CurrentlyPlayingObject, PlaybackObject :

@dataclass
class CurrentlyPlayingResponse extends CurrentlyPlayingObject :

#
# Objects from the Object Models of the Spotify Web Api, ordered alphabetically.
# [Object Model](https://developer.spotify.com/web-api/object-model)
#


    # Full Album Object
    # [album object (full)](https://developer.spotify.com/web-api/object-model/#album-object-simplified)

@dataclass
class AlbumObjectFull extends AlbumObjectSimplified:

        # The copyright statements of the album.
    
    copyrights: list[CopyrightObject]

        # Known external IDs for the album.
    
    external_ids: ExternalIdObject

        # A list of the genres used to classify the album.
        # For example: `"Prog Rock"` , `"Post-Grunge"`. (If not yet classified, the array is empty.)
    
    genres: list[str]

        # The label for the album.
    
    label: str

        # The popularity of the album. The value will be between `0` and `100`, with `100` being the most popular.
        # The popularity is calculated from the popularity of the album’s individual tracks
    
    popularity: int

        # The tracks of the album.
    
    tracks: PagingObject<TrackObjectSimplified>



    # Simplified Album Object
    # [album object (simplified)](https://developer.spotify.com/web-api/object-model/#album-object-simplified)

@dataclass
class AlbumObjectSimplified extends ContextObject:

        # The field is present when getting an artist’s albums.
        # Possible values are “album”, “single”, “compilation”, “appears_on”.
        # Compare to album_type this field represents relationship between the artist and the album.
    
    album_group: "album" | "single" | "compilation" | "appears_on" | None

        # The type of the album: one of “album”, “single”, or “compilation”.
    
    album_type: "album" | "single" | "compilation"

        # The artists of the album.
        # Each artist object includes a link in href to more detailed information about the artist.
    
    artists: ArtistObjectSimplified[]

        # The markets in which the album is available: [ISO 3166-1 alpha-2 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        # Note that an album is considered available in a market when at least 1 of its tracks is available in that market.
    
    available_markets: list[str] | None

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the album.
    
    id: str

        # The cover art for the album in various sizes, widest first.
    
    images: list[ImageObject]

        # The name of the album. In case of an album takedown, the value may be an empty str.
    
    name: str

        # The date the album was first released, for example `1981`.
        # Depending on the precision, it might be shown as `1981-12` or `1981-12-15`.
    
    release_date: str

        # The precision with which release_date value is known: `year`, `month`, or `day`.
    
    release_date_precision: "year" | "month" | "day"

        # Part of the response when [Track Relinking](https://developer.spotify.com/documentation/general/guides/track-relinking-guide/) is applied,
        # the original track is not available in the given market, and Spotify did not have any tracks to relink it with.
        # The track response will still contain metadata for the original track,
        # and a restrictions object containing the reason why the track is not available: `"restrictions" : {"reason" : "market"`
    
    restrictions: RestrictionsObject | None
    type: "album"

        # The number of tracks in the album.
    
    total_tracks: int



    # Full Artist Object
    # [artist object (full)](https://developer.spotify.com/web-api/object-model/)

@dataclass
class ArtistObjectFull extends ArtistObjectSimplified:

        # Information about the followers of the artist.
    
    followers: FollowersObject

        # A list of the genres the artist is associated with.
        # For example: `"Prog Rock"` , `"Post-Grunge"`.
        # (If not yet classified, the array is empty.)
    
    genres: list[str]

        # Images of the artist in various sizes, widest first.
    
    images: list[ImageObject]

        # The popularity of the artist. The value will be between `0` and `100`, with `100` being the most popular.
        # The artist’s popularity is calculated from the popularity of all the artist’s tracks.
    
    popularity: int



    # Simplified Artist Object
    # [artist object (simplified)](https://developer.spotify.com/web-api/object-model/)

@dataclass
class ArtistObjectSimplified extends ContextObject:

        # The name of the artist.
    
    name: str

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist.
    
    id: str
    type: "artist"



    # Audio Features Object
    # https://developer.spotify.com/web-api/object-model/#audio-features-object

@dataclass
class AudioFeaturesObject:
    acousticness: int
    analysis_url: str
    danceability: int
    duration_ms: int
    energy: int
    id: str
    instrumentalness: int
    key: int
    liveness: int
    loudness: int
    mode: int
    speechiness: int
    tempo: int
    time_signature: int
    track_href: str
    type: "audio_features"
    uri: str
    valence: int



    # Audio Analysis Object
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-analysis

@dataclass
class AudioAnalysisObject:
    meta: AudioAnalysisMeta
    track: AudioAnalysisTrack
    bars: AudioAnalysisIntervalObject[]
    beats: AudioAnalysisIntervalObject[]
    sections: AudioAnalysisSection[]
    segments: AudioAnalysisSegment[]
    tatums: AudioAnalysisIntervalObject[]


@dataclass
class AudioAnalysisMeta:
    analyzer_version: str
    platform: str
    detailed_status: str
    status_code: int
    timestamp: int
    analysis_time: int
    input_process: str


@dataclass
class AudioAnalysisTrack:
    num_samples: int
    duration: int
    sample_md5: str
    offset_seconds: int
    window_seconds: int
    analysis_sample_rate: int
    analysis_channels: int
    end_of_fade_in: int
    start_of_fade_out: int
    loudness: int
    tempo: int
    tempo_confidence: int
    time_signature: int
    time_signature_confidence: int
    key: int
    key_confidence: int
    mode: int
    mode_confidence: int
    codestring: str
    code_version: int
    echoprintstring: str
    echoprint_version: int
    synchstring: str
    synch_version: int
    rhythmstring: str
    rhythm_version: int


@dataclass
class AudioAnalysisIntervalObject:
    start: int
    duration: int
    confidence: int


@dataclass
class AudioAnalysisSection:
    start: int
    duration: int
    confidence: int
    loudness: int
    tempo: int
    tempo_confidence: int
    key: int
    key_confidence: int
    mode: int
    mode_confidence: int
    time_signature: int
    time_signature_confidence: int


@dataclass
class AudioAnalysisSegment:
    start: int
    duration: int
    confidence: int
    loudness_start: int
    loudness_max: int
    loudness_max_time: int
    loudness_end: int
    pitches: int[]
    timbre: int[]



    # Category Object
    # [category object](https://developer.spotify.com/web-api/object-model/)

@dataclass
class CategoryObject:
    href: str
    icons: list[ImageObject]
    id: str
    name: str



    # Copyright object
    # [copyright object](https://developer.spotify.com/web-api/object-model/)

@dataclass
class CopyrightObject:
    text: str
    type: "C" | "P"



    # Cursor object
    # [cursor object](https://developer.spotify.com/web-api/object-model/)

@dataclass
class CursorObject:
    after: str
    before: str | None



    # Error object
    # [error object](https://developer.spotify.com/web-api/object-model/)

@dataclass
class ErrorObject:

        # The HTTP status code (also returned in the response header
        # see [Response Status Codes](https://developer.spotify.com/documentation/web-api/#response-status-codes) for more information).
    
    status: int

        # A short description of the cause of the error.
    
    message: str



    # External Id object
    # [](https://developer.spotify.com/web-api/object-model/)
    *
    # Note that there might be other types available, it couldn't be found in the docs.

@dataclass
class ExternalIdObject:
    isrc: str | None
    ean: str | None
    upc: str | None



    # External Url Object
    # [](https://developer.spotify.com/web-api/object-model/)
    *
    # Note that there might be other types available, it couldn't be found in the docs.

@dataclass
class ExternalUrlObject:
    spotify: str



    # Followers Object
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class FollowersObject:

        # A link to the Web API endpoint providing full details of the followers `None` if not available.
        # Please note that this will always be set to `None`, as the Web API does not support it at the moment.
    
    href: None

        # The total number of followers.
    
    total: int



    # Image Object
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class ImageObject:

        # The image height in pixels. If unknown: `None` or not returned.
    
    height: int | None

        # The source URL of the image.
    
    url: str

        # The image width in pixels. If unknown: None or not returned.
    
    width: int | None



    # Paging Object wrapper used for retrieving collections from the Spotify API.
    # [](https://developer.spotify.com/web-api/object-model/#paging-object)

@dataclass
class PagingObject<T>:
    href: str
    items: T[]
    limit: int
    next: str | None
    offset: int
    previous: str | None
    total: int



    # Cursor Based Paging Object wrappers used for retrieving collections from the Spotify API.
    # [](https://developer.spotify.com/web-api/object-model/#cursor-based-paging-object)

@dataclass
class CursorBasedPagingObject<T>:
    href: str
    items: T[]
    limit: int
    next: str | None
    cursors: CursorObject
    total: int | None



    # Base Playlist Object. Does not in itself exist in Spotify Web Api,
    # but needs to be made since the tracks types vary in the Full and Simplified versions.

@dataclass
class PlaylistBaseObject extends ContextObject:

        # Returns `true` if context is not search and the owner allows other users to modify the playlist.
        # Otherwise returns `false`.
    
    collaborative: bool

        # The playlist description. Only returned for modified, verified playlists, otherwise None.
    
    description: str | None

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the playlist.
    
    id: str

        # Images for the playlist. The array may be empty or contain up to three images.
        # The images are returned by size in descending order.
        # See [Working with Playlists](https://developer.spotify.com/documentation/general/guides/working-with-playlists/).
        # Note: If returned, the source URL for the image (`url`) is temporary and will expire in less than a day.
    
    images: list[ImageObject]

        # The name of the playlist.
    
    name: str

        # The user who owns the playlist.
    
    owner: UserObjectPublic

        # The playlist’s public/private status:
        # `true` the playlist is public,
        # `false` the playlist is private,
        # or `None` the playlist status is not relevant.
    
    public: bool | None

        # The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version:
        # see [Remove tracks from a playlist](https://developer.spotify.com/documentation/web-api/reference/playlists/remove-tracks-playlist/).
    
    snapshot_id: str
    type: "playlist"



    # Playlist Object Full
    # [](https://developer.spotify.com/web-api/object-model/#playlist-object-full)

@dataclass
class PlaylistObjectFull extends PlaylistBaseObject:

        # Information about the followers of the playlist.
    
    followers: FollowersObject

        # Information about the tracks of the playlist.
    
    tracks: PagingObject<PlaylistTrackObject>



    # Playlist Object Simplified
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class PlaylistObjectSimplified extends PlaylistBaseObject:
    tracks: {
        href: str
        total: int
    



    # The Track Object in Playlists
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class PlaylistTrackObject:
    added_at: str
    added_by: UserObjectPublic
    is_local: bool
    track: TrackObjectFull | None



    # Recommendations Object
    # [](https://developer.spotify.com/web-api/object-model/#recommendations-object)

@dataclass
class RecommendationsObject:
    seeds: RecommendationsSeedObject[]
    tracks: RecommendationTrackObject[]



    # Recommendation Track Object
    # Uses the same object structure as Full Track Object, but with `album.album_type` in caps.

@dataclass
class RecommendationTrackObject extends Omit<TrackObjectFull, "album">:
    album: RecommendationAlbumObject



    # Recommendation Album Object
    # Uses the same object structure as Simple Album Object, but with `album_type` in caps.

@dataclass
class RecommendationAlbumObject extends Omit<AlbumObjectSimplified, "album_type">:

        # The type of the album: one of “ALBUM”, “SINGLE”, or “COMPILATION”.
        # Note that this differs from the types returned by all other spotify APIs by being in all caps.
    
    album_type: "ALBUM" | "SINGLE" | "COMPILATION"



    # Recommendations Seed Object
    # [](https://developer.spotify.com/web-api/object-model/#recommendations-seed-object)

@dataclass
class RecommendationsSeedObject:
    afterFilteringSize: int
    afterRelinkingSize: int
    href: str
    id: str
    initialPoolSize: int
    type: "artist" | Literal["track"] | "genre"



    # Saved Track Object in Playlists
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class SavedTrackObject:
    added_at: str
    track: TrackObjectFull



    # Saved Track Object in Playlists
    # [](https://developer.spotify.com/web-api/object-model/)

@dataclass
class SavedAlbumObject:
    added_at: str
    album: AlbumObjectFull



    # Saved Episode Object
    # [saved episode object](https://developer.spotify.com/documentation/web-api/reference/#object-savedepisodeobject)

@dataclass
class SavedEpisodeObject:

        # The date and time the episode was saved.
    
    added_at: str

        # Information about the episode.
    
    episode: EpisodeObject



    # Saved Show Object
    # [saved show object](https://developer.spotify.com/documentation/web-api/reference/object-model/#saved-show-object)

@dataclass
class SavedShowObject:

        # The date and time the show was saved.
    
    added_at: str

        # Information about the show.
    
    show: ShowObjectSimplified



    # Full Track Object
    # [track object (full)](https://developer.spotify.com/web-api/object-model/#track-object-full)

@dataclass
class TrackObjectFull extends TrackObjectSimplified:

        # The album on which the track appears.
    
    album: AlbumObjectSimplified

        # Known external IDs for the track.
    
    external_ids: ExternalIdObject

        # The popularity of the track. The value will be between `0` and `100`, with `100` being the most popular.
        # The popularity of a track is a value between `0` and `100`, with `100` being the most popular.
        # The popularity is calculated by algorithm and is based, in the most part,
        # on the total number of plays the track has had and how recent those plays are.
    
    popularity: int

        # Whether or not the track is from a local file.
    
    is_local: bool | None



    # Simplified Track Object
    # [track object (simplified)](https://developer.spotify.com/web-api/object-model/#track-object-simplified)

@dataclass
class TrackObjectSimplified:

        # The artists who performed the track.
    
    artists: ArtistObjectSimplified[]

        # A list of the countries in which the track can be played,
        # identified by their [ISO 3166-1 alpha-2 code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    
    available_markets: list[str] | None

        # The disc number (usually `1` unless the album consists of more than one disc).
    
    disc_number: int

        # The track length in milliseconds.
    
    duration_ms: int

        # Whether or not the track has explicit lyrics (`true` = yes it does `false` = no it does not OR unknown).
    
    explicit: bool

        # Known external URLs for this track.
    
    external_urls: ExternalUrlObject

        # A link to the Web API endpoint providing full details of the track.
    
    href: str

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the track.
    
    id: str

        # Part of the response when [Track Relinking](https://developer.spotify.com/documentation/general/guides/track-relinking-guide/) is applied.
        # If `true`, the track is playable in the given market. Otherwise, `false`.
    
    is_playable: bool | None

        # Part of the response when [Track Relinking](https://developer.spotify.com/documentation/general/guides/track-relinking-guide/) is applied,
        # and the requested track has been replaced with different track.
        # The track in the `linked_from` object contains information about the originally requested track.
    
    linked_from: TrackLinkObject | None

        # Part of the response when [Track Relinking](https://developer.spotify.com/documentation/general/guides/track-relinking-guide/) is applied,
        # the original track is not available in the given market, and Spotify did not have any tracks to relink it with.
        # The track response will still contain metadata for the original track, and a restrictions object containing the reason
        # why the track is not available: `"restrictions" : {"reason" : "market"`.
    
    restrictions: RestrictionsObject | None

        # The name of the track.
    
    name: str

        # A link to a 30 second preview (MP3 format) of the track. Can be None
    
    preview_url: str | None

        # The number of the track. If an album has several discs, the track number is the number on the specified disc.
    
    track_number: int

        # The object type: “track”.
    
    type: Literal["track"]

        # The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the track.
    
    uri: str



    # Track Link Object
    # [](https://developer.spotify.com/web-api/object-model/#track-object-simplified)

@dataclass
class TrackLinkObject:
    external_urls: ExternalUrlObject
    href: str
    id: str
    type: Literal["track"]
    uri: str



    # Episode Object
    # [episode object](https://developer.spotify.com/documentation/web-api/reference/#object-episodeobject)

@dataclass
class EpisodeObject extends EpisodeObjectSimplified:

        # The show on which the episode belongs.
    
    show: ShowObjectSimplified

        # The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode.
    
    uri: str


@dataclass
class EpisodeObjectFull extends EpisodeObject :


    # Simplified Episode Object
    # [episode object (simplified)](https://developer.spotify.com/documentation/web-api/reference/object-model/#episode-object-simplified)

@dataclass
class EpisodeObjectSimplified extends ContextObject:

        # A URL to a 30 second preview (MP3 format) of the episode. None if not available.
    
    audio_preview_url: str | None

        # A description of the episode.
    
    description: str

        # The episode length in milliseconds.
    
    duration_ms: int

        # Whether or not the episode has explicit content (true = yes it does false = no it does not OR unknown).
    
    explicit: bool

        # A description of the episode. This field may contain HTML tags.
    
    html_description: str

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode.
    
    id: str

        # The cover art for the episode in various sizes, widest first.
    
    images: list[ImageObject]

        # True if the episode is hosted outside of Spotify’s CDN.
    
    is_externally_hosted: bool

        # True if the episode is playable in the given market. Otherwise false.
    
    is_playable: bool

        # The language used in the episode, identified by a [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.
        # @deprecated Note: This field is deprecated and might be removed in the future. Please use the languages field instead.
    
    language: str

        # A list of the languages used in the episode, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.
        # Optional because sometimes only the deprecated language field is set and this one isn't set at all.
    
    languages: list[str] | None

        # The name of the episode.
    
    name: str

        # The date the episode was first released, for example "1981-12-15". Depending on the precision, it might be shown as "1981" or "1981-12".
    
    release_date: str

        # The precision with which release_date value is known: "year", "month", or "day".
    
    release_date_precision: str

        # The user’s most recent position in the episode. Set if the supplied access token is a user token and has the scope user-read-playback-position.
    
    resume_point: ResumePointObject | None
    type: "episode"



    # Resume Point Object
    # [resume point object](https://developer.spotify.com/documentation/web-api/reference/object-model/#resume-point-object)

@dataclass
class ResumePointObject:

        # Whether or not the episode has been fully played by the user.
    
    fully_played: bool

        # The user’s most recent position in the episode in milliseconds.
    
    resume_position_ms: int



    # Show Object
    # [show object](https://developer.spotify.com/documentation/web-api/reference/#object-showobject)

@dataclass
class ShowObject extends ShowObjectSimplified:
    episodes: PagingObject<EpisodeObjectSimplified>
    external_urls: ExternalUrlObject


@dataclass
class ShowObjectFull extends ShowObject :

    # Simplified Show Object
    # [show object (simplified)](https://developer.spotify.com/documentation/web-api/reference/object-model/#show-object-simplified)

@dataclass
class ShowObjectSimplified extends ContextObject:

        # A list of the countries in which the show can be played, identified by their [ISO 3166-1 alpha-2 code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    
    available_markets: list[str]

        # The copyright statements of the show.
    
    copyrights: list[CopyrightObject]

        # A description of the show.
    
    description: str

        # A description of the show. This field may contain HTML tags.
    
    html_description: str

        # Whether or not the show has explicit content (true = yes it does false = no it does not OR unknown).
    
    explicit: bool

        # The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the show.
    
    id: str

        # The cover art for the show in various sizes, widest first.
    
    images: list[ImageObject]

        # True if all of the show’s episodes are hosted outside of Spotify’s CDN. This field might be None in some cases.
    
    is_externally_hosted: bool | None

        # A list of the languages used in the show, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.
    
    languages: list[str]

        # The media type of the show.
    
    media_type: str

        # The name of the show.
    
    name: str

        # The publisher of the show.
    
    publisher: str

        # The object type: “show”.
    
    type: Literal["show"]
    # This is found in https://developer.spotify.com/documentation/web-api/reference/shows/get-a-show/ but not in
    # https://developer.spotify.com/documentation/web-api/reference/object-model/#show-object-full.
    # Also it is not always sent, so it is marked optional here.

        # Total number of episodes in the show.
    
    total_episodes: int | None



    # User Object (Private)
    # [](https://developer.spotify.com/web-api/object-model/#track-object-simplified)

@dataclass
class UserObjectPrivate extends UserObjectPublic:
    birthdate: str
    country: str
    email: str
    product: str


    # User Object (Public)
    # [](https://developer.spotify.com/web-api/object-model/#track-object-simplified)

@dataclass
class UserObjectPublic:
    display_name: str | None
    external_urls: ExternalUrlObject
    followers: FollowersObject | None
    href: str
    id: str
    images: list[ImageObject] | None
    type: "user"
    uri: str


    # Context Object
    # [](https://developer.spotify.com/web-api/object-model/#context-object)

@dataclass
class ContextObject:

    # The object type.
    
    type: "artist" | "playlist" | "album" | Literal["show"] | "episode"

    # A link to the Web API endpoint providing full details.
    
    href: str
    
        # Known external URLs.
    
    external_urls: ExternalUrlObject
    
        # The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids).
    
    uri: str


    # Play History Object
    # [](https://developer.spotify.com/web-api/web-api-personalization-endpoints/get-recently-played/#play-history-object)

@dataclass
class PlayHistoryObject:
    track: TrackObjectFull
    played_at: str
    context: ContextObject

@dataclass
class PlaybackObject:
    shuffle_state: bool
    repeat_state: "off" | Literal["track"] | "context"

@dataclass
class CurrentlyPlayingObject:
    timestamp: int
    device: UserDevice
    actions: ActionsObject
    progress_ms: int | None
    is_playing: bool
    item: TrackObjectFull | EpisodeObject | None
    context: ContextObject | None
    currently_playing_type: Literal["track"] | "episode" | "ad" | "unknown"

@dataclass
class UserDevice:
    id: str | None
    is_active: bool
    is_restricted: bool
    is_private_session: bool
    name: str
    type: str
    volume_percent: int | None


@dataclass
class ActionsObject:
    disallows: DisallowsObject


@dataclass
class DisallowsObject:
    interrupting_playback: bool | None
    pausing: bool | None
    resuming: bool | None
    seeking: bool | None
    skipping_next: bool | None
    skipping_prev: bool | None
    toggling_repeat_context: bool | None
    toggling_repeat_track: bool | None
    toggling_shuffle: bool | None
    transferring_playback: bool | None