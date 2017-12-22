line = list('abcdefghijklmnop')

steps = None
with open('16.input', 'r') as handle:
    steps = handle.read().strip().split(',')

seen = []

for i in range(0, 1000000000):
    if line in seen:
        break

    seen.append(line[:])

    for step in steps:
        if step[0] == 's':
            a = int(step[1:])

            line = line[-a:] + line[:-a]

        if step[0] == 'x':
            split_step = step[1:].split('/')
            a = int(split_step[0])
            b = int(split_step[1])
        
            tmp = line[a]
        
            line[a] = line[b]
            line[b] = tmp
        
        if step[0] == 'p':
            split_step = step[1:].split('/')
            a = line.index(split_step[0])
            b = line.index(split_step[1])

            tmp = line[a]

            line[a] = line[b]
            line[b] = tmp

print(''.join(seen[1000000000 % len(seen)]))
