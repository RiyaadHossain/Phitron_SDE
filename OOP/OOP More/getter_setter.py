class User:
    def __init__(self, name,money):
        self.name = name
        self.__balance = money  

    @property
    def balance(self): # Getter -> readonly
        return self.__balance
    
    @balance.setter
    def addMoney(self, money): # Setter -> modify value with checks
        if money < 0: return "Can't be negative"
        self.__balance+=money

    
someone = User("Someone", 100)

# print(someone.balance())
print(someone.balance) # Getter

# print(someone.addMoney(100))
someone.addMoney = 100 # Setter
print(someone.balance) 