
class Admin:
    def __init__(self, name, email, bank):
        self.name = name
        self.email = email
        self.admin_id = bank.generate_admin_id()
        bank.admins.append(self)

    def delete_user(self, bank, account_id):
        bank.delete_user(account_id)

    def account_list(self, bank):
        bank.account_list()

    def check_balance(self, bank):
        bank.check_balance()

    def update_loan_feature(self, bank, status):
        bank.update_loan_feature(status)