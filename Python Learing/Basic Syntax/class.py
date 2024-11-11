class Pen:
    # class attributes (same to all instance)
    brand = 'Matador'

    # constructor
    def __init__(self, name, color, price): 
        # instance attributes (unique to every instance)
        self.name = name
        self.color = color
        self.price = price
    
    # methods
    def write(self, text):
        print(text)

    # Note: Passing self to constructor & every methods is must
        
hi_shcool =Pen('Hi School', 'Black', 5)

print(hi_shcool.color)
hi_shcool.write("Be a good muslim")
