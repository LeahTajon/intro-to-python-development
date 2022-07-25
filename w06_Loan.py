"""
File: w06_Checkpoint_Loan.py
Author: Leah Tajon

Overview: For this assignment, you will implement a simplistic system to determine
if a user can qualify for a loan.
"""

# First, ask for a rating from 1-10 on the following:
# How large is the loan?
# How good is your credit history?
# How high is your income?
# How large is your down payment?
print()
print('\nRate the following questions from 1 - 10.')
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
downpayment = int(input('How large is your down payment? '))

# First, check if the loan size is at least 5. If it is, use the following rules:
# If the credit history and income are both at least 7, then the decision is "yes".
# If either the credit history or income is at least 7, then check if the down payment
# is at least 5, if it is, the decision is "yes", if not, the decision is "no"
# Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        print("Yes")
    elif credit_history >= 7 or income >= 7:
        if downpayment >= 5:
            print("Yes")
        else:
            print("No")
# Otherwise (if the loan is not 5 or greater), use these rules:
# If the credit is less than 4, then the decision is "no"
# Otherwise, check the following:
# If either the income or the down payment is at least, the decision is "yes"
# If both the income and the down payment are at least 4, then the answer is "yes"
# Otherwise, the decision is "no"
else:
    if credit_history < 4:
        print("No")
    else:
        if income >= 7 or downpayment >= 7:
            print("Yes")
        elif income >= 7 and downpayment >= 7:
            print("Yes")
        else:
            print("No")

