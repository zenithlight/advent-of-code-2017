import sys

digits = [int(digit) for digit in list(sys.argv[1])]
rotated_digits = digits[1:] + digits[:1]

pairs = zip(digits, rotated_digits)

print(sum([a for a, b in pairs if a == b]))
