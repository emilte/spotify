import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from mytypes.types import PlaylistObject

url = "https://api.spotify.com"


class Scope:
    a = 'playlist-modify-public'
    b = 'playlist-modify-private'


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

slow_wcs_playlist = 'https://open.spotify.com/playlist/0w0YxOMjvKUFS215VPIK6X?si=af0f0880708744c8'
test = 'https://open.spotify.com/playlist/0zTGrbhMKJcOnCnAn55vGZ?si=34295a468ad74e65'

aa = sp.playlist(playlist_id=test)  # https://developer.spotify.com/documentation/web-api/reference/get-playlist
# bb = sp.playlist_items(playlist_id=test)
# cc = sp.playlist_tracks(playlist_id=test)

# print(aa)
# print(type(aa))
# print(aa.keys())

print(aa)
# print(type(bb))
# print(bb.keys())
# print(bb['items'])

# print(c)
# print(type(cc))
# print(cc.keys())
# print()
# print(cc.items())
# print()
# print(cc.keys())
# for k, v in cc.items():
#     print(k, v)

# for k, v in cc['items']:
#     print(k, v)
pp = PlaylistObject(**aa)
# print(pp.next)
# print(type(pp))
# print(pp)
# print(type(pp.items[0].track))
# print(pp.items[0].track)
# print(pp.items[0].track.artists[0].name)
# print(type(pp.items[0].track.artists[0].name))
# print(pp.items[0].added_at)
# print(cc['items'][0].keys())
