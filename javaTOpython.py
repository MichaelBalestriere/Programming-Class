class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def speak(self):
        print(f"{self.name} barks.")
        

def main():
    animal = Animal("Generic Animal", 5)
    animal.speak()

    dog = Dog("Buddy", 2, "Golden Retriever")
    dog.speak()
    print(f"{dog.name} is a {dog.breed} and is {dog.age} years old.")

if __name__ == "__main__":
    main()