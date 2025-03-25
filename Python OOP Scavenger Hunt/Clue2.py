"""
Clue 2

In this hint, we added a method to 
the class named farm_beets.
"""
class Manager:
    def __init__(self,name, department, employees=None):
        self.name = name
        self.department = department
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print(f"{employee} is already an employee of the {self.department} department)")
            
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Employees: {self.employees}"
    
    def farm_beets():
        print ("Farming beets.")
        
manager1 = Manager("Michael Scott", "Sales", ["Jim", "Dwight", "Pam"])
print(manager1.get_info())
manager1.add_employee("Ryan")
print(manager1.get_info())

Manager.farm_beets()

new_employee = input("Enter the name of the new employee: ")
manager1.add_employee(new_employee)
print(manager1.get_info())