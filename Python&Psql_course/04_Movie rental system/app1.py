from movie import Movie
from user import User
import json


# my_movie = Movie("The Matrix", "Sci-Fi", True)
#
# user.movies.append(my_movie)
#
# print(user)
# print(user.movies)
# print(user.watched_movies())
# user.delete_movie("The Matrix")
# print(user.movies)
# user.add_movie("The Matrix", "Sci-Fi")
# user.add_movie("The Interview", "Comedy")
# user.save_to_file()
# user = User.load_from_file('Jose.txt')

# print(user.name)
# print(user.movies)
user = User("Jose")


user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")

with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)