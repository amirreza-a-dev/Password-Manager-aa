import os
import json
from pathlib import Path

data = None
VAULT_PATH = Path(__file__).parent / "vault.json"

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def dump_data():
    with open(VAULT_PATH, "w", encoding="utf-8",) as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    with open(VAULT_PATH, "r", encoding="utf-8") as f:
        global data
        data = json.load(f)

def pause():
    input("Press Enter to continue...")
    clear()


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
        print("     4. Update Password")
        print("     5. View Saved Accounts")
        print("     6. Exit")
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
            clear()
            print("------------------\nPassword saved successfully.\n------------------")
            pause()

        elif choice=="2":
            website = input("Website / Application: ")
            username = input("Username: ")
            for item in data:
                if item["website"] == website and item["username"] == username:
                    clear()
                    print(f'------------------\nYour password is: {item["password"]}\n------------------')
                    break
            else:
                clear()
                print("------------------\nPassword not found.\n------------------")
            pause()

        elif choice=="3":
            website = input("Website / Application: ")
            username = input("Username: ")
            for item in data:
                if item["website"] == website and item["username"] == username:
                    data.remove(item)
                    clear()
                    print("------------------\nRecord deleted successfully.\n------------------")
                    break
            else:
                clear()
                print("------------------\nRecord not found.\n------------------")
            dump_data()
            pause()

        elif choice=="4":
            website = input("Website / Application: ")
            username = input("Username: ")
            password = input("Current Password: ")
            for item in data:
                if item["website"] == website and item["username"] == username and item["password"] == password:
                    clear()
                    new_password = input("New Password: ")
                    confirm_password = input("Confirm New Password: ")
                    if new_password == confirm_password:
                        item["password"] = new_password
                        dump_data()
                        clear()
                        print("------------------\nPassword updated successfully.\n------------------")
                        break
                    else:
                        clear()
                        print("------------------\nNew passwords do not match.\nTry again.\n------------------")
                        break
            else: 
                clear()
                print("------------------\nRecord not found.\n------------------")
            pause()
        
        elif choice=="5":
            if not data:
                clear()
                print("------------------\nNo saved accounts.\n------------------")
            else:
                clear()
                print("------------------")
                for idx, item in enumerate(data, start=1):
                    print(f"{idx}.")
                    print(f"Website / Application: {item['website']}")
                    print(f"Username: {item['username']}")
                    print("------------------")
            pause()

        elif choice=="6":
            break

        else:
            print("------------------\nInvalid input.\nTry again.\n------------------")
            pause()    


if __name__ == "__main__":
    main()
