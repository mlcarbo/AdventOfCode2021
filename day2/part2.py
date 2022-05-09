#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) > 1:
        inputFile = sys.argv[1]
    else:
        inputFile = "input.txt"

    with open(inputFile) as stream:
        aim = 0
        depth = 0
        horiz = 0
        for line in stream:
            line = line.rstrip()
            line = line.split()
            if line[0].lower() == "up":
                aim -= int(line[1])
            elif line[0].lower() == "down":
                aim += int(line[1])
            elif line[0].lower() == "forward":
                horiz += int(line[1])
                depth += int(line[1]) * aim
                print(f'horiz: {horiz} depth: {depth} aim: {aim}')

    multPos = depth * horiz
    print(multPos)


if __name__ == "__main__":
    main()
