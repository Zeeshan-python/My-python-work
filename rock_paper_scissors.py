import random
print("=== ROCK, PAPER, SCISSORS ===")
user_score = 0
computer_score = 0
while True:
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("\nEnter rock, paper, scissors (or 'quit' to stop): ").lower()
    if user_choice == "quit":
        print("\n--- FINAL SCORE ---")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thank you for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice! Please type rock, paper, or scissors.")
        continue
    print(f"Computer chose: {computer_choice.upper()}")
    print(f"--- SCORE: You {user_score} | Computer {computer_score} ---")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score = user_score + 1
    else:
        print("You lose!")
        computer_score = computer_score + 1
  
        
