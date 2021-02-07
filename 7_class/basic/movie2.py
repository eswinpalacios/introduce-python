class Movie:
    title = ""
    duration = 0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Title: {}".format(self.title))


movie = Movie("Avengers", 120)
movie.show_info()
