# data.py

BALANCE_FILE = "balance.txt"

def read_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        # Create the file with a default balance
        with open(BALANCE_FILE, "w") as f:
            f.write("1000.00")
        return 1000.0
    except ValueError:
        return 0.0

def write_balance(new_balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(f"{new_balance:.2f}")