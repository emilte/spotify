class Scope:
    playlist_modify_public = 'playlist-modify-public'
    playlist_modify_private = 'playlist-modify-private'
    user_modify_playback_state = 'user-modify-playback-state'
    user_read_playback_state = 'user-read-playback-state'


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
