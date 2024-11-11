
class Order:
    def __init__(self):
        self.cart_items = {}

    def view_cart(self):

        print("_______________ Cart Items _______________")

        print("\nName\tPrice\tQuantity")
        for item in self.cart_items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    def get_cart_item(self, restaurnt, item_name):
        item = restaurnt.find_item(item_name)
        if item not in self.cart_items: 
            print(f"{item_name} not added in cart")
            return
        
        return int(self.cart_items[item])

    def add_to_cart(self, item,quantity):
        self.cart_items[item] = self.cart_items.get(item,0) + quantity
        print(f"Success: {item.name} added to cart!")
            
    def remove_from_cart(self,restaurant, item_name):
        item = restaurant.find_item(item_name)

        if item in self.cart_items:    
            del self.cart_items[item]
            print(f"Success: {item_name} removed from cart!")
        else:
            print(f"Error: {item_name} not found!")

    def clear_cart(self):
        self.cart_items = {}

    @property
    def total_bill(self):
        return sum(int(item.price)*int(quantity) for item,quantity in self.cart_items.items())

    def pay_bill(self, amount_taken):
        if self.total_bill > amount_taken:
            print(f"Error: Total bill {self.total_bill}, need {self.total_bill - amount_taken} more!")
            return

        change = amount_taken - self.total_bill
        print(f"Success: Total bill {self.total_bill} paid, your change {change}!")
        self.clear_cart()
