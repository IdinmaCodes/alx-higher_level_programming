#!/usr/bin/python3
#for num in range(100):
#    if num < 99:
#        print(f"{num:02,}".format(num=num), end=", ")
#    else:
#        print(f"{num:02}".format(num=num))

for i in range(0, 100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
