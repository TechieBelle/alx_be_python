# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle the number of rows
while row < size:
    # For loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after a row is complete
    print()
    row += 1
