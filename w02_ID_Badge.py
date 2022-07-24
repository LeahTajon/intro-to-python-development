"""
Author: Leah Tajon

Formatted ID Badge:

Write a program to prompt the user for the following:
First name, Last Name, Email Address, Phone Number, Job title, and ID Number

Format it in a very specific way.   

Additional requirements:
>> The last name should be converted from whatever the user types to be displayed in ALL CAPS.
>> The job title should be displayed so that the first letter is capitalized.
>> The email address should be displayed in all lowercase.
"""
print()
print("Please enter the following information:")

fname = input("First name: ")
lname = input("Last name: ")
email = input("Email Address: ")
phone = input("Phone number: ")
job = input("Job title: ")
idnum = input("ID Number: ")

#Stretch challenges
#Add hair color and eye color and put them both on the same line in the display.
hairColor   = input("Hair color: ") 
eyeColor    = input("Eye color: ")

#Add the name of the month they started and a yes/no field for training. Put them on the same line.
month   = input("Month: ")
training    = input("Training (Y/N): ")

print()
print("The ID Card is:")
print("--------------------------------------------")
print(lname.upper() + "," + fname.capitalize())
print(job.title())
print("ID: " + idnum)
print()
print(email.lower())
print(phone)
print()
print(("Hair: " + hairColor.capitalize() + "\t" + "Eye: " + eyeColor.capitalize()).expandtabs(30))
print(("Month: " + month.capitalize() + "\t" + "Training: " + training.capitalize()).expandtabs(30))
print("--------------------------------------------")
print()

