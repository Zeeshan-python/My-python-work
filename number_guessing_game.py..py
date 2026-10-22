import random
lives = 5
print("=== NUMBER GUESSUNG GAME ===")
print("I am thinking a number between 1 and 100.")

secret_number = random.randint(1, 100)
while True:
   guess = int(input("\nEnter your guess: "))
   if guess == secret_number:
       print("Correct! You guessed the number!")
       break
   else: 
       lives = lives - 1
       print(f"Wrong guess! you have {lives} lives left.")
   if guess < secret_number:
       print("(Hint: the number is higher than that.")
   else:
       print("(Hint: the number is lower than that.")
   if lives == 0:
       print("\nGame over! You ran out of lives.")
       print(f"The secret number was {secret_number}.")
       break # 1. Tuple (Fixed info)
