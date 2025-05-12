# Declare a variable
# A variable is simply a labeled area of RAM (memory)
# 'name' is the label we want to refer to the variable by
# '=' is the assignment operator - 'store the value on the right into the variable on the left'
# 'George is the value we're storing in the variable
name = "George"
# Python will check and see if 'name' already exists.
# If not, Python will create it and store the value in it.
age = 30

# Reference to a variable (no assignment) - reads the current value of the variable
# print(type(name))
# print(type(age))

# Python is dynamically typed (i.e. it figures out the type from the data)
# aka "duck" typing

# Print a message containing the name and age
# Example output: Hello, John! You are 20 years old.
# print('Hello,', name, '! You are', age, 'years old.')
# print('Hello, ' + name + ' ! You are ' + str(age) + ' years old.') # Typecast, or cast
# print(type(age))

# f-string (formatted string)
# print(f'Hello, {name}! You are {age} years old.')
# print(f'In a decade, {name} will be {age + 10} years old!')

item = 'Book'
price = 19.95567
qty = 3

print(f'Item: {item}, Price:{price:.2f}, Quantity:{qty}')