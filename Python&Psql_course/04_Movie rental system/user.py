from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda x: x.name != name, self.movies))
        """The above iterates a list of movies and if the movie name is not equal it keeps the movie, but it is match the name it deletes
        from the list"""


    def set_watched(self):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def watched_movies(self):
        return list(filter(lambda x: x.watched, self.movies))


    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies =[]
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user







