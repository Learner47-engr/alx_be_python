from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_current_date}")

def calculate_future_date():
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        current_date_only = datetime.now().date()
        future_date = current_date_only + timedelta(days=num_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date ({num_days} days from now): {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()