"""
File: w09_Team.py
Author: Leah Tajon

Assignment: Lists of Numbers
"""

num_lists = []

# Ask the user for a series of numbers, and append each one to a list.
# Stop whent they enter 0.
print("Enter a list of numbers, type 0 when finished.")

num_add = -1

while num_add != 0:
    num_add = int(input("Enter number: "))
    if num_add != 0:
        num_lists.append(num_add)

# 01 - Compute the sum, or total, of the numbers in the list.
sum = 0
for num in num_lists:
    sum+= num
print(f"The sum is: {sum}")

# 02 - Compute the average of the numbers in the list.
ave = sum / len(num_lists)
print(f"The average is: {ave:.2f}")

# 03 - Find the maximum, or largest, number in the list.
max_num = max(num_lists)
print(f"The largest number is: {max_num}")
