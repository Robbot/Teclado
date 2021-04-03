import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
chances = 3
for attempt in range(chances):
    print(f"This is attempt {attempt}")
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got the magic number right!")
    else:
        print("You didn't quite get it.")