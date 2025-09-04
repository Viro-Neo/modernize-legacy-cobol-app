# operations.py
from data import read_balance, write_balance

def view_balance():
    balance = read_balance()
    print(f"Current balance: {balance:.2f}")

def credit_account():
    try:
        amount = float(input("Enter credit amount: "))
        balance = read_balance()
        new_balance = balance + abs(amount)
        write_balance(new_balance)
        print(f"Amount credited. New balance: {new_balance:.2f}")
    except ValueError:
        print("Invalid amount entered.")

def debit_account():
    try:
        amount = float(input("Enter debit amount: "))
        balance = read_balance()
        if amount > balance:
            print("Insufficient funds for this debit.")
            return
        new_balance = balance - abs(amount)
        write_balance(new_balance)
        print(f"Amount debited. New balance: {new_balance:.2f}")
    except ValueError:
        print("Invalid amount entered.")