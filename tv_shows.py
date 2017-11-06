import webbrowser

class TV:

    #Access variables using this function
    def __init__(self, TVshow_title, TVshow_storyline, poster_image, trailer_youtube):
        self.title = TVshow_title
        self.storyline = TVshow_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Function used to show the show's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
