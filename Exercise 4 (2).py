# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
for list in("Apple", "Banana", "Orange", "pear", "avocado", "strawberry"):
    
 
# TODO: Use a for loop to print each fruit in the list
 print(list)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
 
countdown= 6

while 1 < countdown:
 countdown -=1
 print(countdown)

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for square_numbers in range(1, 11):
    print(square_numbers * square_numbers)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random 

# TODO: Create a list of colors
colors=("red", "yellow", "blue", "navy", "brown","olive", "violet", "green", "pink" )
# TODO: Use a for loop to select and print 3 random colors from the listreturn 
selected_color=()
for x in range(3):
    random_color=random.choice(colors)
    print(random_color)


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions

# TODO: Use a while loop to create a simple calculator
# Import the custom module
import math_operations as mo

# Simple calculator using a while loop
while True:
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = mo.add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")

        elif choice == '2':
            result = mo.subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")

        elif choice == '3':
            result = mo.multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")

        elif choice == '4':
            result = mo.divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")

    else:
        print("Invalid input. Please choose a valid option.")
