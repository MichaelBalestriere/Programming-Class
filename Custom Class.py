class Person:
    def __init__(self, name, age):
        """
        Initialize a new Person instance.
        
        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def greet(self):
        
        # Print a greeting message including the person's name and age.
        
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Bob", 35)

# Call the greet method
person1.greet()