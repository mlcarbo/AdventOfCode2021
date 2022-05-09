#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        inputName = sys.argv[1]
    else:
        inputName = "input.txt"
    print(inputName)
    with open(inputName, "r") as stream:
        increases = -1
        currNum = 0
        for line in stream:
            line = line.rstrip()
            line = int(line)
            if (line > currNum):
                increases += 1
                print(f"{line} > {currNum}")
            currNum = line


    print(increases)

if __name__ == "__main__":
    main()
