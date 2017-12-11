import sys

string = list(range(256))
lengths = [int(digit) for digit in sys.argv[1].split(',')]

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

for length in lengths:
    string = rearrange(string, current, length)

    current += length + skip_size
    current %= 256

    skip_size += 1

print(string[0] * string[1])
