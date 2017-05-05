import json
import media
import fresh_tomatoes

MOVIES = {}

with open('movie_data.json') as data_file:
    DATA = json.load(data_file)

# print data

def data_to_movie(movie_info):
    '''instatiates Movie then appends to movies list'''
    for movie in movie_info['movies']:
        movie_title = movie["movie_title"]
        MOVIES[movie_title] = media.Movie(movie)

data_to_movie(DATA)
print MOVIES
fresh_tomatoes.open_movies_page(MOVIES)
