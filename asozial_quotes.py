import requests

def get_asozial_quote():
    response = requests.get("https://asozial.org/api/zitate")
    if response.status_code == 200:
        quote = response.json()
        quote["url"] = f"https://asozial.org/api/zitate/{quote['id']}"
        return quote
    else:
        raise RuntimeError(f"Error: {response.status_code}, {response.text}")