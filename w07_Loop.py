"""
File: w07_Loop.py
Author: Leah Tajon

Overview: Demonstrate your understanding of loops by completing the following
individual checkpoint assignment.
"""

# CHECKPOINT 1
# Use a while loop to ask the user for a positive number (>=0). 
# Continue asking as long as the number is negative, then display the number.

num = int(input("Please type a positive number: "))

while num < 0:
    print("\nSorry, that is a negative number. Please try again.")
    num = int(input("Please type a positive number: "))

print(f"The number is: {num}")

# CHECKPOINT 2
# Use a while loop, to simulate a child asking their parent for a piece of candy.
# Have the program keep looping until the user answer "yes", then have the program
# output "Thank you".

response = 'no'

while response.lower() != 'yes':
    response = input("May I have a piece of candy? ")

print("Thank you.")