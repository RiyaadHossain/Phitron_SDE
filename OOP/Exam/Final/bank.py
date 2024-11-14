class Bank:

    def __init__(self, name, address, capital):
        if capital < 0:
            return print("Bank capital can't be negative")

        self.name = name 
        self.address = address 
        self.capital = capital 
        self.loan_feature = True
        self.loan_balance = 0 
        self.user_accounts = []
        self.admins = []

    def generate_admin_id(self):
        return f"A-{101+len(self.admins)}"

    def generate_account_id(self):
        return f"U-{101+len(self.user_accounts)}"

    def find_user(self, account_id):
        user_found = next((user for user in self.user_accounts if user.account_id == account_id), None)

        if user_found is None:
            print(f"No user account find with id {account_id}")

        return user_found
    
    def account_list(self):
        for user in self.user_accounts:
            print(user)
    
    def delete_user(self, account_id):
        user = self.find_user(account_id)
        if user is None:
            return

        self.user_accounts = [user for user in self.user_accounts if user.account_id != account_id]
        print(f"User account deleted with id {account_id}")

    def check_balance(self):
        print(f"Capital: {self.capital} Loan Banlance: {self.loan_balance}")

    def update_loan_feature(self, status):
        if self.loan_feature == status:
            return print(f"Loan feature is already {'on' if status == True else 'off'}")
        
        self.loan_feature = status
        print(f"Loan feature is updated to {'on' if status == True else 'off'}")