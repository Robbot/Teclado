class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def from_json(cls,json_data):
        return Movie(name = json_data['name'], gnre = json_data['genre'], watched = json_data['watched'])
    #or instead the above you can do just:
    #    return Movie(**json_data)