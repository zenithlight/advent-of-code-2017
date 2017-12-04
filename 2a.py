table = None

with open('2.input', 'r') as handle:
    table = [[int(number) for number in line.split()] for line in handle.readlines()]

print(sum([max(line) - min(line) for line in table]))
