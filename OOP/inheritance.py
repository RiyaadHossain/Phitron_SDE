# Parent Class
class Device:
    def __init__(self, brand, price):
            self.brand = brand
            self.price = price

    def run(self):
          return f'Running device {self.brand}'
    
# Child Class
class Laptop(Device):
      def __init__(self, name, brand, price):
        self.name =name;
        super().__init__(brand, price) # Inherit attrubutes and methods
    
lenevof12 = Laptop("Lenevo F12", "Lenevo", 80000)

print(lenevof12.run())

        