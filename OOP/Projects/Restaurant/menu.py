class Menu:
    def __init__(self):
        self.items = []

    def view_menu(self):
        print("_______________ Menu Items _______________")

        print("\nName\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    def find_item(self, item_name):
        return next((item for item in self.items if item.name.lower() == item_name.lower()), None)

    def add_item(self, item):
        if any(f_item.name.lower() == item.name.lower() for f_item in self.items):
            print(f"Error: Food Item {item.name} already exist!")
            return

        self.items.append(item)
        print(f"Success: Food Item {item.name} added!")
        

    def remove_item(self, item_name):
        item = self.find_item(item_name)

        if item:
            self.items.remove(item)
            print(f"Success: Item {item_name} removed!")
        else:
            print(f"Error: Item {item_name} not found!")
