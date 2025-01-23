'''
Program that reads the birth year of a young person 
and informs:
1 - If they still need to enlist;
2 - If it is time to enlist;
3 - If the enlistment deadline has passed.
'''

from datetime import date


print('\033[0;032m-=\033[m' * 25)
print('\033[0;032mMILITARY ENLISTMENT\033[m')
print('\033[0;032m-=\033[m' * 25)

current_year = date.today().year  # Gets the current year from the library

print('If you are female, press [1].')
print('If you are male, press [2].')

gender = int(input('Choose one of the options above: '))

if gender == 1:
    print('Military enlistment is not required!')
elif gender == 2:
    year_of_birth = int(input('Enter your year of birth: '))
    age = current_year - year_of_birth
    if age < 18:
        years_to_enlist = 18 - age
        print(f'Your age is \033[0;032m{age}\033[m years.')
        print(f'You need to enlist in \033[0;033m{years_to_enlist}\033[m years.')
    elif age == 18:
        print(f'Your age is \033[0;032m{age}\033[m years.')
        print('\033[0;034mPlease visit a military post for enlistment.\033[m')
    else:
        overdue_years = age - 18
        print(f'Your age is \033[0;032m{age}\033[m years.')
        print('\033[0;031mATTENTION!!!\033[m')
        print(f'You should have enlisted \033[0;031m{overdue_years}\033[m years ago.')
else:
    print('Invalid option. Please try again.')
