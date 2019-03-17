class Movie():
    '''
    This class provides a way to store movie related information.

    Attributes:
        movie_title (string): The title of the movie.
        storyline (string): A short storyline of the movie.
        poster_url (string): Image URL of the movie poster.
        trailer_link (string): Link URL of the movie trailer.
    '''

    def __init__(self, movie_title, storyline, poster_url, trailer_link):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_link
