import random
print("=== NUMBER GUESSING GAME ===")
print("I am thinking a number between 1 and 100.")
secret_number = random.randint(1, 100)
while True:
   guess = int(input("\nEnter your guess: "))
   if guess < secret_number:
       print("Too low! try again.")
   elif guess > secret_number:
       print("Too high! try again.")
   else:
       print("Correct! You guessed the number!")
       break
