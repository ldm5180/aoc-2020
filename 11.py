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

def is_filled(input, r, c, next_row, next_col):
    while(True):
        r += next_row
        c += next_col
        if r >= 0 and r < len(input) and c >= 0 and c < get_line_len(input):
            if input[r][c] == 'L':
                return False
            elif input[r][c] == '#':
                return True
        else:
            return False

def get_line_len(input):
    return len(input[0])

def get_num_adjacent_filled(row, col, input):
    neighbors = [ (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                  (row, col - 1),                         (row, col + 1),
                  (row + 1, col - 1), (row + 1, col), (row + 1, col + 1) ]
    count = 0
    for r,c in neighbors:
        if r >= 0 and r < len(input) and c >= 0 and c < get_line_len(input):
            #print(str(r) + ',' + str(c))
            #print("Length of line: " + str(len(
            if input[r][c] == '#':
                count += 1
    return count

def get_num_seen_filled(row, col, input):
    count = 0
    count += is_filled(input, row, col, -1, -1)
    count += is_filled(input, row, col, -1, 0)
    count += is_filled(input, row, col, -1, 1)
    count += is_filled(input, row, col, 0, -1)
    count += is_filled(input, row, col, 0, 1)
    count += is_filled(input, row, col, 1, -1)
    count += is_filled(input, row, col, 1, 0)
    count += is_filled(input, row, col, 1, 1)
    return count

def fill_seats(input, look_deeply = False, num_next_to = 4):
    is_changed = False
    output = deepcopy(input)
    for row_num, row in enumerate(input):
        for col_num, seat in enumerate(row):
            if not look_deeply:
                num_adjacent_filled = get_num_adjacent_filled(row_num, col_num, input)
            else:
                num_adjacent_filled = get_num_seen_filled(row_num, col_num, input)

            if num_adjacent_filled == 0 and seat == 'L':
                output[row_num][col_num] = '#'
                is_changed = True
            elif num_adjacent_filled >= num_next_to and seat == '#':
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
    while (True):
        is_changed, input = fill_seats(input)
        if not is_changed:
            break
    filled = count_filled(input)
    print("11.1 ---> " + str(filled))

def part2():
    input = read_input(get_input_file())
    row_len = get_line_len(input)
    while (True):
        is_changed, input = fill_seats(input, True, 5)
        if not is_changed:
            break
    filled = count_filled(input)
    print("11.2 ---> " + str(filled))


if __name__ == "__main__":
    part1()
    part2()
