print("This is a test to check for Python")

name = input("what is your name?")
last = input("what is your last name?")

name = name + " " + last

print("Hello", name)

answer = input("Is your name " + name + "?")
if answer == "yes":
    print("Thank you for confirming")
else:
    print("Sorry for the confusion")
    
age = int(input("How old are you?"))

if age < 21:
    print("You are not old enough to drink")
else:
    print("You are old enough to drink")
    
email = input("What is your email?")
phone = input("What is your phone number?")
address = input("What is your address?")

print("your name is " , name, "you are ", age, "your email is ", email, "your phone number is ", phone, "your address is ", address)

    
    