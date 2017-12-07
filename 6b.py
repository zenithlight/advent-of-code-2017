def redistributed(values):
    new_values = values[:]

    index = new_values.index(max(new_values))
    blocks = new_values[index]
    new_values[index] = 0

    while blocks > 0:
        index += 1
        index %= len(new_values)
        new_values[index] += 1
        blocks -= 1

    return new_values

values = None

with open('6.input', 'r') as handle:
    values = [int(value) for value in handle.read().split()]

states = [values]

while True:
    new_values = redistributed(states[-1])

    if new_values in states:
        states.append(new_values)
        break

    states.append(new_values)

print(len(states) - states.index(states[-1]) - 1)

