"""
File: w02_MadLib.py
Author: Leah Tajon

Assignment: MadLib

You will implement a program that asks the user for a series of words
and then displays the story with the user's words inserted into the 
appropriate places.

This program also contains a way to implement the stretch challenges.
"""
print()
print("\nPlease enter the following:")
print()
adj = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclam = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
print()

# Stretch
# Added a song MadLib. Added more words that will be filled in
obj1 = input("object: ")
direction = input("direction: ")
obj2 = input("object: ")
obj3 = input("object: ") 


print("\nYour story is:\n")

print("The other day, I was really in trouble. It all started when I saw a very ")
print(f'{adj} {animal} {verb1} down the hallway. "{exclam.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print("right in front of my family.\n")

# Stretch
# Added a song MadLib. 
print("\nThe song is:\n")
print(f"Twinkle, twinkle, little {obj1}.")
print(f"How I wonder what you are.")
print(f"{direction.capitalize()} above the world so high")
print(f"Like a {obj2} in the sky")
print(f"Twinkle, twinkle, little {obj3}")
print(f"How I wonder what you are.\n")