def square_number(num):     # Define a function called square_number that takes a number as input
    return num ** 2         # This function takes a number as input and returns its square

input_num = float(input("Enter a number: "))    # Prompt the user to enter a number accepts the input as a float or integer

print(f'The square of {input_num} is {square_number(input_num)}')   # Calculate the square of the input number and print the result