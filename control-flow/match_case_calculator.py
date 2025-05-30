num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")


match operator:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case '/':
        if num1 or num2 == 0:
            print("cannot divide by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("invalid operator")