"""
File: w13_Basic_Functions.py
Author: Leah Tajon

Overview: This checkpoint is designed to help you practice writing basic functions.0
"""

# 01    | display_regular - Receives a string and prints it out, exactly as received.
def display_regular(message):
    msg = message
    return msg

# 02    | display_uppercase - Receives a string, converts it to upper case, and then prints it out.
def display_uppercase(message2):
    msg2 = message2.upper()
    return msg2

# 03    | display_lowercase - Receives a string, converts it to lower case, and then prints it out.
def display_lowercase(message3):
    msg3 = message3.lower()
    return msg3

input_msg = input('What is your message? ')

regular_msg = display_regular(input_msg)
uppercase_msg = display_uppercase(input_msg)
lowercase_msg = display_lowercase(input_msg)

print(regular_msg)
print(uppercase_msg)
print(lowercase_msg)