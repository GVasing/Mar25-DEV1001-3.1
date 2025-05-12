# Define a variable pi and assign it the value 3.14159.
# Ask the user to enter the radius of a circle (allow decimals).
# Calculate the area: area = pi * radius * radius.
# Print the radius and the calculated area, formatted to 3 decimal places.
# Example output:
# A circle with radius [Radius] has an area of [Area].

pi = 3.14159
radius = float(input('What is the radius of your cirlce?'))
# area = pi * float(radius) * float(radius)
area = pi * radius * radius

# print(radius)

print(f'{radius} {area:.3f}')

print(f'A circle with a radius of {float(radius)} has an area of {area:.3f}.')
