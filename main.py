from user import User
from storage import create_files, load_users, save_users, add_transaction, get_transactions
from transaction import make_transaction
from validation import valid_name, valid_upi, valid_pin, get_positive_amount

def find_user(users, upi_id):
    for user in users:
        if user["upi_id"] == upi_id:
            return user
    return None

def register_user():
    users = load_users()
    print("\n--- Create New Wallet ---")
    name = input("Enter your name: ").strip()
    if not valid_name(name):
        print("Name is too short.")
        return

    upi_id = input("Create your UPI ID (example: name@wallet): ").strip()
    if not valid_upi(upi_id):
        print("Invalid UPI ID.")
        return

    if find_user(users, upi_id):
        print("This UPI ID already exists.")
        return

    pin = input("Create a 4 digit PIN: ")
    if not valid_pin(pin):
        print("PIN must contain exactly 4 digits.")
        return

    users.append({"name": name, "upi_id": upi_id, "pin": pin, "balance": "0.0"})
    save_users(users)
    print("Wallet created successfully.")

def login():
    users = load_users()
    upi_id = input("Enter UPI ID: ").strip()
    pin = input("Enter PIN: ")

    user_data = find_user(users, upi_id)
    if user_data is None or user_data["pin"] != pin:
        print("Invalid UPI ID or PIN.")
        return None

    return user_data

def update_user_balance(user_data, new_balance):
    users = load_users()
    for user in users:
        if user["upi_id"] == user_data["upi_id"]:
            user["balance"] = str(new_balance)
    save_users(users)

def add_money(user_data):
    amount = get_positive_amount("Enter amount to add: ")
    balance = float(user_data["balance"]) + amount
    user_data["balance"] = str(balance)
    update_user_balance(user_data, balance)
    add_transaction("SYSTEM", user_data["upi_id"], amount, "ADD MONEY", "SUCCESS")
    print("Money added successfully.")
    print("New balance: Rs.", round(balance, 2))

def send_money(user_data):
    receiver_upi = input("Enter receiver UPI ID: ").strip()
    if receiver_upi == user_data["upi_id"]:
        print("You cannot send money to yourself.")
        return

    users = load_users()
    receiver = find_user(users, receiver_upi)
    if receiver is None:
        print("Receiver UPI ID was not found.")
        return

    amount = get_positive_amount("Enter amount to send: ")
    sender_balance = float(user_data["balance"])

    if amount > sender_balance:
        print("Insufficient balance.")
        add_transaction(user_data["upi_id"], receiver_upi, amount, "UPI TRANSFER", "FAILED")
        return

    receiver_balance = float(receiver["balance"])
    sender_balance = sender_balance - amount
    receiver_balance = receiver_balance + amount

    user_data["balance"] = str(sender_balance)
    receiver["balance"] = str(receiver_balance)
    save_users(users)

    add_transaction(user_data["upi_id"], receiver_upi, amount, "UPI TRANSFER", "SUCCESS")
    print("UPI transaction successful.")
    print("Sent Rs.", round(amount, 2), "to", receiver_upi)
    print("Remaining balance: Rs.", round(sender_balance, 2))

def show_history(user_data):
    records = get_transactions(user_data["upi_id"])
    print("\n--- Transaction History ---")
    if len(records) == 0:
        print("No transactions found.")
        return

    for record in records:
        print(record["type"], "| From:", record["from_upi"],
              "| To:", record["to_upi"], "| Rs.", record["amount"],
              "|", record["status"])

def wallet_menu(user_data):
    while True:
        print("\n--- Digital Wallet ---")
        print("1. Check Balance")
        print("2. Add Money")
        print("3. Send Money by UPI")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance: Rs.", round(float(user_data["balance"]), 2))
        elif choice == "2":
            add_money(user_data)
        elif choice == "3":
            send_money(user_data)
        elif choice == "4":
            show_history(user_data)
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Please select a valid option.")

def main():
    create_files()

    while True:
        print("\n================================")
        print(" DIGITAL WALLET & UPI SIMULATOR")
        print("================================")
        print("1. Create Wallet")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login()
            if user is not None:
                wallet_menu(user)
        elif choice == "3":
            print("Thank you for using the simulator.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
