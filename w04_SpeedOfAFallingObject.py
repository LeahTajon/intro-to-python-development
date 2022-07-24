"""
Team Activity: Speed of a Falling Object
Course: CSE110 - Team 3

Overview:
For this activity, you will work to implement a fairly complicated
Physics formula.

Problem: Determine how fast an object will fall.
"""
# Import math library
import math

# 1. | Prompt the user for each of the variables described above.
mass = float(input("\nMass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sec_area = float(input("Cross sectional area (in m^2): "))
drag_const = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# 2. | Compute the value for the inner c. Display the value c to three decimal places
inner_value_c = (1 / 2) * density * cross_sec_area * drag_const
print(f"\nThe inner value of c is: {round(inner_value_c,3)}")

# 3. | Compute the overall velocity. Display the value to three decimal places. 
velocity_at_t = math.sqrt((mass*gravity)/inner_value_c) * (1 - math.exp(-math.sqrt(mass * gravity * inner_value_c)/mass * time))
print(f"The velocity after {time:.1f} seconds is: {velocity_at_t:.3f} m/s\n")