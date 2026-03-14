import requests
import time

BLACKLISTED_QUOTE_IDS = [34, 39, 41, 58, 64, 67, 68, 72, 80, 100, 109, 111, 113, 122, 129, 133, 145, 149, 211, 214, 229, 230, 233, 238, 241, 245, 249, 250, 260, 313, 392, 472, 519, 575, 578, 611, 612, 620, 640, 656, 658, 667, 677, 709, 711, 724, 733, 738, 754, 757, 762, 763, 766, 776, 788, 790, 791, 808, 812, 828, 836, 853, 860, 863, 866, 873, 885, 886, 887, 888, 889, 917, 933, 935, 945, 955, 959, 962, 969, 974, 975, 982, 984, 990, 1001, 1010, 1011, 1012, 1017, 1027, 1028, 1029, 1034, 1038, 1048, 1083, 1088, 1106, 1110, 1111, 1112, 1117, 1118, 1127, 1128, 1131, 1132, 1138, 1150, 1152, 1156, 1161, 1172, 1193, 1198, 1199, 1208, 1220, 1225, 1230, 1233, 1239, 1241, 1245, 1260, 1261, 1268, 1269, 1287, 1288, 1290, 1302, 1304, 1312, 1313, 1314, 1328, 1329, 1331, 1332, 1374, 1382, 1389, 1393, 1410, 1412, 1416, 1430, 1431, 1432, 1433, 1434, 1441, 1446, 1448, 1454, 1459, 1465, 1466, 1474, 1480, 1481, 1483, 1487, 1491, 1499, 1506, 1507, 1517, 1521, 1533, 1540, 1559 ]
BLACKLISTED_AUTHOR_IDS = [218, 229, 733, 836, 846, 1377, 1408, 1545, 1788, 1795]

def get_asozial_quote():
    quote = get_wrong_quote()
    if quote["quote"]["id"] in BLACKLISTED_QUOTE_IDS or quote["quote"]["author"]["id"] in BLACKLISTED_AUTHOR_IDS:
        time.sleep(1)
        return get_asozial_quote()
    return quote

def get_wrong_quote():
    response = requests.get("https://zitate.prapsschnalinen.de/api/wrongquotes/random?min_rating=0")
    if response.status_code == 200:
        quote = response.json()[0]
        quote["url"] = f"https://zitate.prapsschnalinen.de/{quote['id']}"
        return quote
    else:
        raise RuntimeError(f"Error: {response.status_code}, {response.text}")