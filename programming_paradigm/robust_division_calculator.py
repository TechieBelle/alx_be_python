def safe_divide(numerator, denominator):
    try:
        result =  numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")



