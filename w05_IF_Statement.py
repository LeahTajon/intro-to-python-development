"""
File: w05_Checkpoint_IF_Statement.py
Author: Leah Tajon

Overview: 
Practice the mechanics of if statements.
"""

# Write a program that asks the user for two integers.
first_num = int(input("What is the first number? "))
second_num = int(input("What is the second number? "))

# Then, write three separate if/else statements as follows:
# If the first number is greater than the second, print "The first number is greater".
# Otherwise, print "The first numbre is not greater".
if first_num > second_num:
    print('The first number is greater')
else:
    print('The first number is not greater')

# If the two numbers are equal print "The numbers are equal."
# Otherwise, print "The numbers are not equal."
if first_num == second_num:
    print('The numbers are equal')
else:
    print('The numbers are not equal.')

# If the second number is greater than the first, print "The second number is greater".
# Otherwise, print "The second number is not greater".
if second_num > first_num:
    print('The second number is greater.')
else:
    print('The second number is not greater')

# Have the program ask the user for their favorite animal.
# Then write an IF statement as follows:
animal = input('\nWhat is your favorite animal? ')

# Check to see if the user's favorite animal is the same as your favorite animal
# (meaning you, the programmer). If it is, print "That's my favorite animal too!".
# If it's not, print "That one is not my favorite." Verify that it works regardless
# of the capitalization.
if animal.lower() == 'cat':
    print("That's my favorite animal too!\n")
else:
    print("That's not my favorite.\n")
