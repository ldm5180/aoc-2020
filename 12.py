#!/usr/bin/env python3

import os
import sys
from copy import deepcopy

def get_input_file():
    return os.path.basename(os.path.abspath(sys.argv[0])).strip(".py") + ".in"


def read_input(filename):
    with open(filename, 'r') as f:
        data = f.readlines();
        return data


def change_heading(heading, count):
    heading += count
    heading %= 360
    if heading == 0:
        return 'N', heading
    elif heading == 90:
        return 'E', heading
    elif heading == 180:
        return 'S', heading
    else:
        return 'W', heading


def move(heading, ew, ns, instruction, count, ew_mult = 1, ns_mult = 1):
    if instruction == 'N':
        return heading, ew, ns + count
    elif instruction == 'S':
        return heading, ew, ns - count
    elif instruction == 'E':
        return heading, ew + count, ns
    else:
        return heading, ew - count, ns


def update(heading, ew, ns, instruction, count):
    if instruction == 'R':
        instruction,heading = change_heading(heading, count)
        return heading, ew, ns
    elif instruction == 'L':
        instruction,heading = change_heading(heading, -count)
        return heading, ew, ns
    elif instruction == 'F':
        instruction,heading = change_heading(heading, 0)

    heading, ew, ns = move(heading, ew, ns, instruction, count)

    return heading, ew, ns


def change_mult(instruction, count, ew_mult, ns_mult):
    if instruction == 'N':
        return ew_mult, ns_mult + count
    elif instruction == 'S':
        return ew_mult, ns_mult - count
    elif instruction == 'E':
        return ew_mult + count, ns_mult
    else:
        return ew_mult - count, ns_mult


def move2(ew, ns, count, ew_mult, ns_mult):
    ew += count * ew_mult
    ns += count * ns_mult
    return ew, ns


def change_heading2(heading, count, ew_mult, ns_mult):
    if count < 0:
        count = 360 + count
    if count == 90:
        ew_mult, ns_mult = (ns_mult, -ew_mult)
    elif count == 180:
        ew_mult, ns_mult = (-ew_mult, -ns_mult)
    elif count == 270:
        ew_mult, ns_mult = (-ns_mult, ew_mult)
    return heading, ew_mult, ns_mult

def update2(heading, ew, ns, ew_mult, ns_mult, instruction, count):
    if instruction == 'R':
        heading, ew_mult, ns_mult = change_heading2(heading, count, ew_mult, ns_mult)
        return heading, ew, ns, ew_mult, ns_mult
    elif instruction == 'L':
        heading, ew_mult, ns_mult = change_heading2(heading, -count, ew_mult, ns_mult)
        return heading, ew, ns, ew_mult, ns_mult
    elif instruction == 'F':
        ew, ns = move2(ew, ns, count, ew_mult, ns_mult)
    else:
        ew_mult, ns_mult = change_mult(instruction, count, ew_mult, ns_mult)
    return heading, ew, ns, ew_mult, ns_mult


def part1(input):
    heading = 90
    ew = 0
    ns = 0
    for i in input:
        instruction = i[0]
        count = int(i[1:])
        heading, ew, ns = update(heading, ew, ns, instruction, count)

    print("11.1 ---> " + str(abs(ew) + abs(ns)))


def part2(input):
    heading = 90
    ew_mult = 10
    ns_mult = 1
    ew = 0
    ns = 0
    for i in input:
        instruction = i[0]
        count = int(i[1:])
        heading, ew, ns, ew_mult, ns_mult = update2(heading, ew, ns, ew_mult, ns_mult, instruction, count)
        print(i.strip() + ' --- ' + str(heading) + ',' + str(ew) + ',' + str(ns) + ' : ' + str(ew_mult) + ',' + str(ns_mult))
    print("11.2 ---> " + str(abs(ew) + abs(ns)))
    pass


if __name__ == "__main__":
    input = read_input(get_input_file())
    part1(input)
    part2(input)
