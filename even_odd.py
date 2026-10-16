num = int(input("Enter a number:" ))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print("f{num} is an odd number.")

print("\nEven numbers from 2 to 20:")
for i in range(2, 20, 2):
    print(i)
