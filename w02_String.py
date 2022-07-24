"""
Author: Leah Tajon

Assignment:
Prompt the user for their first name.Then, prompt them for their last name. 
Display the text back all on one line saying, "Your name is last-name, first-name, last-name"

"""

first_name  = input("What is your first name? ")
last_name   = input("What is your last name? ")

output  =   f'Your name is {last_name}, {first_name} {last_name}.'
print(output)

