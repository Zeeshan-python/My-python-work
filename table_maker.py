print("=== MULTIPLICATION  TABLE MAKER ===")
while True:
    number = int(input("Enter a number (or 0 or quit) "))
    if number == 0:
        print("Goodbye! Thanks for using this program.")
        break
    else:
        print(f"--- Table of {number} ---")
        for i in range(1, 11):
            print(f"{number} * {i} = {number * i}")
        print("------------------------")
