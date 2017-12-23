import os
import collections

letters = list('abcdefgh')

instructions = []
registers = collections.defaultdict(int)

with open('23.input', 'r') as handle:
    for line in handle:
        instructions.append(line.strip().split())

def get_value(input):
    if input in letters:
        return registers[input]
    else:
        return int(input)

mul_count = 0

i = 0
while 0 <= i < len(instructions):
    symbols = instructions[i]

    if symbols[0] == 'set':
        registers[symbols[1]] = get_value(symbols[2])

    if symbols[0] == 'sub':
        registers[symbols[1]] -= get_value(symbols[2])

    if symbols[0] == 'mul':
        mul_count += 1
        registers[symbols[1]] *= get_value(symbols[2])

    if symbols[0] == 'jnz':
        if get_value(symbols[1])!= 0:
            i += get_value(symbols[2])
            continue

    i += 1

print(mul_count)
