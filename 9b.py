stream = None
with open('9.input', 'r') as handle:
    stream = handle.read().strip()

score = 0
in_garbage = False
ignore_next = False

for character in stream:
    if ignore_next:
        ignore_next = False
        continue

    if character == '!':
        ignore_next = True

    if in_garbage:
        if character == '>':
            in_garbage = False
        else:
            if character != '!':
                score += 1
            continue

    if character == '<':
        in_garbage = True

print(score)
