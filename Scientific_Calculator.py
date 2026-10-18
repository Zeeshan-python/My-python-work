import math

def show_menu():
    print("\n=== SCIENTIFIC CALCULATOR ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Log base 10 (log)")
    print("11. Natural Log (ln)")
    print("12. Factorial (!)")
    print("13. Value of Pi (π)")
    print("14. Value of e")
    print("0. Exit")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (0-14): ")

    if choice == "0":
        print("Goodbye!")
        break
        
    elif choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2}")
                
    elif choice == "5": # Square Root
        num = float(input("Enter a number: "))
        if num < 0:
            print("Error! Cannot take square root of a negative number.")
        else:
            print(f"Result: {math.sqrt(num)}")
            
    elif choice == "6": # Power
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        print(f"Result: {base ** exponent}")
        
    elif choice in ["7", "8", "9"]: # Trig functions
        angle = float(input("Enter angle in degrees: "))
        # IMPORTANT: Python math uses radians, so we convert degrees to radians!
        rad = math.radians(angle) 
        
        if choice == "7":
            print(f"Result: {math.sin(rad)}")
        elif choice == "8":
            print(f"Result: {math.cos(rad)}")
        elif choice == "9":
            print(f"Result: {math.tan(rad)}")
            
    elif choice == "10": # Log base 10
        num = float(input("Enter a number: "))
        if num <= 0:
            print("Error! Log is only for positive numbers.")
        else:
            print(f"Result: {math.log10(num)}")
            
    elif choice == "11": # Natural Log (ln)
        num = float(input("Enter a number: "))
        if num <= 0:
            print("Error! Log is only for positive numbers.")
        else:
            print(f"Result: {math.log(num)}")
            
    elif choice == "12": # Factorial
        num = int(input("Enter a whole number: "))
        if num < 0:
            print("Error! Factorial is not for negative numbers.")
        else:
            print(f"Result: {math.factorial(num)}")
            
    elif choice == "13":
        print(f"Result: {math.pi}")
        
    elif choice == "14":
        print(f"Result: {math.e}")
        
    else:
        print("Invalid choice! Please enter a number from 0 to 14.")










        
