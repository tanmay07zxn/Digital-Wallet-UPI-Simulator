import csv
import os

USER_FILE = "data/users.csv"
TRANSACTION_FILE = "data/transactions.csv"

def create_files():
    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "upi_id", "pin", "balance"])

    if not os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["from_upi", "to_upi", "amount", "type", "status"])

def load_users():
    users = []
    with open(USER_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def save_users(users):
    with open(USER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "upi_id", "pin", "balance"])
        for user in users:
            writer.writerow([user["name"], user["upi_id"], user["pin"], user["balance"]])

def add_transaction(from_upi, to_upi, amount, transaction_type, status):
    with open(TRANSACTION_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([from_upi, to_upi, amount, transaction_type, status])

def get_transactions(upi_id):
    result = []
    with open(TRANSACTION_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["from_upi"] == upi_id or row["to_upi"] == upi_id:
                result.append(row)
    return result
