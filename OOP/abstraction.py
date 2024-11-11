from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # Defining calss structure to align the derived classes
    def eat(self) -> None:
        pass

class Monkey(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def eat(self):
        print("Eating Banana")
        return super().eat() # Enforcing to use eat fucntion
    
banor = Monkey("Banor")
banor.eat()