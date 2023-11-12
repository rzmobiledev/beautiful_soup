import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.billboard.com/charts/hot-100/"


class SearchPlayList:
    """Search music by year and scrape it"""

    def __init__(self, date_year: str):
        self.date_year = date_year

    def is_date_format(self) -> bool:
        """Check if date string has a correct format"""
        try:
            datetime.fromisoformat(self.date_year)
        except ValueError:
            return False
        else:
            return True

    @property
    def scrap_song_lists(self):
        """Scrapping all songs based on year"""

        if not self.is_date_format():
            return

        play_list_url = URL + self.date_year

        response = requests.get(url=play_list_url).text
        soup = BeautifulSoup(markup=response, features="html.parser")

        # collect all songs from list
        all_song_datas = [song.getText() for song in soup.select(selector="h3#title-of-a-story.a-font-primary-bold-s")]

        # remove first and second index
        all_song_datas.pop(0)
        all_song_datas.pop(0)

        # removing spaces and new line from lists
        all_songs = [''.join(song.split()) if '' == '\n\t\n' in song.split() else ' '.join(song.split()) for song in all_song_datas]

        # collect all singers from list
        # all_singer_datas = [singer.getText() for singer in soup.select(selector="span.c-label.a-font-primary-s")]

        # removing spaces and new line from lists
        # all_singers = [''.join(singer.split()) if '' == '\n\t\n' in singer.split() else ' '.join(singer.split()) for singer in all_singer_datas]

        # delete all contents from all_songs.csv
        # open("all_songs.csv", "w").close()

        all_song_lists = []

        # for num in range(len(all_singers)):
            # with open("all_songs.csv", "a") as file:
                # file.write(f"{num + 1}, {all_songs[num]}, {all_singers[num]}\n")
            # print(all_singers[num])
            # all_song_lists.append(all_songs[num])
        return all_songs


# should_continue = True
# while should_continue:
#
#     search_song_in_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#     if search_song_in_year.upper() == "EXIT":
#         should_continue = False
#     scrap_song_lists(search_song_in_year)