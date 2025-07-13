import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score
    
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

def game():
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        play_round()
        print(f"Score ➤ You: {user_score} | Computer: {computer_score}")
        
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing!")
            break
game()
