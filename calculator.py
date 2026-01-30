import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)

def power(a, b):
    return a ** b

def calculator():
    print("=== Welcome to Python CLI Calculator ===")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Power (a^b)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in [str(i) for i in range(1, 8)]:
            print("Invalid choice. Try again.")
            continue

        try:
            if choice in ['1', '2', '3', '4', '7']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            else:
                num1 = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square(num1))
        elif choice == '6':
            print("Result:", square_root(num1))
        elif choice == '7':
            print("Result:", power(num1, num2))

if __name__ == "__main__":
    calculator()
