import os

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
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            print("Password saved successfully.")
            input("Press Enter to continue...")
            clear()
        elif choice=="2":
            website = input("Website: ")
            username = input("Username: ")
            clear()
        elif choice=="3":
            break
        else: print("Invalid input!\nTry again.")

if __name__ == "__main__":
    main()
