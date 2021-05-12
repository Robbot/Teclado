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

    def watched_movies(self):
        # watched_movie_list = []
        #
        # for movie in self.movies:
        #     if movie.watched:
        #         watched_movie_list.append(movie)
        #
        # return watched_movie_list
        movies_watched = list(filter(lambda x: x.watched, self.movies))  # this one line replaces the above function!
        return movies_watched

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(movie.name + "," + movie.genre + "," + str(movie.watched) + "\n")


"""The above iterates a list of movies and if the movie name is not equal it keeps the movie, but it is match the name it deletes
from the list"""

# or like this  f.write("{},{},{}\n".format(movie.name,movie.genre,str(movie.watched)))

