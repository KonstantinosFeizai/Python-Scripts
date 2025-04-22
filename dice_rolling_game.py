# This program simulates a simple dice rolling game.
# if user enters y
#   Generate two random numbers between 1 and 6
#   Print them
# if user enters n
#  Print thank you message
#  Terminate the program
# Else
#  Print invalid input message

import random

while True:
    choice = input('Roll the dice? (y/n): ')
    if choice.lower() == 'y':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f'You rolled a {num1} and a {num2}.')
    elif choice.lower() == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid input. Please enter y or n.')