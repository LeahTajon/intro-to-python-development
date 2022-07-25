"""
File: w08_Multiplication_Table.py
Author: Leah Tajon

Overview:
In this activity you'll write a program that uses loops within loops
to generate multiplication tables.
"""

# Ask the user for the number of rows and columns.
number = int(input("How many columns and rows do you want in your multiplication table? "))

range_number = number + 1

for row in range(1, range_number):
    for col in range(1, range_number):
        ans = row * col
        print(f"{ans:3}",end=" ")
    print()
