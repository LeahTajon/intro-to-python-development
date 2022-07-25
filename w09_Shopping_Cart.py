"""
File: w09_Prove.py
Author: Leah Tajon

Project: Shopping Cart
Description: For this project you will create a program that stores a list of products in a
shopping cart along with their prices. The user should have the ability to add items to the list,
remove them, and see the total price of the cart.
"""

print("\nWelcome to the Shopping Cart Program!\n")

# 02 - Create a list that will store the names of the items in the shopping cart.
add_new = []

# 01 - Have a menu system that repeats until the user chooses to quit.
action = -1
while action != 5:
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")

    action = int(input("Please enter an action: "))
    
    if action != 5:
        # 03 - Complete the option to add the name of the item to the list.
        if action == 1:
            add_item = input("What item would you like to add? ")
            add_new.append(add_item)
            print(f"'{add_item}' has been added to the cart.\n")
        # 04 - Complete the option to display the names of the items in the list.
        elif action == 2:
            print("The contents of the shopping cart are:")
            for item in add_new:
                print(item)
            print()         
    else:
        print("Thank you. Goodbye!")
    

        
     