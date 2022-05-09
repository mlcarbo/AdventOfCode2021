#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        inputName = sys.argv[1]
    else:
        inputName = "input.txt"

    with open(inputName, "r") as stream:
        increases = -1
        prevSum = 0
        currSum = 0
        window = []
        for line in stream:
            line = line.rstrip()
            line = int(line)
            window.append(line)
            if len(window) < 3:
                continue
            if len(window) > 3:
                window.pop(0)
            currSum = sum(window)
            if currSum > prevSum:
                increases += 1

            prevSum = currSum
    print(increases)

if __name__ == "__main__":
    main()
