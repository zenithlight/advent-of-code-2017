time = 0
levels = {}

with open('13.input', 'r') as handle:
    for line in handle:
        split_line = line.strip('\n').split(': ')

        level = int(split_line[0])
        depth = int(split_line[1])

        levels[level] = depth

end = max(levels.keys())

delay = -1
detected = True
while detected:
    detected = False
    delay += 1

    for i in range(0, end + 1):
        if i in levels and (i + delay) % ((levels[i] - 1) * 2) == 0:
            print(delay, i)
            detected = True

print(delay)
