"""
Program that reads any year and
determines if it is a leap year or not
"""

from datetime import date


print('-=' * 20)
print('LEAP YEAR')
print('-=' * 20)

year = int(input('Which year do you want to analyze? Enter 0 to analyze the current year: '))

if year == 0:
    year = date.today().year
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f'The year {year} is a leap year!')
else:
    print(f'The year {year} is not a leap year!')
