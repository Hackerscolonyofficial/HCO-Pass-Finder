# hash_solver.py

import hashlib
import time
import os

def load_user_inputs(file_path="user_inputs.txt"):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        lines = f.readlines()

    values = []
    for line in lines:
        parts = line.strip().split(":")
        if len(parts) == 2:
            values.append(parts[1].strip())
    return values

def generate_guesses(info_list):
    guesses = []
    for word in info_list:
        guesses.extend([
            word,
            word + "123",
            word + "@123",
            word + "2024",
            word.capitalize(),
            word[::-1],
            word + word
        ])
    return list(set(guesses))

def hash_match(target_hash, guesses, mode="md5"):
    for guess in guesses:
        if mode == "md5":
            h = hashlib.md5(guess.encode()).hexdigest()
        elif mode == "sha1":
            h = hashlib.sha1(guess.encode()).hexdigest()
        else:
            continue

        print(f"🔎 Trying: {guess}")
        if h == target_hash:
            return guess
        time.sleep(0.1)
    return None

# Main Execution
print("\n🔐 HCO Hash Solver")
target_hash = input("Enter hash (MD5 or SHA1): ").strip()

mode = "md5" if len(target_hash) == 32 else "sha1"
print(f"🧠 Assuming hash type: {mode.upper()}")

info = load_user_inputs()
if not info:
    print("⚠️ No user info found in user_inputs.txt")
    input("Press Enter to return to menu...")
    exit()

guesses = generate_guesses(info)
print(f"\n🔁 Total guesses to try: {len(guesses)}\n")

matched = hash_match(target_hash, guesses, mode)

if matched:
    print(f"\n✅ Hash cracked! 🔓 Password is: {matched}")
else:
    print("\n❌ No match found.")

input("\nPress Enter to return to menu...")
