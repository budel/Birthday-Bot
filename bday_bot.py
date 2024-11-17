import csv
from datetime import datetime, timedelta

# Load the CSV file
with open("birthdays.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    # Get current date
    current_date = datetime.now()

    # Iterate over each row in the CSV
    for row in csv_reader:
        # Assuming the CSV has columns named 'name' and 'birthday' in the format 'MM-DD'
        birthday = datetime.strptime(row["birthday"], "%d.%m.")

        # Check if today is the birthday
        if birthday.month == current_date.month and birthday.day == current_date.day:
            print(f"Happy Birthday, {row['name']}!")
