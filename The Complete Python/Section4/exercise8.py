# Define a Movie class that has two properties: name and director
class Movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director


# You should be able to create Movie objects like this one:
my_movie = Movie('The Matrix', 'Wachowski brothers')

print(f"My favourite movie is {my_movie.name} which was directed by {my_movie.director}.")
