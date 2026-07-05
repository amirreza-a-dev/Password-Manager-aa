import os
import json
from pathlib import Path

VAULT_PATH = Path(__file__).parent / "vault.json"

if  not VAULT_PATH.exists():
    with open(VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)
with open(VAULT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def main():
    while True:
        print("------------^------------")
        print("     1. Add Password")
        print("     2. Search Password")
        print("     3. Exit")
        print("------------=------------")
        choice = input("Enter your choice: ")
        clear()
        if choice=="1":
            website = input("Website / Application: ")
            username = input("Username: ")
            password = input("Password: ")
            d = {
                "Website" : website,
                "Username" : username,
                "Password" : password
            }
            data.append(d)
            with open(VAULT_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("Password saved successfully.")
            input("Press Enter to continue...")
            clear()
        elif choice=="2":
            print("Working...")
            input("Press Enter to continue...")
            clear()
        elif choice=="3":
            break
        else: print("Invalid input!\nTry again.")


if __name__ == "__main__":
    main()
