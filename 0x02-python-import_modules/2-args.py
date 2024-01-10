#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tot = len(argv) - 1
    if tot < 1:
        print("{} arguments:".format(tot))
    elif tot == 1:
        print("{} argument:".format(tot))
    else:
        print("{} arguments:".format(tot))
    for e in range(tot):
        print("{}: {:s}".format(e + 1, argv[e + 1]))
