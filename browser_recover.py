# browser_recover.py

import time
import random

print("\n🧠 HCO Browser Password Recovery")
print("🔍 Scanning 'LoginData' (simulated)...\n")
time.sleep(1.5)

# Simulated password entries
entries = [
    {"site": "facebook.com", "username": "azhar@hco.com", "password": "Azhar@123"},
    {"site": "instagram.com", "username": "azhar_colony", "password": "HCOrocks2025"},
    {"site": "gmail.com", "username": "azharhco@gmail.com", "password": "azhar321"},
    {"site": "youtube.com", "username": "HackersColonyYT", "password": "H@cking123"},
]

for entry in entries:
    print(f"🌐 Site     : {entry['site']}")
    print(f"👤 Username : {entry['username']}")
    print(f"🔑 Password : {entry['password']}")
    print("-" * 35)
    time.sleep(random.uniform(0.8, 1.2))

print("\n✅ Simulated browser recovery complete.")
input("\nPress Enter to return to menu...")
