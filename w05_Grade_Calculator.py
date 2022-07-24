"""
File: w05_Grade_Calculator.py
Author: Team 3

Overview: 
Write a program that determines the letter grade for a course according to the following scale:
A >= 90, B >= 80, C >= 70, D >= 60, F < 60 
"""

grade = int(input("\nEnter your grade: "))

if grade >= 90:
    grade_a = grade % 10
    letter = 'A'
    if grade_a >= 7 or grade_a <= 10:
        sign = '+'
    elif grade_a < 3:
        sign = '-'
    else:
        sign = ' '
elif grade >= 80:
    grade_b = grade % 10
    letter = 'B'
    if grade_b >= 7:
        sign = '+'
    elif grade_b < 3:
        sign = '-'
    else:
        sign = ' '
elif grade >= 70:
    letter = 'C'
    sign = ' '
elif grade >= 60:
    letter = 'D'
    sign = ' '
elif grade < 60:
    letter = 'F'
    sign = ' '

print("\nThe equivalent letter grade is: " + letter + sign)

if grade >= 70:
    print("Congratulations! You passed the course.\n")
else:
    print("I'm sorry you did not pass the course.\n")
