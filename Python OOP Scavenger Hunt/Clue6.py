"""
Clue 6

Abstraction is a way to ensure that a subclass 
implements a method from the superclass.
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Manager(Employee):
    def __init__(self, name, department, employees=None):
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
            print(f"{employee} is already an employee of the {self.department} department.")
            
    def get_info(self):
        return f"Name: {self.name}, Department: {self.department}, Employees: {self.employees}"
    
    def farm_beets(self):
        print("Farming beets.")
        
    def work(self):
        print(f"{self.name} is managing the department.")

    def __del__(self):
        print("Manager object deleted")

class Salesperson(Manager):
    def __init__(self, name, department, employees=None, sales_target=0):
        super().__init__(name, department, employees)
        self.sales_target = sales_target
    
    def work(self):
        print(f"{self.name} is working on reaching the sales target of {self.sales_target}.")

manager1 = Manager("Michael Scott", "Sales", ["Jim", "Dwight", "Pam"])
print(manager1.get_info())
manager1.add_employee("Ryan")
print(manager1.get_info())

manager1.work()

salesperson1 = Salesperson("Pam Beesly", "Sales", ["Jim", "Dwight"], 100)
print(salesperson1.get_info())
salesperson1.work()

del manager1
