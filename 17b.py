index = 0
length = 1

current = 0

for i in range(50000000):
    index += 329
    index %= length

    length += 1
    index += 1

    if index == 1:
        current = i + 1

print(current)
