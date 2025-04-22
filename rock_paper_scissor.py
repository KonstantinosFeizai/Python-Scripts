#Ask the user to make a choice
# if choice is not valid
#  Print invalid input message
# Let the computer make a choice
# print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# if not
#  terminate the program
import random
emojis = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

while True:
    user_choice= input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter rock, paper, or scissors.")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f'your choice: {emojis[user_choice]}')
    print(f"Computer chose: {emojis[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    should_continue=input("Continue playing? (y/n): ").lower()
    if should_continue== 'n':
        print("Thank you for playing!")
        break
    else:
        print("Lets play again!")
        continue