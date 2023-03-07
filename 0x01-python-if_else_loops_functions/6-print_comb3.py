#!/usr/bin/python3
for number in range(0, 10):
    for number2 in range(0, 10):
        if number2 <= number:
            continue
        elif number == 8 and number2 == 9:
            print("{:d}{:d}".format(number, number2))
        else:
            print("{:d}{:d}".format(number, number2), end=', ')
