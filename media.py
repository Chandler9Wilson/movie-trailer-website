# define movie class
import webbrowser

class Movie():

    def __init__(self, info):
        '''assigns the basic info of the movie to the class instance'''
        self.title = info["movie_title"]
        self.poster_image_url = info["poster_image_url"]
        self.trailer_youtube_url = info["trailer_youtube_url"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
