#!/usr/bin/python3
def uppercase(str):
    letter = list(str)
    for i in range(len(letter)):
        if (ord(letter[i]) > 96 and ord(letter[i]) < 123):
            letter[i] = chr(ord(letter[i]) - 32)
    print("{}".format(("").join(letter)))
