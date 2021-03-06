#!/usr/bin/env python3

import os
import sys
import pprint

def get_input_file():
    return os.path.basename(os.path.abspath(sys.argv[0])).strip(".py") + ".in"

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines();
        return data;

def preamble_and_data(input, size):
    p = input[:size]
    d = input[size:]
    return p, d

def check(preamble, element):
    for i in preamble:
        if element - i in preamble:
            return True
    return False

def find_invalid(input, preamble_size):
    while(len(input) > preamble_size + 1):
        preamble, data = preamble_and_data(input, preamble_size)
        if not check(preamble, data[0]):
            print("09 ---> " + str(data[0]))
            return data[0]
        input = input[1:]
    return None

def find_contiguous(input, element):
    contiguous_len = 2
    index = 0
    while(contiguous_len + index < len(input)):
        sublist = input[index:index+contiguous_len]
        if sum(sublist) == element:
            return min(sublist) + max(sublist)
        contiguous_len += 1
        if contiguous_len + index >= len(input):
            index += 1
            contiguous_len = 2
    return 0

if __name__ == "__main__":
    preamble_size = 25
    raw_input = read_input(get_input_file())
    input = [ int(x.strip()) for x in raw_input ]
    invalid = find_invalid(input, preamble_size)
    print("part 2 ---> " + str(find_contiguous(input, invalid)))
