class Person:
    def __init__(self,name,age):
        self.name =name 
        self.age = age

    def eat(self, food):
        print(f'Eat {food}')

    # Forcing to implement the method
    def practice(self):
        raise NotImplementedError
    
class Cricketer(Person):
    def __init__(self, name, age,rating, team):
        self.rating =rating
        self.team = team
        super().__init__(name, age)

    # Overriding eat method
    def eat(self, food):
        print(f'Cricketer eat {food}')

    # Force to implement practice method
    def practice(self):
        print('Practicing')

    # Override operator fucntion
    def __add__(self, other):
        return self.age + other.age
    
    # Override operator fucntion
    def __gt__(self, other):
        return self.rating > other.rating

sakib = Cricketer("Sakib", 32, 899, "Ban")
mushi = Cricketer("Mushi", 30, 893, "Ban")

print(sakib+mushi); # Override add funciton
print(sakib>mushi);
