from wallet import Wallet

class User:
    def __init__(self, name, upi_id, pin, balance=0.0):
        self.name = name
        self.upi_id = upi_id
        self.pin = pin
        self.wallet = Wallet(upi_id, name, balance)

    def check_pin(self, pin):
        return self.pin == pin
