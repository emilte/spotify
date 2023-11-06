from time import sleep

from utils import Scope
from spotipy_client import SpotipyClient

url = "https://api.spotify.com"

MIN = 60
HOUR = 60 * MIN

SLEEP_S = 1.5 * HOUR
# SLEEP_S = 2 * HOUR

USER = 'emiltelstad'

if __name__ == '__main__':

    sleep(SLEEP_S)
    sp = SpotipyClient(username=USER, scope=Scope.user_modify_playback_state)
    sp.pause_playback()
