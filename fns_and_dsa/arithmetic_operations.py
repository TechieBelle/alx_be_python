
# This function performs  basic arithmetic operations
print("Arithmetic Operations")
#Receiving users input
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero."
        case _:
            return "Invalid operation."



# Output
result = perform_operation(num1, num2, operation)
print("Result:", result)


