import sys
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

print(sum(binary_knot_hash(sys.argv[1] + '-' + str(i)).count('1') for i in range(0, 128)))
