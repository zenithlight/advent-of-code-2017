import collections

letters = list('abcdefghijklmnopqrstuvwxyz')

instructions = []
registers = collections.defaultdict(int)
last_played = 0

with open('18.input', 'r') as handle:
    for line in handle:
        instructions.append(line.strip().split())

def get_value(input):
    if input in letters:
        return registers[input]
    else:
        return int(input)

i = 0
while 0 <= i < len(instructions):
    symbols = instructions[i]

    if symbols[0] == 'snd':
        last = get_value(symbols[1])

    if symbols[0] == 'set':
        registers[symbols[1]] = get_value(symbols[2])

    if symbols[0] == 'add':
        registers[symbols[1]] += get_value(symbols[2])

    if symbols[0] == 'mul':
        registers[symbols[1]] *= get_value(symbols[2])

    if symbols[0] == 'mod':
        registers[symbols[1]] %= get_value(symbols[2])

    if symbols[0] == 'rcv':
        if registers[symbols[1]] != 0:
            print(last)
            break

    if symbols[0] == 'jgz':
        if registers[symbols[1]] > 0:
            i += get_value(symbols[2])
            continue

    i += 1
