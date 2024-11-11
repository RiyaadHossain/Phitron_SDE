from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name = name 
        self.employee = []
        self.menu = Menu()

    def view_emp(self):
        print("_______________ Employee List _______________")

        print("\nName\tdesignation\tsalary")
        for emp in self.employee:
            print(f"{emp.name}\t{emp.designation}\t{emp.salary}")

    def add_emp(self, emp):
        if emp in self.employee:
            print("Error: Employee {emp.name} already added!")
            return

        self.employee.append(emp)
        print(f"Success: Employee {emp.name} added!")

    def remove_emp(self, emp_name):
        employee = next((emp for emp in self.employee if emp.name == emp_name), None)

        if employee:
            self.employee.remove(employee)
            print(f"Success: Employee {emp_name} removed successfully")
        else:
            print(f"Error: No Employee found!")

    def view_menu(self):
        self.menu.view_menu()

    def find_item(self, item_name):
        return self.menu.find_item(item_name)

    def add_item(self, item):
       self.menu.add_item(item)
        
    def remove_item(self, item_name):
        self.menu.remove_item(item_name)
