from bs4 import BeautifulSoup
import requests

response = requests.get("http://web.archive.org/web/20210205074131/https://www.empireonline.com/movies/features/best-movies-2/")

movies_list_page = response.text

soup = BeautifulSoup(movies_list_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")


movie_list = [movie.getText() for movie in movies]
print(movie_list)
revise_list = movie_list[::-1]
with open("movies.txt", "w") as file:
    for movie in revise_list:
        file.write(f"1){movie}\n")