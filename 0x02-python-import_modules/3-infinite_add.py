#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tot = 0
    for e in range(1, len(argv)):
        tot += int(argv[e])
    print("{}".format(tot))

