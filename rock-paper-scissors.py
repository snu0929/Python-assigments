import random

def get_user_choice():
    # Function to get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors) or 'q' to quit: ").lower()
    return user_choice

def get_computer_choice():
    # Function to get the computer's random choice
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner based on the rules
    if user_choice == computer_choice:
        return 'draw'
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
         user_choice == 'scissors' and computer_choice == 'paper' or \
         user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    draw_count = 0

    while True:
        user_choice = get_user_choice()

        if user_choice == 'q':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose from 'rock', 'paper', 'scissors', or 'q' to quit.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            user_score += 1
            print(f"You win! You chose {user_choice}, and the computer chose {computer_choice}.")
        elif winner == 'computer':
            computer_score += 1
            print(f"You lose! You chose {user_choice}, and the computer chose {computer_choice}.")
        else:
            draw_count += 1
            print(f"It's a draw! Both you and the computer chose {user_choice}.")

        print(f"Score - User: {user_score}, Computer: {computer_score}, Draws: {draw_count}\n")

    print("Thanks for playing!")

rock_paper_scissors_game()
