"""
File: w10_List_Index.py
Author: Leah Tajon

Overview: Practice working with list indexes.

Assignment: Ask the user for a list of list of items in a shopping list, stop asking for 
items when the user types "quit".
"""
items = []

print('\nPlease enter the items of the shopping list (type: quit to finish):')

add_item = ""

while add_item.lower() != 'quit':
    add_item = input('Item: ')

    if add_item.lower() != 'quit':
        items.append(add_item)

print('\nThe shopping list is:')
for i in range(len(items)):
    print(items[i])

print('\nThe shopping list with indexes is:')
for i in range(len(items)):
    print(f"{i}. {items[i]}")

change_item = int(input('Which item would you like to change? '))
change_value = input('What is the new item? ')

items[change_item] = change_value

print('\nThe shopping list is:')
for i in range(len(items)):
    print(f"{i}. {items[i]}")
