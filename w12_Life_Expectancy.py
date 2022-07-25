"""
File: w12_Prove.py
Author: Leah Tajon

Overview:
For this assignment you will write a program to analyze a dataset
containing information about life expectancies over the years throughout
the countries of the world.
"""
with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)

    max_expectancy = -1
    max_country = ""

    min_expectancy = 99999999999
    min_country = ""

    year_life1 = 0
    year_life2 = 99999999999

    sum = 0
    count = 0

    max_life = -1
    min_life = 99999999999
    
    # This allows the user to type in a year
    input_year = int(input('\nEnter the year of interest: '))

    max_life_country = -1
    min_life_country = 99999999999

    sum2 = 0
    count2 = 0

    yr_life1 = 0
    yr_life2 = 99999999999

    # SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
    # Allow the user to type in a country, then show the minimum, maximum, and average
    # life expectancy for that country
    
    # This allows the user to type in a country
    input_country = input('Enter the country of interest: ')

    for file in life_expectancy:
        part = file.split(",")
        clean = file.strip()

        entity = part[0]
        code = part[1]
        year = int(part[2])
        expectancy = float(part[3])

        # This condition returns the year and country that has
        # the highest life expectancy in the data set
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_country = entity
            year_life1 = year
        
        # This condition returns the year and country that has
        # the lowest life expectancy in the data set
        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_country = entity
            year_life2 = year

        # This condition finds the country with the minimum and the one with
        # the maximum life expectancies for that year.
        # It also finds the average life expectancy for that year.
        if input_year == year:
            count += 1
            sum += expectancy

            if expectancy > max_life:
                max_life = expectancy
                max_country = entity
               
            if expectancy < min_life:
                min_life = expectancy
                min_country = entity
        
        # This condition finds the minimum, maximum, and average life expectancy for
        # the desired country.
        if input_country.lower() == entity.lower():
            count2 += 1
            sum2 += expectancy

            if expectancy > max_life_country:
                max_life_country = expectancy
                yr_life1 = year

            if expectancy < min_life_country:
                min_life_country = expectancy
                yr_life2 = year

    # Displays the years and countries that have the minimum and maximum life expectancy in the data set.
    print(f"\nThe overall max life expectancy is: {max_expectancy} from {max_country} in {year_life1}")
    print(f"The overall min life expectancy is: {min_expectancy} from {min_country} in {year_life2}")

    print(f"\nFor the year {input_year}:")
    
    ave = sum / count

    # Displays the average life expectancy for the selected year. Also the country with the minimum and maximum 
    # life expectancies for the selected year.
    print(f"The average life expectancy across all countries was {ave:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life}")
    print(f"The min life expectancy was in {min_country} with {min_life}")

    print(f"\nIn {input_country}:")

    # SHOWING CREATIVITY AND EXCEEDING REQUIREMENTS
    # Allow the user to type in a country, then show the minimum, maximum, and average
    # life expectancy for that country

    ave_country = sum2 / count2

    # Displays the average, maximum and minimum life expectancy for the selected country.
    print(f"The average life expectancy is: {ave_country:.2f}")
    print(f"The max life expectancy is {max_life_country} in {yr_life1}")
    print(f"The min life expectancy is {min_life_country} in {yr_life2}\n")    


