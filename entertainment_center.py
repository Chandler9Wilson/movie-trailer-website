import json
import media
import fresh_tomatoes

movies = {}

with open('movie_data.json') as data_file:
    # imports json file
    data = json.load(data_file)


def data_to_movie(movie_info):
    # loops over movies dictionary after import from json
    for movie in movie_info['movies']:
        # instatiates Movie then adds to the  movies dictionary
        movie_title = movie["movie_title"]
        movies[movie_title] = media.Movie(movie)

data_to_movie(data)
fresh_tomatoes.open_movies_page(movies)
