"""
File: w09_List.py
Author: Leah Tajon

Overview: Practice working with lists.

Assignment:
Ask the user for the names of their friends and append
them to a list. Then, display each of the friends in the list.
You should stop asking for friends when the user types "end".
"""
friends = []

add_friend = ""
while add_friend.lower() != "end":
    add_friend = input("Type the name of a friend: ")
    
    if add_friend.lower() != "end":
        friends.append(add_friend)

for friend in friends:
    print(friend)
