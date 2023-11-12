import os
import requests
from dotenv import load_dotenv
load_dotenv()

class PlayList:

    def __init__(self, name: str, description: str, public: bool = False):
        self.name = name
        self.description = description
        self.public = public
        self.endpoint = f"https://api.spotify.com/v1/users/{os.environ.get('SPOTIFY_ID')}/playlists"

    def create_playlist(self):
        params = {
            "name": self.name,
            "description": self.description,
            "public": self.public
        }

        response = requests.post(url=self.endpoint, json=params)
        return response.json()