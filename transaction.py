def make_transaction(sender, receiver, amount):
    if sender == receiver:
        return False, "Sender and receiver cannot be the same."

    if amount <= 0:
        return False, "Amount must be greater than zero."

    if amount > sender.wallet.balance:
        return False, "Insufficient balance."

    sender.wallet.send_money(amount)
    receiver.wallet.add_money(amount)
    return True, "Transaction successful."
