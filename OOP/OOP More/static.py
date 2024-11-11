class Shop:
    # Static Attributes
    country = "Bangladesh"
    def __init__(self,name, location):
        self.name = name
        self.location = location

    @staticmethod
    def doMath(a, b):
        print(a+b);

    @classmethod
    def getName(self):
        print(self.country)
    
myShop = Shop("my Shop", "Lohagara")

Shop.doMath(2, 3) # Static Method
Shop.getName()