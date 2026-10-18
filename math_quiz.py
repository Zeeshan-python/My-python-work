import random
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    print(f"\nWhat is {num1} + {num2}?")
    return answer
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False
    #---Main program Starts here---
print("=== WELCOME TO THE MATH QUIZ ===")
score = 0
for i in range(3):
    correct = generate_question()
    user_input = int(input("Your answer: "))
    if check_answer(user_input, correct):
        score = score + 1
print(f"\n=== QUIZ OVER ===")
print(f"Your final score is: {score}/3")

                         
