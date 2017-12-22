directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

position = (12, 12)
facing = 0 # directions index

infected = set()
with open('22.input', 'r') as handle:
    for i, line in enumerate(handle):
        for j, character in enumerate(line):
            if character == '#':
                infected.add((j, i))

weakened = set()
flagged = set()

count = 0
for i in range(10000000):
    if position in infected:
        facing += 1
        facing %= len(directions)

        infected.remove(position)
        flagged.add(position)

    elif position in flagged:
        facing += 2
        facing %= len(directions)

        flagged.remove(position)
        
    elif position in weakened:
        weakened.remove(position)
        infected.add(position)

        count += 1

    else:
        facing -= 1
        facing %= len(directions)

        weakened.add(position)

    position = (position[0] + directions[facing][0], position[1] + directions[facing][1])

print(count)
