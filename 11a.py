steps = None
with open('11.input', 'r') as handle:
    steps = handle.read().strip().split(',')

# steps can be decomposed into positive and negative n and se steps
n = 0
se = 0

for step in steps:
    if step == 'n':
        n += 1

    if step == 'ne':
        n += 1
        se += 1

    if step == 'se':
        se += 1

    if step == 's':
        n -= 1

    if step == 'sw':
        n -= 1
        se -= 1

    if step == 'nw':
        se -= 1

print(max(abs(n), abs(se)))
