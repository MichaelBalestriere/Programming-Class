# Python Sorting Exercises

# Exercise 1 Sort lists

a = [5, 1, 4, 3]    # Creates a list of numbers
print(sorted(a))    # [1, 3, 4, 5]
print(a)            # [5, 1, 4, 3]

# Exercise 2 Sort lists with key

strs = ['ccc', 'aaaa', 'd', 'bb']  # Creates a list of strings
print(sorted(strs, key=len))       # ['d', 'bb', 'ccc', 'aaaa'] based on string length

# Exercise 3 Sort method

strs = ['xc', 'zb', 'yd', 'wa']    # Creates a list of strings
strs.sort()                        # Sorts the list in place
print(strs)                        # ['wa', 'xb', 'yd', 'za']

# Python Dictionary and File Exercises

# Exercise 1 Dictionary creation

d = {'foo': 42, 'bar': 100, 'baz': 1000}  # Creates a dictionary
print(d)                                  # {'foo': 42, 'bar': 100, 'baz': 1000}

# Exercise 2 Dictionary interation

for key in d:          # Iterates over the keys in the dictionary
    print(key, d[key]) # Prints the key and the value
    
# Exercise 3 File reading and writing

f = open('workfile', 'w')  # Opens a file for writing
f.write('This is a test\n') # Writes a string to the file


