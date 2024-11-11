
# Encapsulation - Hide details (attributes || methods || functionality ) inside the class
class BankAccount:
    def __init__(self, name, accuntId, initDiposit):
        self.name = name # Public
        self.accuntId = accuntId # Protected (Consider)
        self.__balance = initDiposit # Private 

    def getBalance(self):
        return self.__balance

    # Hide the balance calculation
    def withDraw(self, amount):
        if(amount > self.__balance): # private attributes only can be accessed inside the class
            return f'Can\'t withdraw more than savings'
        self.__balance -= amount
        return f"Here is your amount {amount}"
    

    

san_account = BankAccount("San", 972342234, 1000)
print(san_account.getBalance())
    
        