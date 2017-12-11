import collections

registers = collections.Counter()

with open('8.input', 'r') as handle:
    for line in handle.readlines():
        split_line = line.split()

        register = split_line[0]
        sign = split_line[1]
        amount = int(split_line[2])
        comparator = split_line[4]
        operator = split_line[5]
        comparend = split_line[6]

        if eval(
            'registers[\'{}\'] {} {}'.format(comparator, operator, comparend), 
            { '__builtins__': {}, 'registers': registers }
        ):
            if sign == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

print(registers.most_common()[0][1])
