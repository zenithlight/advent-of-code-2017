import sys
import itertools
import functools
import operator

def knot_hash(message):
    string = list(range(256))
    lengths = [ord(character) for character in message] + [17, 31, 73, 47, 23]

    def rearrange(string, start, length):
        # unshift the string so it starts at position denoted by `start`
        new_string = string[start:] + string[:start]

        # reverse the first `length` elements of string
        new_string = new_string[:length][::-1] + new_string[length:]

        # reshift the resulting string
        new_string = new_string[-start:] + new_string[:-start]

        return new_string

    current = 0
    skip_size = 0

    for i in range(64):
        for length in lengths:
            string = rearrange(string, current, length)

            current += length + skip_size
            current %= 256

            skip_size += 1

    blocks = [string[i:i + 16] for i in range(0, 256, 16)]
    dense = [functools.reduce(operator.xor, block, 0) for block in blocks]

    return ''.join('{:02x}'.format(number) for number in dense)

def binary_knot_hash(message):
    return '{:0128b}'.format(int(knot_hash(message), 16))

rows = [list(binary_knot_hash(sys.argv[1] + '-' + str(i))) for i in range(0, 128)]
visited = set()
number_of_groups = 0

# from a starting position, add it and all others in its group to visited set
def flood_fill(x, y):
    if rows[x][y] != '1' or (x, y) in visited:
        visited.add((x, y))
        return False

    visited.add((x, y))

    if x > 0:
        flood_fill(x - 1, y)
    if x < 127:
        flood_fill(x + 1, y)
    if y > 0:
        flood_fill(x, y - 1)
    if y < 127:
        flood_fill(x, y + 1)

    return True

for i in range(128):
    for j in range(128):
        if flood_fill(i, j):
            number_of_groups += 1

print(number_of_groups)
