import random

def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    print(f"The drawing gives the following results{lottery_numbers}")
    matched_numbers = user_numbers.intersection(lottery_numbers)
    if matched_numbers == 0:
        print("You didn't win at this time")
    else:
        print(f"You matched {matched_numbers}.You won ${100**len(matched_numbers)}!")


# User can pick 6 numbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers from 1 to 20, separated by commas: ")
    #Now, I want to create a set of integers from this number_cs
    number_list =  number_csv.split(",") # ['1','2','3']
    integer_set = {int(number) for number in number_list}
    return integer_set
# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values
menu()