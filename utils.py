class Scope:
    playlist_modify_public = 'playlist-modify-public'
    playlist_modify_private = 'playlist-modify-private'
    user_modify_playback_state = 'user-modify-playback-state'
    user_read_playback_state = 'user-read-playback-state'


def scope_builder(*scopes: Scope):
    return ' '.join(scopes)
