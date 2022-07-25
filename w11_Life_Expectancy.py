"""
File: w11_Life_Expectancy.py
Author: Leah Tajon

Overview:
For this assignment you will write a program to analyze a dataset
containing information about life expectancies over the years throughout
the countries of the world.
"""
# 01    | Download the dataset
# 02    | Load the dataset in your Python program
import code


with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)

    entities = []
    codes = []
    years = []
    expectancies = []

    for file in life_expectancy:        # 03    | Iterate through the data line by line
        file_split = file.split(",")    # 04    | Split each line into parts
        file_strip = file.strip()
        
        
        entities.append(file_split[0])
        codes.append(file_split[1])
        years.append(file_split[2])
        expectancies.append(float(file_split[3]))

    print(f"The overall max life expectancy is: {max(expectancies)}") # 05  | Find the highest value for life expectancy
    print(f"The overall min life expectancy is: {min(expectancies)}") # 06  | Find the lowest value for life expectancy
    

        