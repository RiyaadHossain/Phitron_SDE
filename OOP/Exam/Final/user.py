from transaction import Transaction

class User:
    def __init__(self, name, email, address, account_type,bank):
        self.name = name 
        self.email = email 
        self.address= address
        self.account_type = account_type 
        self.account_id = bank.generate_account_id()
        self.transactions = []
        self.balance = 0
        self.loan_balance = 0
        self.loan_taken = 0
        bank.user_accounts.append(self)

    def amount_validity(self, amount, check_curr_balance):
        if amount < 0:
            print("Amount can't be negative")
            return False
        
        if check_curr_balance and (amount > self.balance and amount > self.loan_balance):
            print("Don't have sufficient balance")
            return False
        
        return True
    
    def update_balance(self, amount):
        print(type(amount))
        if  self.balance > amount:
            self.balance -= amount
        else:
            self.loan_balance -= amount

    def deposit(self, amount, bank):
        if self.amount_validity( amount, False) is False:
            return
        
        self.balance += amount
        bank.capital += amount
        self.transactions.append(Transaction(self, amount, 'deposit'))
        print(f"Amount {amount} deposited successfully")
    
    def withdraw(self, amount,bank):
        if self.amount_validity( amount, True) is False:
            return
        
        if bank.capital < amount:
            return print(f"Bank '{bank.name}' is bankrupt")
        
        self.update_balance(amount)
        self.transactions.append(Transaction(self, amount, 'withdraw'))
        print(f"Amount {amount} withdrew successfully")

    def check_balance(self):
        print(f"Current Balance: {self.balance} Loan Balance: {self.loan_balance}")

    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, bank, amount):
        if self.amount_validity( amount, False) is False:
            return

        if bank.loan_feature is False:
            return print(f"Currently, Bank '{bank.name}' loan feature is off!")
        
        if bank.capital < amount:
            return print(f"Bank '{bank.name}' is going to be bankruptted")
        
        if self.loan_taken == 2:
            return print("You can't take loan more thank two times!")
        
        self.loan_taken += 1
        self.loan_balance += amount
        bank.loan_balance += amount
        self.transactions.append(Transaction(self, amount, 'take_loan'))
        print("Loan transferred successfully")
        self.check_balance()

    def fund_transferr(self, bank, receiver_id, amount):
        if self.amount_validity( amount, True) is False:
            return

        user = bank.find_user(receiver_id)
        if user is None:
            return
        
        self.update_balance(amount)
        user.balance += amount
        self.transactions.append(Transaction(self, amount, 'fund_transferr'))
        user.transactions.append(Transaction(user, amount, 'fund_transferr'))
        print(f"Fund Transferr to '{user.name}' amount {amount} is successfull!")

    def __repr__(self):
        details = f"Account ID: {self.account_id} \nName: {self.name} \nAccount Type: {self.account_type} \nBalance: {self.balance}"
        return details