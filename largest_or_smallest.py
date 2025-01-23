"""
Program that reads three numbers and 
identifies the smallest and the largest
"""

print('-=' * 20)
print('WHICH NUMBER IS THE LARGEST? AND WHICH IS THE SMALLEST?')
print('-=' * 20)

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

# Check which is the smallest
smallest = n1
if n2 < n1 and n2 < n3:
    smallest = n2
if n3 < n1 and n3 < n2:
    smallest = n3

# Check which is the largest
largest = n1
if n2 > n1 and n2 > n3:
    largest = n2
if n3 > n1 and n3 > n2:
    largest = n3
print(f'The smallest value entered was {smallest}.')
print(f'The largest value entered was {largest}.')
