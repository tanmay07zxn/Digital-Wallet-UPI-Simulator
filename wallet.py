class Wallet:
    def __init__(Self, Upi_id, Name, balance=0.0):
        Self.Upi_id = Upi_id
        Self.Name = name
        Self.balance = float(balance)

    def add_money(Self, amount):
        if amount <= 0:
            return False
        Self.balance = Self.balance + amount
        return True

    def send_money(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True
