# browser_recover.py

import time
import random

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[0m"

print(f"\n{C}🧠 HCO Browser Password Recovery{W}")
print(f"{Y}🔍 Scanning 'LoginData' (simulated)...{W}\n")
time.sleep(1.5)

entries = [
    {"site": "facebook.com", "username": "azhar@hco.com", "password": "Azhar@123"},
    {"site": "instagram.com", "username": "azhar_colony", "password": "HCOrocks2025"},
    {"site": "gmail.com", "username": "azharhco@gmail.com", "password": "azhar321"},
    {"site": "youtube.com", "username": "HackersColonyYT", "password": "H@cking123"},
]

for entry in entries:
    print(f"{G}🌐 Site     : {entry['site']}{W}")
    print(f"{C}👤 Username : {entry['username']}{W}")
    print(f"{Y}🔑 Password : {entry['password']}{W}")
    print(f"{R}" + "-" * 35 + f"{W}")
    time.sleep(random.uniform(0.8, 1.2))

print(f"\n{G}✅ Simulated browser recovery complete.{W}")
input(f"\n{Y}Press Enter to return to menu...{W}")
