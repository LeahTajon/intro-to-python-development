"""
File: w11_Open_Files.py
Author: Leah Tajon

Overview: Practice Opening Files

Assignment:
Have your program open the file, read though it line by line,
strip off leading and trailing whitespace and display each book to the screen
"""

with open("books.txt") as bom:
    for book_name in bom:
        bom_strip = book_name.strip()
        bom_split = book_name.split()

        print(f"{bom_strip}")
        #print(f"{bom_split}")
        