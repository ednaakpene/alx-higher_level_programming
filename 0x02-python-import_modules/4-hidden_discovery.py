#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    na = dir()
    for e in range(0, len(na)):
        if na[:2] != "__":
            print("{:s}".format(na[e]))
