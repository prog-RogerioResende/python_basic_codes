'''
Program that reads two grades of a student 
and calculates the average obtained. The program 
will then display a message according to the average:
1 - AVERAGE BELOW 5.0 (FAILED);
2 - AVERAGE BETWEEN 5.0 AND 6.9 (RECOVERY);
3 - AVERAGE 7.0 OR ABOVE (PASSED).
'''

print('\033[0;036m-=\033[m' * 20)
print('\033[0;036mSTUDENT GRADE AVERAGE.\033[m')
print('\033[0;036m-=\033[m' * 20)

grade1 = float(input('Enter the grade of the first exam: '))
grade2 = float(input('Enter the grade of the second exam: '))
average = (grade1 + grade2) / 2

if average < 5.0:
    print(f'Your final average was \033[0;031m{average:.2f}\033[m.')
    print('You have \033[0;031mFAILED.\033[m')
elif 7 > average >= 5.0:
    print(f'Your final average was \033[0;033m{average:.2f}\033[m.')
    print('\033[0;033mIn recovery.\033[m')
else:
    print(f'Your final average was \033[0;032m{average:.2f}\033[m.')
    print('Congratulations, you have \033[0;032mPASSED!!!\033[m.')
