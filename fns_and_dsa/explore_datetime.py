
from datetime import datetime, timedelta

from sqlalchemy.sql.functions import current_date


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time:{current_date}")

#call function
display_current_datetime()
print()

#Part 2: Calculate a Future Date
def calculate_future_date():
    # Ask the user for number of days
    duration = int(input("Enter the number of days to add to the current date: "))

    # Get today's date and time
    current_date = datetime.now()

    # Calculate future date
    future_date = current_date + timedelta(days = duration)

    print("Future date:", future_date.strftime("%Y-%m-%d"))


#call function
calculate_future_date()



