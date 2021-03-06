from user import User
import json
import os


with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = User.from_json(json_data)

    print(user.json())


def menu():
    name = input("Enter user name: ")
    filename = "{}.txt".format(name)
    if file_exixts(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)


    user_input = input("Enter 'a' to add movie, 's' to list movies,"
        "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies"
        "or 'q' to to and quit")
    while user_input !='q':
        if user_input == 'a':
            movie_name = input("Enter the move name: ")
            movie_genre =  input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched)
        elif user_input == 'f':
                user.filnename =  user.json()
                with open(filename, 'w') as f:
                    json.dump(user.json(), f)


    def file_exists(filename):
    return os.path.isfile(filename)


menu()