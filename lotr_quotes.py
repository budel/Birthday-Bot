import os
import requests
import random
from dotenv import load_dotenv


# Function to get character name by ID
def get_character_name(character_id, headers):
    character_url = f"https://the-one-api.dev/v2/character/{character_id}"
    response = requests.get(character_url, headers=headers)
    if response.status_code == 200:
        character_data = response.json()
        if character_data.get("docs"):
            return character_data["docs"][0].get("name", "Unknown Character")
        return "Unknown Character"


def get_lotr_quote():
    load_dotenv()
    token = os.getenv("LOTR_TOKEN")
    url = "https://the-one-api.dev/v2/quote"
    headers = {"Authorization": f"Bearer {token}"}
    all_quotes = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        params = {"page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            all_quotes.extend(data.get("docs", []))
            total_pages = data.get("pages", 1)
            page += 1
        else:
            raise RuntimeError(f"Error: {response.status_code}, {response.text}")
        if all_quotes:
            random_quote = random.choice(all_quotes)
            character_name = get_character_name(random_quote["character"], headers)
            return {
                "quote": random_quote["dialog"],
                "author": character_name,
                "url": "https://the-one-api.dev",
            }
        else:
            raise RuntimeError(f"Error: No quotes available.")
