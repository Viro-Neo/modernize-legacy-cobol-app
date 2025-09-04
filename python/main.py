# main.py
from operations import view_balance, credit_account, debit_account

def display_menu():
    print("1. View Balance")
    print("2. Credit Account")
    print("3. Debit Account")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): \n").strip()
        if choice == "1":
            view_balance()
        elif choice == "2":
            credit_account()
        elif choice == "3":
            debit_account()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()