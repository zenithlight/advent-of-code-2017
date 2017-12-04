import sys

digits = [int(digit) for digit in list(sys.argv[1])]

half_length = int(len(digits) / 2)
rotated_digits = digits[half_length:] + digits[:half_length]

pairs = zip(digits, rotated_digits)

print(sum([a for a, b in pairs if a == b]))
