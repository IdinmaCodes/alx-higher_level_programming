#!/usr/bin/python
def uppercase(str):
    if str == None:
        print("None")
    else:
        for character in str:
            if ord(character) >=97 and ord(character) <= 122:
                character = chr(ord(character) - 32)
            print(f"{character}", end="")
        print()

uppercase("HABEEB")
#str = "habeeb"
#print("HABEEB")
