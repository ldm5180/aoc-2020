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

if __name__ == "__main__":
    input = [0] + read_input(get_input_file())
    diffs = adjacent_diffs(input)
    print("10 ---> " + str(answer(diffs)))
