#!/usr/bin/env python3

import os
import sys
from copy import deepcopy

def get_input_file():
    return os.path.basename(os.path.abspath(sys.argv[0])).strip(".py") + ".in"

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines();
        for i, line in enumerate(data):
            data[i] = list(line.strip())
        return data

def get_line_len(input):
    return len(input[0])

def get_num_adjacent_filled(row_num, col_num, input):
    neighbors = [ (row_num - 1, col_num - 1), (row_num - 1, col_num), (row_num - 1, col_num + 1),
                  (row_num, col_num - 1),                         (row_num, col_num + 1),
                  (row_num + 1, col_num - 1), (row_num + 1, col_num), (row_num + 1, col_num + 1) ]
    count = 0
    for r,c in neighbors:
        if r >= 0 and r < len(input) and c >= 0 and c < get_line_len(input):
            #print(str(r) + ',' + str(c))
            #print("Length of line: " + str(len(
            if input[r][c] == '#':
                count += 1
    return count

def fill_seats(input):
    is_changed = False
    output = deepcopy(input)
    for row_num, row in enumerate(input):
        for col_num, seat in enumerate(row):
            num_adjacent_filled = get_num_adjacent_filled(row_num, col_num, input)
            if num_adjacent_filled == 0 and seat == 'L':
                output[row_num][col_num] = '#'
                is_changed = True
            elif num_adjacent_filled >= 4 and seat == '#':
                output[row_num][col_num] = 'L'
                is_changed = True
    return is_changed, output

def count_filled(input):
    filled = 0
    for row in input:
        filled += row.count('#')
    return filled

def part1():
    input = read_input(get_input_file())
    row_len = get_line_len(input)
    while (is_changed):
        is_changed, input = fill_seats(input)
        if not is_changed:
            break
    filled = count_filled(input)
    print("11 ---> " + str(filled))

def part2():
    pass

if __name__ == "__main__":
    part1()
    part2()
