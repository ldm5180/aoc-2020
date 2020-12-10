#!/usr/bin/env python

#!/usr/bin/env python3

import os
import sys
import re
import pprint

def get_input_file():
    return os.path.basename(os.path.abspath(sys.argv[0])).strip(".py") + ".in"

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines();
        return data;

def handle(instruction):
    if instruction.startswith('acc'):
        return int(instruction[4:]), 1
    elif instruction.startswith('jmp'):
        return 0, int(instruction[4:])

    return 0, 1

def process(instructions):
    run = []
    accum = 0
    pc = 0
    while(pc not in run):
        add, adv = handle(instructions[pc])
        run.append(pc)
        accum += add
        pc += adv
    return accum

if __name__ == "__main__":
    input_file = get_input_file();
    instructions = read_input(input_file)
    print("08 ---> " + str(process(instructions)))
