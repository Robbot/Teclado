# Coding exercise 2
name = input("What is your name? ")
print(f"Hello, {name}")
age = int(input("What is your age? "))
print(f"You are {age*12} months old")

# Coding exercise 3
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set() #This is an empty set
friend = input("What is the name of your friend? ")
user_friends.add(friend)
print(nearby_people.intersection(user_friends))

#Coding exercise 4
lottery_numbers = {13, 21, 22, 5, 8}
"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {
        'name': 'Rob',
        'numbers': {5,6,10,12,21,22}
    },
    {
        'name': 'Rolf',
        'numbers': {5,10,13,21,22,48}
    }
]
"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
won1 = (len((players[0]['numbers']).intersection(lottery_numbers)))
print(f"Player {players[0]['name']} got {won1} numbers right. ")
won2 = (len((players[1]['numbers']).intersection(lottery_numbers)))
print(f"Player {players[1]['name']} got {won2} numbers right. ")