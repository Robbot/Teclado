import random

minimum = 100
for index in range(10):
    random_number = random.randint(0,100)
    print(f"The number generated is {random_number}")
    if random_number <= minimum:
        minimum = random_number
        print("This is current minimum")
    else:
        print(f"The random number {random_number} generated is higher than a {minimum}")