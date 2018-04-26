import webbrowser

class Movie():
    """Class that stores movie data."""

    def __init__(self, title, year, poster_image_url, trailer_youtube_url):
        """Initialize an instance of the class `Movie` with the movie data.
           
        Args:
          title (str): Movie title.
          year (int): Year is which the movie was released.
          poster_image_url (str): URL for the image of the movie poster.
          trailer_youtube_url (str): URL for the movie trailer on Youtube.
        """
        self.title = title
        self.year = year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
  