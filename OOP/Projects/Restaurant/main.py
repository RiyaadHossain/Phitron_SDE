from user import Admin, Employee, Customer
from restaurant import Restaurant
from order import Order
from food_item import FoodItem
from menu import Menu

customer = None
admin = None

mama_restro = Restaurant("Mama Restaurant")

def customer_manual():

    while True:
        print("\n")
        print("1. View Menu")
        print("2. Add To Cart")
        print("3. View Cart")
        print("4. Remove From Cart")
        print("5. Checkout")
        print("6. Pay Bill")
        print("7. Exit")

        option = int(input("Select an option: "))

        if option == 1:
            customer.view_menu(mama_restro)
        elif option == 2:
            print("\n________ Item Info ________")
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            customer.add_to_cart(mama_restro, name, quantity)

        elif option == 3:
            customer.view_cart()

        elif option == 4:
            item_name = input("Item Name: ")
            customer.remove_from_cart(mama_restro, item_name)
        
        elif option == 5:
            customer.checkout()

        elif option == 6:
            given_amount = int(input("Pay Amount: "))
            customer.pay_bill(given_amount)
        
        elif option == 7:
            break

        else:
            print("Invalid Choice")

def admin_manual():

    while True:

        print("\n")
        print("1. View Employee")
        print("2. Add New Employee")
        print("3. Remove Employee")
        print("4. View Menu")
        print("5. Add Item")
        print("6. Remove Item")
        print("7. Exit")

        option = int(input("Select an option: "))

        if option == 1:
            admin.view_emp(mama_restro)
        elif option == 2:
            print("\n________ Employee Info ________")

            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            age = input("Age: ")
            designation = input("Designation: ")
            salary = input("Salary: ")
            
            emp = Employee(name, email, phone, address, age, designation, salary)
            admin.add_emp(mama_restro, emp)

        elif option == 3:
            emp_name = input("Name: ")
            admin.remove_emp(mama_restro, emp_name)

        elif option == 4:
            admin.view_menu(mama_restro)
        
        elif option == 5:

            print("\n________ Item Info ________")
            name = input("Name: ")
            price = int(input("Price: "))
            quantity = int(input("Quantity: "))

            item = FoodItem(name, price, quantity)
            admin.add_item(mama_restro, item)

        elif option == 6:
            item_name = input("Name: ")
            admin.remove_item(mama_restro, item_name)
        
        elif option == 7:
            break

        else:
            print("Invalid Choice")

def main_manual():
    while True:
        print(f"\nWelcome to {mama_restro.name}")

        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        option = int(input("Choose your role:"))

        print("\n________ User Info ________")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")

        if option == 1:
            global admin
            admin = Admin(name, email, phone, address)
            print(f"\nWelcome {admin.name} to {mama_restro.name}")
            admin_manual()
        elif option == 2:
            global customer
            customer = Customer(name, email, phone, address)
            print(f"\nWelcome {customer.name} to {mama_restro.name}")
            customer_manual()
        elif option == 3:
            break
        else:
            print("Invalid Input")

main_manual()
        