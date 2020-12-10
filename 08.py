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
        return int(instruction[4:]), 1, False, instruction
    elif instruction.startswith('jmp'):
        return 0, int(instruction[4:]), True, instruction

    return 0, 1, True, instruction

def modify_instruction(inst):
    if inst.startswith('nop'):
        return 'jmp' + inst[3:]
    elif inst.startswith('jmp'):
        return 'nop' + inst[3:]
    return inst

def process(instructions, iteration):
    run = []
    accum = 0
    pc = 0
    while(pc not in run and pc != len(instructions)):
        add, adv, is_suspect, inst_run = handle(instructions[pc])
        if is_suspect and iteration == 0:
            add, adv, is_suspect, inst_run = handle(modify_instruction(instructions[pc]))
            iteration -= 1
        elif is_suspect:
            iteration -= 1
        run.append(pc)
        accum += add
        pc += adv
    return accum, pc

def search(instructions):
    pc = 0
    accum = 0
    iteration = 0
    while(pc != len(instructions)):
        accum, pc = process(instructions, iteration)
        iteration += 1
    return accum

if __name__ == "__main__":
    input_file = get_input_file();
    instructions = read_input(input_file)
    print("08 ---> " + str(search(instructions)))
