"""
File: w03_Prove_MealCalculator.py
Author: Leah Tajon

Instructions:
Compute the price of a meal as follows by asking for the price of child and adult meals, 
the number of each, and then the sales tax rate. Use these values to determine the total price
of the meal. Then, ask for the payment amount and compute the amount of change to give back
to the customer.
"""
child_meal = float(input("\nWhat is the price of child's meal? "))  # Enter the price of child's meal
adult_meal = float(input("What is the price of an adult's meal? ")) # Enter the price of adult's meal
child_num = int(input("How many children are there? "))     # Enter number of children
adult_num = int(input("How many adults are there? "))       # Enter number of adult
tax_rate = float(input("What is the sales tax rate? "))     # Enter value of sales tax rate

tot_price_child = child_meal * child_num    # Compute the total price of child's meal
tot_price_adult = adult_meal * adult_num    # Compute the total price of adult's meal

subtotal = tot_price_child + tot_price_adult    # Compute the Subtotal
format_subtotal = "{:.2f}".format(subtotal)     # Subtotal Formatted --> For display only
sales_tax = (subtotal * tax_rate) / 100         # Compute the Sales tax

#STRETCH --> ADD 10% SERVICE CHARGE
service_charge = .10
tot_service_charge = subtotal * service_charge

total_price = subtotal + sales_tax + tot_service_charge    # Compute the Total Price

print("\nSubtotal: $" + format_subtotal)                    # Display the Subtotal
print(f"Sales Tax: ${round(sales_tax,2)}")                  # Display the total sales tax
print(f"Service Charge: ${tot_service_charge:.2f}")         # Display the amount of service charge
print(f"Total: ${round(total_price,2)}")                    # Display the total price

payment = float(input("\nWhat is the payment amount? ")) # Enter the payment amount

change = payment - total_price          # Compute the Change
print(f"Change: ${round(change, 2)}\n") # Display the amount of change

