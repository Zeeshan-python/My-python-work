all_questions = [
  ["What is 15+5?", "10", "20", "15", "25", "b"],
    ["Which one is the largest country in the world", "America", "Russia",   "India", "Pakistan", "b"],
  ["who was the fastest bowler in cricket history", "Bretlee", "Starc", "Shoib Akhtar", "Shaheen", "c"]
]
for question in all_questions:
    print("\nQuestion:", question[0])
    print("a.", question[1])
    print("b.", question[2])
    print("c.", question[3])
    print("d.", question[4])
    user_answer = input("Enter your answer (a/b/c/d): ")
    if user_answer == question[5]:
        print("Correct! you move the next question.")
    else:
        print(f"Wrong! correct answer was {question[5]}. Game over.")
        break
print("\nGame over! Thanks for playing.")
