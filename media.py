import webbrowser

class Movie():
    """ This class provides a way to store movie information such as
        -title
        -directors
        -relese date
        -porter image
        -trailer url
    """
    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_release_date, movie_directors, movie_poster, movie_trailer):
        self.title = movie_title
        self.release_date = movie_release_date
        self.directors = movie_directors
        self.poster_image_url = movie_poster
        self.youtube_trailer_url = movie_trailer

    def play_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
