"""
File: w10_Multiple_Lists.py
Author: Leah Tajon

Overview: Create multiple lists.
"""

# Create two lists, one for the names of the bank accounts, and one
# for the balances.
accounts = []
balances = []

# Ask the user for the name of the bank account and then for its current
# balance. Keep looping until the user types "quit" for the name of an account.
# For each one, add the name and the balance to the appropriate list.
print("\nEnter the names and balances of bank accounts (type: quit when done)")

acct_type = ""

while acct_type.lower() != 'quit':
    acct_type = str(input("What the name of this account? "))

    if acct_type.lower() != 'quit':
        acct_balance = float(input("What is the balance? $"))

        accounts.append(acct_type)
        balances.append(acct_balance)

# Loop through the lists using an index and display the name of the account
# with the balance next to it.
amount = 0
print("\nAccount information:")
for i in range(len(accounts)):
    print(f"{i}. {accounts[i]} - {balances[i]:.2f}")

    amount += balances[i]

# Compute and display the total balance in all of the accounts and
# the average balance.
ave = amount / len(accounts)

print(f"\nTotal: ${amount:.2f}")
print(f"Average: ${ave:.2f}")



   