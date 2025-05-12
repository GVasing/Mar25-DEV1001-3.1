# Ask the user for the name of an event (e.g., "Birthday Party").
# Ask for the number of adult guests (integer).
# Ask for the number of child guests (integer).
# Assume adult tickets cost $25.75 each and child tickets cost $12.50 each.
# Calculate the total cost for adult tickets and child tickets separately.
# Calculate the overall total cost for the event.
# Print a summary using f-strings, formatting all costs to two decimal places. Include the event name and guest counts in the summary.
# Example output snippet:
# Event: Birthday Party
# Adult Guests: 10, Child Guests: 5
# Cost for Adults: $257.50
# Cost for Children: $62.50
# Total Event Cost: $320.00

name = input('What\'s the name of the event? ')
adult_amount = int(input('How many adults will be attending? '))
child_amount = int(input('How many chilldren will be attending? '))

adult_ticket = 25.75
child_ticket = 12.50

adult_admission = adult_ticket * (adult_amount)
child_admission = child_ticket * (child_amount)
Total = adult_admission + child_admission

print(f'''
Event: {name} 
Adult Guests: {adult_amount} 
Child Guests: {child_amount} 
Total Adult Price: {adult_admission} 
Total Child Price: {child_admission} 
Overall Price {Total}''')