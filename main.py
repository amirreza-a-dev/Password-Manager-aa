import os
import json
from pathlib import Path

data = None
def clear():
    os.system("cls" if os.name=="nt" else "clear")

def dump_data():
    with open(VAULT_PATH, "w", encoding="utf-8",) as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        global data
        data = json.load(f)

VAULT_PATH = Path(__file__).parent / "vault.json"

if not VAULT_PATH.exists():
    with open(VAULT_PATH, "w", encoding="utf-8",) as f:
        json.dump([], f)
load_data()

def main():
    while True:
        print("------------^------------")
        print("     1. Add Password")
        print("     2. Search Password")
        print("     3. Delete Password")
        print("     4. Exit")
        print("------------=------------")
        choice = input("Enter your choice: ")
        clear()
        if choice=="1":
            website = input("Website / Application: ")
            username = input("Username: ")
            password = input("Password: ")
            d = {
                "website" : website,
                "username" : username,
                "password" : password
            }
            data.append(d)
            dump_data()
            print("------------------\nPassword saved successfully.\n------------------")
            input("Press Enter to continue...")
            clear()

        elif choice=="2":
            website = input("Website / Application: ")
            username = input("Username: ")
            for item in data:
                if item["website"] == website and item["username"] == username:
                    print(f'------------------\nYour password is: {item["password"]}\n------------------')
                    break
            else:
                print("------------------\nPassword not found...\n------------------")
            input("Press Enter to continue...")
            clear()

        elif choice=="3":
            website = input("Website / Application: ")
            username = input("Username: ")
            for item in data:
                if item["website"] == website and item["username"] == username:
                    data.remove(item)
                    print("------------------\nRecord deleted successfully.\n------------------")
                    break
            else:
                print("------------------\nRecord not found...\n------------------")
            dump_data()
            input("Press Enter to continue...")
            clear()

        elif choice=="4":
            break

        else:
            print("Invalid input!\nTry again.")
            input("Press Enter to continue...")
            clear()     


if __name__ == "__main__":
    main()
