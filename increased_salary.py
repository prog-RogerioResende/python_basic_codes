"""
Program that asks for the employee's salary 
and calculates the value of their raise. For salaries above 
€1250, it calculates a 10% raise. For those equal to or below, 
the raise is 15%.
"""

print('-=' * 20)
print('SALARY WITH INCREASE')
print('-=' * 20)

salary = float(input('Enter the salary: '))

if salary > 1250:
    new_salary = salary + (salary * 0.1)
    print(f'Your previous salary was €{salary:.2f}.')
    print(f'With the raise, your new salary is €{new_salary:.2f}.')
else:
    new_salary = salary + (salary * 0.15)
    print(f'Your previous salary was €{salary:.2f}.')
    print(f'With the raise, your new salary is €{new_salary:.2f}.')
