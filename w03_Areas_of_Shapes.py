"""
Team Activity: Areas of Shapes
Course: CSE110 - Team 3

Requirements: Write a program to compute the areas of three different shapes. Prompt
for the necessary information, then compute and display the area.

Shapes: Square, Rectangle and Circle
"""
import math

#Area of Square
square = input("\nWhat is the length of a side of the square? ")
area_square = float(square) ** 2
print(f"The area of the square is: {area_square}\n")

# #Area of Rectangle
rec_length = input("What is the length of rectangle? ")
rec_width = input("What is the width of the rectangle? ")

area_rectangle = float(rec_length) * float(rec_width)
print(f"The area of the rectangle is: {area_rectangle}\n")

#Area of Circle
circle = input("What is the radius of the circle? ")
pi = 3.14
area_circle = pi * (float(circle)**2)

print(f"The area of the circle is: {area_circle}\n")

#STRETCH #01
"""
Instead of using 3.14, see if you can find and use the built-in value of Pi
"""

circle = input("What is the radius of the circle? ")
pi = math.pi
area_circle = pi * (float(circle)**2)

print(f"The area of the circle is: {round(area_circle,2)}\n")


#STRETCH #02
"""
Prompt a user for a single length value, then compute and display the areas
of a square with that length of side, a circle with that radius, and then the volumes of
a cube with that side and a sphere with that radius, all from the same value from the user.
"""

num = float(input("\nEnter a number: "))

area_sqr_num = num ** 2                     #Area of square
area_circ_num = math.pi * num ** 2          #Area of circle
vol_cube_num = num ** 3                     #Volume of cube
vol_sphere_num = 4 / 3 * math.pi * (num ** 3)  #Volume Area of a sphere

print(f"\nThe area of the square is: {area_sqr_num}")
print(f"The area of the circle is: {area_circ_num}")
print(f"The volume of the cube is: {vol_cube_num}")
print(f"The surface area of the sphere is: {vol_sphere_num}\n")

#STRETCH #03
"""
For each of the three areas in the core requirements, change the prompt for the
user to ask for the value in centimeters. Then, display the resulting area in both
square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter,
and a square centimeter is 1/10,000 of a square meter.
"""
print("\nPlease enter the values in centimeters:")

#SQUARE
square_3 = float(input("\nWhat is the length of a side of the square (in cm)? "))
area_sqr_cm = square_3 ** 2
area_sqr_mtr = area_sqr_cm / 10000

print(f"The area of a square is (cm^2): {area_sqr_cm}")
print(f"The area of a square is (m^2): {area_sqr_mtr}")

#RECTANGLE
rec_length2 = float(input("\nWhat is the length of rectangle (in cm)? "))
rec_width2 = float(input("What is the width of rectangle (in cm)? "))

area_rec2 = rec_length2 * rec_width2
area_rec_mtr = area_rec2 / 10000

print(f'The area of the rectangle is (cm^2): {area_rec2}')
print(f'The area of the rectangle is (m^2): {area_rec_mtr}')

#CIRCLE
circ_radius = float(input('\nWhat is the radius of the circle? '))
pi = 3.14
area_circ2 = pi * (circ_radius**2)
area_circ_mtr = area_circ2 / 10000

print(f"\nThe area of the circle is (cm^2): {area_circ2}")
print(f"The area of the circle is (m^2): {area_circ_mtr}\n")


