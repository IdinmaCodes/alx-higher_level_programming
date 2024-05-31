#!/usr/bin/python3
if __name__ == "__main__":
    def infinite_add():
        import sys
        sum = 0
        for i in sys.argv[1:]:
            sum += int(i)
        print("{}\n".format(sum))
    infinite_add()
