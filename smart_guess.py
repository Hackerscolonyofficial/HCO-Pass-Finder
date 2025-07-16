# smart_guess.py

import time

def generate_guesses(name, dob, phone, email):
    guesses = []

    dob_parts = dob.split("-")  # Format: DD-MM-YYYY
    day, month, year = dob_parts if len(dob_parts) == 3 else ("", "", "")

    guesses.extend([
        name + "123",
        name + "@123",
        name + day,
        name + year,
        name + phone[-4:],  # Last 4 digits
        phone,
        email.split("@")[0] + "123",
        name + month + year[-2:],
        name.capitalize() + "@" + year
    ])

    return list(set(guesses))  # Remove duplicates

# Input section
print("🧠 HCO Smart Password Guess")
print("Please enter your known details:\n")

name = input("🔤 Name        : ").strip()
dob = input("📅 DOB (DD-MM-YYYY): ").strip()
phone = input("📞 Phone No    : ").strip()
email = input("📧 Email       : ").strip()

print("\n🔍 Generating smart guesses...\n")
time.sleep(1)

guesses = generate_guesses(name, dob, phone, email)

for guess in guesses:
    print(f"🔐 {guess}")
    time.sleep(0.3)

print(f"\n✅ Total guesses generated: {len(guesses)}")
input("\nPress Enter to return to menu...")
