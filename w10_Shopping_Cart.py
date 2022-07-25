"""
File: w10_Prove.py
Author: Leah Tajon

Project: Shopping Cart
Description: 
For this project you will create a program that stores a list of products in a
shopping cart along with their prices. The user should have the ability to add items to the list,
remove them, and see the total price of the cart.
"""

from os import remove

print("\nWelcome to the Shopping Cart Program!\n")

items = []  # List for the items
prices = [] # List for the prices

# For this project, the user will be given a menu and have the ability to
# choose items from the menu. The options in the menu include the following:
action = 0
while action != 5:
    print("Please select one of the following:")
    print("1. Add item")        # 01. | Add a new item
    print("2. View Cart")       # 02. | Display the contents of the shopping cart
    print("3. Remove Item")     # 03. | Remove an item
    print("4. Compute Total")   # 04. | Compute the total 
    print("5. Quit")            # 05. | Quit

    # When the user chooses one of these options, the program should perform the 
    # appropriate action. Then the program should show them the menu again, and
    # allow them to choose another option. It should continue running until
    # the user choose the option to quit.
    action = int(input("Please enter an action: "))

    if action != 5:
        if action == 1:
            # The program asks the user for the name of the item and the price.
            # The program stores these values in the lists.
            add_item = input("What item would you like to add? ")
            items.append(add_item)
            add_price = float(input(f"What is the price of {add_item}? $"))
            prices.append(add_price)
            print(f"'{add_item}' has been added to the cart.\n")
        elif action == 2:
            # The program should display all of the items and prices in the shopping cart, one per line.
            # The program should also display the number associated with each item in the list,
            # beginning with 1. 

            # SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
            # Added better formatting by aligning the item number, item name and prices.
            item_num = "Item No."
            item_value = "Item"
            item_price = "Price"
            print("==================================")
            print(f"{item_num: <10}{item_value: ^10}{item_price: >10}")
            print("----------------------------------")
            i = 0
            for i in range(len(items)):
                number = i + 1
                print(f"{number: <10}{items[i]: ^10} \t${prices[i]:.2f}")
            print("----------------------------------")
            print()
        elif action == 3:
            # The user types in the number of the item they want to remove and the item is removed
            # from the list.
            remove_item = int(input("Which item would you like to remove? "))
            remove_item -= 1
            
            # Make sure that the index is within the bounds of the current list.
            if remove_item >= 0 and remove_item < len(items):
                # Both the item name and price are removed from their respective lists.
                items.remove(items[remove_item])
                prices.remove(prices[remove_item])
                print("Item removed.\n")
            # If the index is outside the bounds of the list, you should not attempt to remove it,
            # but rather, display a message informing the user that they have made an invalid choice.
            else:
                print("CAUTION: The item is not on the list. Please try again.\n")
        elif action == 4:
            # The program should iterate through each item in the list and add up the prices
            # and then display the total amount to the user.

            total = 0
            for i in range(len(items)):
                total += prices[i]
            # Whenever prices are displayed, they should be shown to two decimal places.
            print(f"The total price of the items in the shopping cart is ${total:.2f}\n")
        else:
            print("Sorry! The number you entered is incorrect. Please try again.\n")
    else:
        # SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
        # Added better formatting by aligning the item numbers, item names and prices.
        # Added additional transaction by asking for payment and compute the change. 
        item_num = "Item No."
        item_value = "Item"
        item_price = "Price"
        item_total = "Total"
        
        i = 0

        print("__________________________________")
        print("     Thank you for shopping!")
        print("==================================")
        print(f"{item_num: <10}{item_value: ^10}{item_price: >10}")
        print("----------------------------------")
        for i in range(len(items)):
            number = i + 1
            print(f"{number: <10}{items[i]: ^10} \t${prices[i]:.2f}")
        print("----------------------------------")
        print(f"{item_total}: \t\t\t${sum(prices):.2f}")

        payment = float(input("Payment:\t\t$"))
        change = payment - sum(prices)
        print("----------------------------------")
        print(f"Change:\t\t\t${change:.2f}") 
        print()
    
        
     