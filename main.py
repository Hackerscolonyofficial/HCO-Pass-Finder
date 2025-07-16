# main.py
import os

# Color codes
R = "\033[1;31m"   # Red
G = "\033[1;32m"   # Green
Y = "\033[1;33m"   # Yellow
B = "\033[1;34m"   # Blue
C = "\033[1;36m"   # Cyan
W = "\033[0m"      # Reset

def banner():
    os.system("clear")
    print(f"""{C}
╔═════════════════════════════════════════╗
║{R}     🔐 HCO-PassFinder               {C}║
║{G}   Smart Password Recovery Tool      {C}║
║{Y}   Coded by: Azhar @ Hackers Colony  {C}║
╚═════════════════════════════════════════╝{W}
""")

def main_menu():
    banner()
    print(f"""{B}
[1] {W}Recover Browser Passwords
[2] {W}Smart Password Guess
[3] {W}Crack Hash from Info
[0] {W}Exit
""")

    choice = input(f"{Y}Select an option ➤ {W}")

    if choice == "1":
        import browser_recover
    elif choice == "2":
        import smart_guess
    elif choice == "3":
        import hash_solver
    elif choice == "0":
        print(f"\n{G}Goodbye, hacker! Stay sharp. 💀{W}")
        exit()
    else:
        print(f"\n{R}⚠️ Invalid choice. Please try again.{W}")
        input(f"{C}Press Enter to continue...{W}")
        main_menu()

if __name__ == "__main__":
    main_menu()
