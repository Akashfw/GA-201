import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors), or 'q' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'q']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "user"
    else:
        return "computer"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            return play_again == 'yes'
        else:
            print("Invalid choice. Please try again.")

def play_game():
    user_score = 0
    computer_score = 0
    draw_count = 0
    round_count = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        print("===================================")
        print("Round:", round_count + 1)
        user_choice = get_user_choice()
        
        if user_choice == 'q':
            break

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print("You win!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            draw_count += 1
            print("It's a draw!")

        round_count += 1
        print(f"\nScore: User - {user_score} | Computer - {computer_score} | Draws - {draw_count}")

        if not play_again():
            break

    print("\nThank you for playing!")

play_game()
