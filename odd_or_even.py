"""
Program that reads an integer and determines if 
it is even or odd
"""

print('-=' * 20)
print('EVEN OR ODD?')
print('-=' * 20)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f'The chosen number is {num}, and it is even.')
else:
    print(f'The chosen number is {num}, and it is odd.')
