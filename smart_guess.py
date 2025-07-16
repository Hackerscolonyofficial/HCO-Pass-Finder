# smart_guess.py

import time

# Color codes
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[0m"

def generate_guesses(name, dob, phone, email):
    guesses = []

    dob_parts = dob.split("-")
    day, month, year = dob_parts if len(dob_parts) == 3 else ("", "", "")

    guesses.extend([
        name + "123",
        name + "@123",
        name + day,
        name + year,
        name + phone[-4:],
        phone,
        email.split("@")[0] + "123",
        name + month + year[-2:],
        name.capitalize() + "@" + year
    ])

    return list(set(guesses))

print(f"\n{C}🧠 HCO Smart Password Guess{W}")
print(f"{Y}Please enter your known details:{W}\n")

name = input(f"{C}🔤 Name        : {W}").strip()
dob = input(f"{C}📅 DOB (DD-MM-YYYY): {W}").strip()
phone = input(f"{C}📞 Phone No    : {W}").strip()
email = input(f"{C}📧 Email       : {W}").strip()

print(f"\n{Y}🔍 Generating smart guesses...{W}\n")
time.sleep(1)

guesses = generate_guesses(name, dob, phone, email)

for guess in guesses:
    print(f"{G}🔐 {guess}{W}")
    time.sleep(0.3)

print(f"\n{C}✅ Total guesses generated: {len(guesses)}{W}")
input(f"\n{Y}Press Enter to return to menu...{W}")
