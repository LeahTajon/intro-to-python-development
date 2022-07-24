"""
File: w04_Conversion.py
Author: Leah Tajon

Overview:
Practice solving problems with variables and expressions, and
displaying results.

The Problem: Converting between different types of units

Assignment: 
Write a program to convert from Fahrenheit to Celsius. 
Display the result to one decimal place of precision.
"""

# Ask the user to enter temperature in Fahrenheit
fahrenheit = float(input("\nWhat is the temperature in Fahrenheit? "))

# Convert degrees in Fahrenheit to Celsius
conversion_to_celsius = (fahrenheit - 32) * (5/9)

# Display the result
print(f"The temperature in Celsius is {conversion_to_celsius:.1f} degrees.\n")
