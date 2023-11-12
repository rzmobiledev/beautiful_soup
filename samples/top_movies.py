from bs4 import BeautifulSoup
import requests


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(markup=website, features="html.parser")

movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

