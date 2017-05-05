import json
import media
import fresh_tomatoes

movies = {}

with open('movie_data.json') as data_file:
    data = json.load(data_file)


def data_to_movie(movie_info):
    # instatiates Movie then appends to movies list
    for movie in movie_info['movies']:
        movie_title = movie["movie_title"]
        movies[movie_title] = media.Movie(movie)

data_to_movie(data)
fresh_tomatoes.open_movies_page(movies)
