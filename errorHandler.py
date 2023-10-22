import numpy as np
import sys
import os.path


def error_handling() -> list[list[int]]:
    if len(sys.argv) != 2:
        print(f"Error, there should be only one argument got {len(sys.argv) - 1}")
        exit(84)
    if not os.path.isfile(sys.argv[1]):
        print("The argument should be a file")
        exit(84)
    contents = []
    with open(sys.argv[1]) as f:
        contents = (f.readlines())
    if (len(contents) != 9):
        print(f"Error, number of line different than 9, got {len(contents)}")
        exit(84)
    splitted_contents = []
    for line in contents:
        splitted_line = line.split(' ')
        if len(splitted_line) != 9:
            print(f"Error, number of columns different than 9, got {len(splitted_line)}")
            exit(84)
        splitted_contents.append(splitted_line)
    board = [[int(i) for i in y] for y in splitted_contents]
    for i in board:
        for y in i:
            if y < 0 or y > 9:
                print(f"Error, numbers should be between 0 and 9 got {y}")
                exit(84)
    return board
