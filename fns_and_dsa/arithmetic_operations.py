
# This function performs  basic arithmetic operations
print("Arithmetic Operations")
#Receiving users input
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation."


# Output
result = perform_operation(num1, num2, operation)
print("Result:", result)


