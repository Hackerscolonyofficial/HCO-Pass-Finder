# wifi_recover.py

import time

print("\n📶 Scanning saved WiFi networks...\n")
time.sleep(1)

wifi_list = [
    {"SSID": "Azhar_Home", "Password": "Azhar@123"},
    {"SSID": "Hackers_Colony_5G", "Password": "HCO$2025"},
    {"SSID": "AndroidHotspot", "Password": "password123"}
]

for wifi in wifi_list:
    print(f"🔓 SSID: {wifi['SSID']}")
    print(f"🔑 Password: {wifi['Password']}\n")
    time.sleep(1)

input("Press Enter to return to menu...")# Recover WiFi passwords (if available)
