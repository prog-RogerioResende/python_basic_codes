"""
Program that calculates the ticket price by 
asking for the distance in km of a trip. It will charge €0.50 
per km for trips up to 200 km and €0.45 for longer trips.
"""

print('-=' * 20)
print('WHERE ARE WE TRAVELING TO?')
print('-=' * 20)

dist = float(input("Enter the distance of your trip in km: "))

if dist > 200:
    price = dist * 0.45
    print(f'Your trip will cover a distance of {dist} km.')
    print(f'The cost of the trip is €{price:.2f}.')
else:
    price = dist * 0.5
    print(f'Your trip will cover a distance of {dist} km.')
    print(f'The cost of the trip is €{price:.2f}.')
