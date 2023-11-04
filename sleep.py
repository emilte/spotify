from time import sleep

from utils import Scope, scope_builder
from spotipy_client import SpotipyClient

url = "https://api.spotify.com"


def sleep_mode(
    client: SpotipyClient,
    seconds: int,
):
    sleep(seconds)
    client.pause_playback()


if __name__ == '__main__':
    emil = 'emiltelstad'
    sp = SpotipyClient(username=emil, scope=Scope.user_modify_playback_state)
    SLEEP = 5

    sleep_mode(client=sp, seconds=SLEEP)
