def valid_name(name):
    return len(name.strip()) >= 2

def valid_upi(upi_id):
    if "@" not in upi_id:
        return False
    parts = upi_id.split("@")
    return len(parts) == 2 and len(parts[0]) > 0 and len(parts[1]) > 0

def valid_pin(pin):
    return len(pin) == 4 and pin.isdigit()

def get_positive_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            print("Enter an amount greater than zero.")
        except ValueError:
            print("Please enter a valid number.")
