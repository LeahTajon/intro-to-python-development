"""
File: w03_Numeric.py
Author: Leah Tajon

Overview: 
Practice converting user input to numeric data types and
perform calculations.
"""

# Write a program that does the following:

'''
01. Prompt the user for their age. Convert it to a number, add one to it, and tell them
    how old they will be on their next birthday
'''
age = int(input('How old are you? '))
next_age = age + 1

print("On your next birthday, you will be " + str(next_age))
print()

'''
02. Prompt the user for the number of egg cartons they have. Assume each carton holds
    12 eggs, multiply their number by 12, and display the total number of eggs.
'''
carton = int(input("How many egg cartons do you have? "))
total_eggs = carton * 12

print("You have " + str(total_eggs) + " eggs.")
print()

'''
03. Prompt the user for the number of cookies and a number of people. Then, divide the number
    of cookies by the number of people to determine how many cookies each person gets.
'''

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
shared_cookies = cookies / people

print(f"Each person may have {float(shared_cookies)} cookies")
print()

