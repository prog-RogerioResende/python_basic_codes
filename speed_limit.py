'''
Program that simulates a car's speed camera.
If the car exceeds 80 km/h, you will be fined.
The fine will cost €7 per km/h above the limit
'''

print('-=' * 20)
print('SPEED LIMIT')
print('-=' * 20)

speed = int(input("How fast was your car?"))

if (speed > 80):
    ticket = (speed - 80) * 7
    print("You have been fined! The limit is 80 km/h.")
    print(f"Your speed was {speed} km/h.")
    print(f"You must pay €{ticket:.2f} fine for speeding.")
else:
    print(f"Your speed was {speed} km/h.")
    print("It's within limits.")
