class Scope:
    """
    https://developer.spotify.com/documentation/web-api/concepts/scopes
    """
    ugc_image_upload = 'ugc-image-upload'
    user_read_playback_state = 'user-read-playback-state'
    user_modify_playback_state = 'user-modify-playback-state'
    user_read_currently_playing = 'user-read-currently-playing'
    app_remote_control = 'app-remote-control'
    playlist_read_private = 'playlist-read-private'
    playlist_read_collaborative = 'playlist-read-collaborative'
    playlist_modify_private = 'playlist-modify-private'
    playlist_modify_public = 'playlist-modify-public'
    user_follow_modify = 'user-follow-modify'
    user_follow_read = 'user-follow-read'
    user_read_playback_position = 'user-read-playback-position'
    user_top_read = 'user-top-read'
    user_read_recently_played = 'user-read-recently-played'
    user_library_modify = 'user-library-modify'
    user_library_read = 'user-library-read'
    user_read_email = 'user-read-email'
    user_read_private = 'user-read-private'
    user_soa_link = 'user-soa-link'
    user_soa_unlink = 'user-soa-unlink'
    user_manage_entitlements = 'user-manage-entitlements'
    user_manage_partner = 'user-manage-partner'
    user_create_partner = 'user-create-partner'


def scope_builder(*scopes: str | list[str]):

    if len(scopes) == 0 or scopes[0] is None:
        return None

    if isinstance(scopes[0], (list, tuple)):
        scopes = scopes[0]

    # Must check twice.
    if len(scopes) == 0 or scopes[0] is None:
        return None

    return ' '.join(scopes)


if __name__ == '__main__':
    print(1, scope_builder(Scope.playlist_modify_private))
    print(2, scope_builder(Scope.playlist_modify_private, Scope.playlist_modify_public))
    print(3, scope_builder([Scope.playlist_modify_private, Scope.playlist_modify_public]))
    print(4, scope_builder())
    print(5, scope_builder([]))
    print(6, scope_builder(None))
    print(6, scope_builder(None))
    print(7, scope_builder(None, None))
    print(8, scope_builder(None, [None]))
    print(9, scope_builder([None]))
    print(10, scope_builder([None, None]))
    print(11, scope_builder([None], [None]))
