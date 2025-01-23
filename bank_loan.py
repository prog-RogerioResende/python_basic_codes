'''
Program to approve or deny a bank loan.
It should ask for the house value, the buyer's salary, 
and in how many years they want to pay off the loan. 
If the monthly installment exceeds 30% of the salary, 
the loan will be denied.
'''

print('-=' * 20)
print('BANK LOAN')
print('-=' * 20)

house_value = float(input('Enter the house value: €'))
salary = float(input('Enter the buyer\'s salary: €'))
years = int(input('In how many years do you want to pay off the house? '))
salary_limit = salary * 0.3
months = years * 12
installment = house_value / months

if installment <= salary_limit:
    print('\033[0;32mLoan Approved!\033[m')
    print(f'To pay for a house worth \033[0;32m€{house_value:.2f}\033[m over \033[0;32m{years}\033[m years', end='')
    print(f', the monthly installment will be \033[0;32m€{installment:.2f}\033[m.')
else:
    print('\033[0;31mLoan Denied!\033[m')
