'''
Program that uses a number converter 
to transform numbers into binary, 
octal, and hexadecimal formats.
'''

print('-=' * 20)
print('\033[0;32mNUMBER CONVERTER\033[m')
print('-=' * 20)

num = int(input('Enter an integer: '))

print('\033[0;33mPress 1 for Binary\033[m')
print('\033[0;34mPress 2 for Octal\033[m')
print('\033[0;35mPress 3 for Hexadecimal\033[m')

convert = int(input('Choose the desired conversion: '))

if convert == 1:
    binary = bin(num)[2:]
    print(f'The number \033[0;33m{num}\033[m in binary is \033[0;33m{binary}\033[m.')
elif convert == 2:
    octal = oct(num)[2:]
    print(f'The number \033[0;34m{num}\033[m in octal is \033[0;34m{octal}\033[m.')
elif convert == 3:
    hexadecimal = hex(num)[2:]
    print(f'The number \033[0;35m{num}\033[m in hexadecimal is \033[0;35m{hexadecimal}\033[m.')
else:
    print('\033[1;31mInvalid option selected!\033[m')
