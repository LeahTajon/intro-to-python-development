"""
File: w07_Team.py
Author: Leah Tajon

Project: Guess My Title Game
Overview: In my Guess My Number game the computer picks a magic number, and
then the user tries to guess it. After each guess, the computer tells the user
to guess "higher" or "lower" until they guess the magic number.
"""
import random

random_num = random.randint(1, 100)
guess_num = int(input("What is your guess? "))

while random_num != guess_num:
    if random_num > guess_num:
        print("Higher\n")
    elif random_num < guess_num:
        print("Lower\n")
    guess_num = int(input("What is your guess? "))

print("You guessed it!\n")