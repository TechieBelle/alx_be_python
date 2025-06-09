#Create a Python script named temp_conversion_tool.py.
# This script will define functions to convert temperatures between Celsius and Fahrenheit,
# demonstrating the use of global variables to store conversion factors that are accessible within functions.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp}°C")



def convert_to_fahrenheit(celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celsius}°C is {temp}°F")

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if unit == 'C':
    convert_to_fahrenheit(temperature)


elif unit == 'F':
    convert_to_celsius(temperature)

else:
    print("Invalid unit. Please enter 'C' or 'F'.")

# Global conversion factors
# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
#
# # Function to convert Fahrenheit to Celsius
# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
#
# # Function to convert Celsius to Fahrenheit
# def convert_to_fahrenheit(celsius):
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
#
# def main():
#     try:
#         # Get temperature input from the user
#         temperature = float(input("Enter the temperature to convert: "))
#         unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
#
#         if unit == 'C':
#             result = convert_to_fahrenheit(temperature)
#             print(f"{temperature}°C is {result}°F")
#         elif unit == 'F':
#             result = convert_to_celsius(temperature)
#             print(f"{temperature}°F is {result}°C")
#         else:
#             raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
#
#     except ValueError as ve:
#         print("Error:", ve)
#     except Exception:
#         print("Invalid temperature. Please enter a numeric value.")
#
# # Run the program
# if __name__ == "__main__":
#     main()

