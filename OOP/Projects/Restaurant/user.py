from order import Order
class User:
    def __init__(self,name, email, phone, address):
        self.name = name
        self.email = email
        self.phone= phone
        self.address= address

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age= age
        self.designation= designation
        self.salary= salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def view_emp(self,restaurant):
        restaurant.view_emp()

    def add_emp(self,restaurant,emp):
        restaurant.add_emp(emp)

    def remove_emp(self,restaurant, emp_name):
        restaurant.remove_emp(emp_name)

    def view_menu(self,restaurant):
        restaurant.view_menu()

    def add_item(self,restaurant,item):
        restaurant.add_item(item)

    def remove_item(self,restaurant, item_name):
        restaurant.remove_item(item_name)

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.view_menu()

    def add_to_cart(self,restaurant, item_name, quantity):
        item = restaurant.find_item(item_name)
        if item is None:
            print(f"Error: {item_name} not found!")
            return 
        
        if item.quantity < quantity:
            print(f"Error: {item.name} only {item.quantity} pcs available!")
            return
        
        item.quantity -= quantity
        self.cart.add_to_cart(item,quantity)

    def remove_from_cart(self, restaurant, item_name):
        item = restaurant.find_item(item_name)
        if item is None:
            print(f"Error: {item_name} not found!")
            return 
        
        item.quantity += self.cart.get_cart_item(restaurant, item_name)
        self.cart.remove_from_cart(restaurant,item_name)

    def view_cart(self):
        self.cart.view_cart()

    def pay_bill(self,given_amount):
        self.cart.pay_bill(given_amount)

    def checkout(self):
        print(f"Your bill: {self.cart.total_bill}")
        