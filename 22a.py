directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

position = (12, 12)
facing = 0 # directions index

infected = set()
with open('22.input', 'r') as handle:
    for i, line in enumerate(handle):
        for j, character in enumerate(line):
            if character == '#':
                infected.add((j, i))

count = 0
for i in range(10000):
    if position in infected:
        facing += 1
        facing %= len(directions)

        infected.remove(position)

    else:
        facing -= 1
        facing %= len(directions)

        infected.add(position)

        count += 1

    position = (position[0] + directions[facing][0], position[1] + directions[facing][1])

print(count)
