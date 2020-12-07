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

def process(line):
    rules = {}
    last_match_len = 0

    m = re.search("(?P<key>.*) bags contain ", line)
    key = m.group('key')
    line = line[len(m.group(0)):]
    rules[key] = []

    while(True):
        m = re.search("(?P<count>\d+) (?P<color>[\w ]+) bag[s]*", line)
        if (m):
            rules[key].append( { "color" : m.group('color'), "count" : m.group('count') })
            line = line[len(m.group(0)):]
        else:
            break;

    return rules


def contains(bags, color, rules):
  for bag in bags:
    if 'shiny gold' == bag['color'] or contains(rules[bag['color']], color, rules):
        return True
  return False

def count(rules, color):
    contains_color = []
    for bag, subbags in rules.items():
        if contains(subbags, color, rules):
            contains_color.append(bag)
    return contains_color

if __name__ == "__main__":
    input_file = get_input_file();
    input = read_input(input_file)
    rules = {}
    for i in input:
        rules.update(process(i))
    print(len(count(rules, "shiny gold")))
