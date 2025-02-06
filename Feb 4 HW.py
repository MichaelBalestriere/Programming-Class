# Python String Exercises 

# Exercise 1 String Manipulation

s = 'hi'             # Sets the 's' variable to the string 'hi'
print(s[1])          # Will print the indexed value at 1. Strings start indexing at 0 so the code will print 'i'
print(len(s))        # The len() function wil return how long the string is starting with 1 and not 0. Code will print '2'
print(s + ' there')  # The '+' sign will concatitnate the the string stored in the variable 's' with the string that comes after. Anser will be 'hi there'

# Exercise 2 String Methods

s = 'hi'                    # Sets the 's' variable to the string 'hi'
print(s.lower())            # Will print s in all lower case. 'hi'
print(s.upper())            # Will print s in all Upper case. 'HI'
print(s.startswith('h'))    # Will return 'True' if s starts with 'h'
print(s.find('i'))          # Will return the indexed value where 'i' is found. Output is '1'
print(s.replace('h','H'))   # Will replace 'h' with 'H'

# Exercise 3 String Slices

s = "Hello"         # Sets the 's' variable to the string 'Hello'
print(s[1:4])       # Prints 'ell' because it starts at index 1 and extends up to but not including index 4
print(s[1:])        # Prints 'ello' because omitting either index defaults to the start or end of the string
print(s[:])         # Prints 'Hello' because omitting both always gives us a copy of the whole thing 
print(s[1:100])     # prints 'ello' because an index that is too big is truncated down to the string length


# Python List Exercises

# Exercise 1 List Manipulation 

colors = ['red', 'blue', 'green']   # Creates a list of colors
print(colors[0])                    # Accessing the first element of the list, which is 'red' becasue list indexing starts at 0
print(colors[2])                    # Accessing the third element of the list, which is 'green'
print(len(colors))                  # Getting the length of the list, which is 3 because there are 3 elements in the list

# Exercise 2 List Methods

list = ['larry', 'curly', 'moe']    # Creates a list of names
list.append('shemp')                # The append() method adds 'shemp' to the end of the list  
list.insert(0, 'xxx')               # The insert() method inserts 'xxx' at index 0, shifting the other elements to the right  
list.extend(['yyy', 'zzz'])         # The extend() method adds the elements 'yyy' and 'zzz' to the end of the list  
print(list)                         # Will print the updated list: ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']  

print(list.index('curly'))          # The index() method returns the index position of 'curly'. Output is '2'  

list.remove('curly')                # The remove() method finds and removes 'curly' from the list  
list.pop(1)                         # The pop() method removes and returns the element at index 1, which is 'larry'  
print(list)                         # Will print the updated list: ['xxx', 'moe', 'shemp', 'yyy', 'zzz']  

# Exercise 3 List Slices

list = ['a', 'b', 'c', 'd']     # Creates a list of letters 
print(list[1:-1])               # Prints ['b', 'c'] because it starts at index 1 and extends up to but not including the last index  
list[0:2] = 'z'                 # Replaces elements at index 0 and 1 (['a', 'b']) with ['z']  
print(list)                     # Prints ['z', 'c', 'd'] because 'a' and 'b' were replaced 
