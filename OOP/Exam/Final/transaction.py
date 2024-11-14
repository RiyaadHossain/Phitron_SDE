from datetime import datetime

class Transaction:
    def __init__(self, user, amount, transaction_type):
        self.user = user
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.now()
        # self.receiver = receiver

    def __repr__(self):
        details = f"{self.user.name} {self.transaction_type} {self.amount} at {self.date}"
        return details