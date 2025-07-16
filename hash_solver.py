# hash_solver.py

import hashlib
import time
import os

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[0m"

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

        print(f"{C}🔎 Trying: {guess}{W}")
        if h == target_hash:
            return guess
        time.sleep(0.1)
    return None

print(f"\n{C}🔐 HCO Hash Solver{W}")
target_hash = input(f"{Y}Enter hash (MD5 or SHA1): {W}").strip()

mode = "md5" if len(target_hash) == 32 else "sha1"
print(f"{C}🧠 Assuming hash type: {mode.upper()}{W}")

info = load_user_inputs()
if not info:
    print(f"{R}⚠️ No user info found in user_inputs.txt{W}")
    input(f"{Y}Press Enter to return to menu...{W}")
    exit()

guesses = generate_guesses(info)
print(f"\n{Y}🔁 Total guesses to try: {len(guesses)}{W}\n")

matched = hash_match(target_hash, guesses, mode)

if matched:
    print(f"\n{G}✅ Hash cracked! 🔓 Password is: {matched}{W}")
else:
    print(f"\n{R}❌ No match found.{W}")

input(f"\n{Y}Press Enter to return to menu...{W}")
