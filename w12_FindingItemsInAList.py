"""
File: w12_FindingItemsInAList.py
Author: Leah Tajon

Overview: 
This activity will help  you practice finding things in a list.
Write a program to find the youngest person in the list.
"""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_so_far = 999
youngest_name = " "

for item in people:
    value = item
    part = value.split(" ")
    
    name = part[0]
    age = int(part[1])

    #print(value)
    print(f"Name: {name}, Age: {age}")

    if age < youngest_so_far:
        youngest_so_far = age
        youngest_name = name

print(f"\nThe youngest person is {youngest_name} with an age of {youngest_so_far}\n")


    
    



    
