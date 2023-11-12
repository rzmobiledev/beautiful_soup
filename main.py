from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

from search_music import SearchPlayList

load_dotenv()

"""
I am creating a spotify playlist to my spotify profile
by scrapping Billboard chart website
"""

auth = SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=os.environ.get("SPOTIFY_ID"),
    client_secret=os.environ.get("SPOTIFY_SECRET"),
    redirect_uri=os.environ.get("SPOTIFY_REDIRECT_URL"),
)

spotify = Spotify(auth_manager=auth)
user_id = spotify.current_user()['id']


# search artists
# responses = spotify.search(q="artist:Mariah Carey", type="artist")
# print(responses["artists"]["items"])

search_song_in_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
search_playlist = SearchPlayList(search_song_in_year)
all_songs = search_playlist.scrap_song_lists

song_uris = []
year = search_song_in_year.split("-")[0]
for song in all_songs:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create playlist
playlist = spotify.user_playlist_create(
    user=user_id,
    name=f"Top 100 songs in {search_song_in_year}",
    public=False
)

spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
