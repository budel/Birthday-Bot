import csv
from datetime import datetime, timedelta
import os
import requests
from dotenv import load_dotenv

from asozial_quotes import get_asozial_quote
from lotr_quotes import get_lotr_quote


def main():
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
            if (
                birthday.month == current_date.month
                and birthday.day == current_date.day
            ):
                try:
                    quote = get_asozial_quote()
                    print(quote)
                    send_greetings(row["name"], quote)
                except Exception as e:
                    print(e.args)
                    try:
                        quote = get_lotr_quote()
                        print(quote)
                        send_greetings(row["name"], quote)
                    except Exception as e:
                        print(e.args)


def send_greetings(name: str, quote: dict):
    load_dotenv()
    os.getenv("WEBHOOK")
    print(f"Happy Birthday, {name}!")
    print(f"{quote['quote']} - {quote['author']}")
    print(quote["url"])


if __name__ == "__main__":
    main()
