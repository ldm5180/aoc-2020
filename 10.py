#!/usr/bin/env python3

import os
import sys

def get_input_file():
    return os.path.basename(os.path.abspath(sys.argv[0])).strip(".py") + ".in"

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines();
        num_data = [ int(x.strip()) for x in data ]
        num_data.sort()
        return num_data

def adjacent_diffs(input):
    res = []
    for i in range(len(input) - 1):
        res.append(input[i+1] - input[i])
    return res

def answer(diffs):
    ones = diffs.count(1)
    threes = diffs.count(3) + 1
    return ones * threes

def run_math(diffs):
    runs_of_5 = 0
    runs_of_4 = 0
    runs_of_3 = 0
    runs_of_2 = 0
    while len(diffs) > 1:
        s5 = diffs[:min([len(diffs), 5])]
        s4 = diffs[:min([len(diffs), 4])]
        s3 = diffs[:min([len(diffs), 3])]
        s2 = diffs[:min([len(diffs), 2])]
        if s5.count(1) == 5:
            runs_of_5 += 1
            diffs = diffs[5:]
        if s4.count(1) == 4:
            runs_of_4 += 1
            diffs = diffs[4:]
        elif s3.count(1) == 3:
            runs_of_3 += 1
            diffs = diffs[3:]
        elif s2.count(1) == 2:
            runs_of_2 += 1
            diffs = diffs[2:]
        else:
            diffs = diffs[1:]
    return (2**runs_of_2) * (4**runs_of_3) * (7**runs_of_4)

if __name__ == "__main__":
    input = [0] + read_input(get_input_file())
    diffs = adjacent_diffs(input)
    print("10 ---> " + str(answer(diffs)))
    part2 = run_math(diffs)
    print("part 2 ---> " + str(part2))
