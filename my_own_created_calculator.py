num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Module (%)")
print("6. Power (**)")
operation = input("Enter yuor choice (+, -, *, /, %, **):")
if operation == "+":
 print(f"Result: {num1} + {num2} = {nmu1 + num2}")
elif operation == "-":
 print(f"Result: {num1} - {num2} = {num1 - num2}")
elif operation == "*":
 print(f"Result: {num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 == 0:
        print("Error! cannot divide by zero.")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
elif operation == "%":
 print(f"Result: {num1} % {num2} = {num1 % num2}")
elif operation == "**":
 print(f"Result: {num1} ** {num2} == {num1 ** num2}")
else:
 print("Invalid operation! Please enter +, -, *, /, %, or **")
 
        
