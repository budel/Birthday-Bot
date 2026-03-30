import requests
import time

BLACKLISTED_QUOTE_IDS = [58, 67, 72, 109, 122, 211, 229, 230, 233, 245, 250, 260, 313, 392, 472, 575, 578, 611, 612, 709, 738, 754, 757, 776, 788, 812, 828, 860, 866, 873, 917, 955, 959, 975, 984, 1011, 1017, 1027, 1048, 1083, 1106, 1110, 1111, 1112, 1117, 1127, 1132, 1150, 1161, 1172, 1193, 1199, 1220, 1230, 1233, 1239, 1241, 1245, 1260, 1261, 1268, 1269, 1287, 1288, 1313, 1314, 1328, 1329, 1331, 1332, 1374, 1382, 1389, 1393, 1410, 1412, 1416, 1430, 1431, 1432, 1433, 1434, 1446, 1448, 1459, 1465, 1466, 1474, 1480, 1481, 1483, 1491, 1506, 1517, 1521, 1533 ]
BLACKLISTED_AUTHOR_IDS = [218, 229, 307, 733, 836, 846, 1377, 1408, 1545, 1788, 1795]

def get_asozial_quote():
    q = get_wrong_quote()
    if q["quote"]["id"] in BLACKLISTED_QUOTE_IDS or q["quote"]["author"]["id"] in BLACKLISTED_AUTHOR_IDS:
        time.sleep(1)
        return get_asozial_quote()
    return {
        'quote': q['quote']['quote'],
        'author': q['author']['author'],
        'url': f"https://zitate.prapsschnalinen.de/{q['id']}"        
    }

def get_wrong_quote():
    response = requests.get("https://zitate.prapsschnalinen.de/api/wrongquotes/random?min_rating=1")
    if response.status_code == 200:
        quote = response.json()[0]
        return quote
    else:
        raise RuntimeError(f"Error: {response.status_code}, {response.text}")