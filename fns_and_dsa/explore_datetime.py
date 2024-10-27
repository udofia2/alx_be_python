from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """Calculates and displays a future date based on the given number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")


def main():
    display_current_datetime()
    
    while True:
        try:
            days = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    calculate_future_date(days)


if __name__ == "__main__":
    main()