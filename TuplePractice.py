""" Tuples
Problem 5: Create a tuple with the names of the days of the week. Write a function to:


Print the first and last days of the week.

Check if "Wednesday" is in the tuple and print the result.

Problem 6: Given a tuple of numbers, write a function to:


Convert the tuple to a list.

Sort the list in ascending order.

Convert the list back to a tuple and print it.
"""

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def my_function():
    #print first and last day of the week
    print(days[0])
    print(days[6])
    #check if wednesday is in days tuple
    if 'Wednesday' in days:
        print("Yes, Wednesday is in days")
    else:
        print("Wednesday is not in days")

my_function()



numbers_tuple = 2,3,4,1,5

def function():
    #convert tuple to list
    numbers_list = list(numbers_tuple)
    #sort list
    numbers_list.sort()
    #convert list back to tuple
    new_tuple = tuple(numbers_list)
    
    print(new_tuple)
    
function()
