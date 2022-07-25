"""
File: w13_Wind_Chill.py
Author: Leah Tajon

Assignment: Write a program that asks the user for a temperature and then shows
the wind chill values for various wind speeds at that temperature.
"""

# 01 | Write a function to calculate and return the wind chill based 
#      on a given temperature and wind speed.

def calc_wind_chill(t, v):
    wind_chill = 35.74 + 0.6215 * t - 35.75 * (v ** .16) + 0.4275 * t * (v ** .16)
    return wind_chill

# 02 | Write a function to convert from Celsius to Fahrenheit.
#      The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

def convert_temp(c):
    f = c * 9 / 5 + 32
    return f

# 03 | Allow the user to enter the temperature in Celsius to Fahrenheit. 
#      If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

temp = float(input('What is the temperature? '))
degree = input('Fahrenheit or Celsius (F/C)? ')
print()

# 04 | Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and
#      calculate and display the wind chill for each of these wind speeds.

if degree.lower() == 'c' or degree.lower() == 'celsius':
    temp_fah = convert_temp(temp)
    speed_celcius = 0
    for x in range(0, 12):
        speed_celcius += 5
        wind_chill_cel = calc_wind_chill(temp_fah, speed_celcius)

# 05 | Display the wind chill value to 2 decimals of precision.
        print(f'At temperature {temp_fah:.1f}F, and wind speed {speed_celcius} mph, the windchill is: {wind_chill_cel:.2f}F')
elif degree.lower() == 'f' or degree.lower() == 'fahrenheit':
    speed_fah = 0
    for y in range(0, 12):
        speed_fah += 5
        wind_chill_fah = calc_wind_chill(temp, speed_fah)

        print(f'At temperature {temp:.1f}F, and wind speed {speed_fah} mph, the windchill is: {wind_chill_fah:.2f}F')
else:
    print('Please type F or C only.')










