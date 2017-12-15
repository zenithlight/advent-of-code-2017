a = int(sys.argv[1])
b = int(sys.argv[2])
count = 0

for i in range(5000000):
    a *= 16807
    a %= 2147483647

    while a % 4 != 0:
        a *= 16807
        a %= 2147483647

    b *= 48271
    b %= 2147483647

    while b % 8 != 0:
        b *= 48271
        b %= 2147483647

    if '{:b}'.format(a)[-16:] == '{:b}'.format(b)[-16:]:
        count += 1

print(count)

