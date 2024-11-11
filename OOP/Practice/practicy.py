# Write what is meant by operator overloading and method overriding with examples.

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __gt__(self, other):
        return self.age > other.age
    
    def __str__(self):
        return f'{self.name} {self.age}'

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

# Find out which of these players is older using the operator overloading.
players = [sakib, musfiq, kamal, jack, kalam]
oldest_player = max(players, key= lambda player: player.age)
print(oldest_player)


# Write down 4 differences between the class method and static method with proper examples.
# Write what are getter and setter with proper examples
# Explain the difference between inheritance and composition with proper examples.

