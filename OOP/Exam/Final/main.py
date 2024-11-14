from user import User
from bank import Bank
from transaction import Transaction
from admin import Admin

riba_free_bank = Bank("Say no to Riba", "World", 10000)

# admin = Admin("Admin", "admin", riba_free_bank)
user1 = User("User1", "user1", "World", 'savings', riba_free_bank)

user = None
admin = None

def user_manual():
    name = input("\nEnter Name:")
    email = input("Enter Email:")
    address = input("Enter Address:")
    account_type = ''

    while True:
        print("Choose Account Type:")
        print("1. Savings")
        print("2. Current")

        option = int(input("Type Here:"))
        if option == 1:
            account_type = 'savings'
        elif option == 2:
            account_type = 'current'
        else:
            print("Invalid Choice")

        if account_type != '':
                    break
         
    user = User(name, email, address, account_type, riba_free_bank)

    while True:
        print("\nSelect Option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Take Loan")
        print("5. Fund Transferr")
        print("6. Transaction History")
        print("7. Exit")

        option = int(input("Type Here:"))

        if option == 1:
             amount = int(input("Enter Amount:"))
             user.deposit(amount, riba_free_bank)
        elif option == 2:
             amount = int(input("Enter Amount:"))
             user.withdraw(amount, riba_free_bank)
        elif option == 3:
             user.check_balance()
        elif option == 4:
             amount = int(input("Enter Amount:"))
             user.take_loan(riba_free_bank, amount)
        elif option == 5:
             amount = int(input("Enter Amount:"))
             receiver_id = input("Enter Receiver Id:")
             user.fund_transferr(riba_free_bank, receiver_id, amount)
        elif option == 6:
             user.transaction_history()
        elif option == 7:
            break
        else:
            print("Invalid Choice")


def admin_manual():
    name = input("\nEnter Name:")
    email = input("Enter Email:")
    
    admin = Admin(name, email, riba_free_bank)

    while True:
        print("\nSelect Option:")
        print("1. User Account List")
        print("2. Check Balance")
        print("3. Update Loan Feature")
        print("4. Delete User")
        print("5. Exit")

        option = int(input("Type Here:"))

        if option == 1:
             print("\nUser Account List")
             admin.account_list(riba_free_bank)
        elif option == 2:
             admin.check_balance(riba_free_bank)
        elif option == 3:
             
             status = None
             while True:
                    print("Select Loan Feature Status:")
                    print("1. On")
                    print("2. Off")

                    cmd = int(input("Type Here:"))

                    if cmd == 1:
                         status = True
                    elif cmd == 2:
                         status = False
                    else:
                         print("Invalid Choice")

                    if status is not None:
                         break

             admin.update_loan_feature(riba_free_bank, status)
        elif option == 4:
             user_account_id = input("Enter User Account ID:")
             admin.delete_user(riba_free_bank, user_account_id)
        elif option == 5:
            break
        else:
            print("Invalid Choice")


def main_manual():

    print(f"____________ Welcome to {riba_free_bank.name} ____________")

    while True:
        print("\nChoose your role:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        option = int(input("Select Option:"))
        if option == 1:
            admin_manual()
        elif option == 2:
            user_manual()
        elif option == 3:
             break
        else:
            print("Invalid Choice")

        
main_manual()

