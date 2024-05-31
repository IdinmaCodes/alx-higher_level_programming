<<<<<<< HEAD
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
=======
#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if char >= "a" and char <= "z":
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
>>>>>>> ea9c67427e3b45ac7bad0fbbea8dab945b2856c4
