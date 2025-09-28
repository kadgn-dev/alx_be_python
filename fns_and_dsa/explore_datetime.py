from datetime import datetime, timedelta


def display_current_datetime():
    # Save the current datetime
    current_date = datetime.now()
    # Format the datetime in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(days):
    # Calculate future date by adding timedelta
    future_date = datetime.now() + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date


def main():
    # Part 1: show current date and time
    display_current_datetime()

    # Part 2: ask user for days and compute future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer for days.")


if __name__ == "__main__":
    main()
