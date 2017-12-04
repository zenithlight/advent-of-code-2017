import itertools

table = None

with open('2.input', 'r') as handle:
    table = [[int(number) for number in line.split()] for line in handle.readlines()]

# take a line and find the only integer division result
def divisible(line):
    for pair in itertools.combinations(line, 2):
        result = max(pair) / min(pair)

        if result.is_integer():
            return int(result)

print(sum([divisible(line) for line in table]))
