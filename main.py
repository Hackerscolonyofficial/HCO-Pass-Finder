# main.py
import os

def banner():
    os.system("clear")
    print("""
    ╔══════════════════════════════╗
    ║     🔐 HCO-PassFinder        ║
    ║   Smart Password Recovery    ║
    ║    Coded by: Azhar 🧠        ║
    ╚══════════════════════════════╝
    """)

def main_menu():
    banner()
    print("""
    [1] Recover Browser Passwords
    [2] Smart Password Guess
    [3] Crack Hash from Info
    [4] WiFi Password Viewer
    [0] Exit
    """)

    choice = input("Select an option: ")

    if choice == "1":
        import browser_recover
    elif choice == "2":
        import smart_guess
    elif choice == "3":
        import hash_solver
    elif choice == "4":
        import wifi_recover
    elif choice == "0":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice.")
        input("Press Enter to continue...")
        main_menu()

if __name__ == "__main__":
    main_menu()
