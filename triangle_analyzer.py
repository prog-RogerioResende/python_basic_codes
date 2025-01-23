"""
Program that reads the lengths of three line segments 
and tells the user whether they can form a triangle or not.
"""

print('-=' * 20)
print('TRIANGLE ANALYZER')
print('-=' * 20)

side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))

if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    print('With these sides, it is possible to form a triangle.')
else:
    print('With these sides, it is not possible to form a triangle.')
