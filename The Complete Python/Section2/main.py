# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.
# q_isnt_pressed = True
# while q_isnt_pressed:
#     user_input = input("Please enter 'p' or 'q' ")
#     if user_input == "p":
#         print("Hello")
#     elif user_input == "q":
#         q_isnt_pressed = False
#         exit()
#     else:
#         print("Only letters 'p' or 'q' are allowed")
#

# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...


# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...
#Coding exercise 5
user_input = input("Please enter 'p' or 'q' ")
while user_input == "p":
        print("Hello")
        user_input = input("Please enter 'p' or 'q' ")