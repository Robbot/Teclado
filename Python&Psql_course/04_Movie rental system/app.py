from movie import Movie
from user import User

user = User("Jose")
# my_movie = Movie("The Matrix", "Sci-Fi", True)
#
# user.movies.append(my_movie)
#
# print(user)
# print(user.movies)
# print(user.watched_movies())
# user.delete_movie("The Matrix")
# print(user.movies)
user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")
user.save_to_file()