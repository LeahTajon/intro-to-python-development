
"""
File: w13_AreaOfAShape.py
Author: Leah Tajon

Assignment:
Write functions to compute and return the areas of squares,
rectangles, and circle. These functions should not display the values
directly, but rather should return them, so they could be used in other
parts of the program.
"""
import math

def compute_area_square(s):
    area_square = s * s
    return area_square

def compute_area_rectangle(l, w):
    area_rectangle = l * w
    return area_rectangle

def compute_are_circle(r):
    area_circle = math.pi * (r ** 2)
    return area_circle

length_square = float(input("What is the length of the side of the square? "))
square = compute_area_square(length_square)
print(f'The area of the square is {square}')

length_rec = float(input('\nWhat is the length of the rectangle? '))
width_rec = float(input('What is the width of the rectangle? '))
rectangle = compute_area_rectangle(length_rec, width_rec)
print(f'The area of the rectangle is {rectangle}')

radius_circ = float(input('\nWhat is the radius of the circle? '))
circle = compute_are_circle(radius_circ)
print(f'The area of the circle is {circle:.2f}')
