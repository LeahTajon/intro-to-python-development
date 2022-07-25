"""
File: w06_Ride.py
Author: Leah Tajon

Overview: For this assignment, you'll work as a team to write a program for a 
fictitious amusement park ride.
"""
# Prompt the user for the age and height of the first person.
rider1_age = int(input("\nWhat is the age of the first rider? "))
rider1_height = float(input("What is the height of the first rider (in inches)? "))

# Ask whether there is a second rider, and if so, ask for their age and height
rider2 = input("Is there a second rider (yes/no)? ")

# Handle the case of both riders
if rider2.lower() == 'yes':
    rider2_age = int(input("What is the age of the second rider? "))
    rider2_height = float(input("What is the height of the second rider? "))
    # No one under 36 inches may ever ride, either by themselves or with another rider
    if rider1_height < 36 or rider2_height < 36:
        print("Sorry, you may not ride.")
    else:
        # If there are two riders and one of them is at least 18 years old, they may ride together
        if rider1_age >= 18 or rider2_age >= 18:
            print("\nWelcome to the ride. Please be safe and have fun!\n")
        # Stretch - 1
        # If there are two riders, but neither one is at least 18 years old, they may still ride
        # as long as they both at least 12 years old and at least 52 inches tall.
        elif rider1_age >= 12 and rider2_age >=12 and rider1_height >= 52 and rider2_height >= 52:
            print("\nWelcome to the ride. Please be safe and have fun!\n")
        else:
            print("\nSorry you may not ride.\n")

# Handle the case of the first rider
elif rider2.lower() == 'no':
    # A single rider can only ride if they are at least 18 years old
    # and are at least 62 inches tall
    if rider1_height >= 62 and rider1_age >= 18:
        print("\nWelcome to the ride. Please be safe and have fun!\n")
    # If the conditions are not met, first rider is not allowed to ride
    else:
        print("\nSorry, you may not ride.\n")