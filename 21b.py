current = [
    list('.#.'),
    list('..#'),
    list('###')
]

def flip(pattern):
    return [row[::-1] for row in pattern]

def rotate(pattern):
    return [list(column) for column in zip(*pattern[::-1])]

patterns = []
outputs = []
with open('21.input', 'r') as handle:
    for rule in handle:
        [pattern, output] = rule.strip().split(' => ')

        identity = [list(row) for row in pattern.split('/')]
        rotate_90 = rotate(identity)
        rotate_180 = rotate(rotate_90)
        rotate_270 = rotate(rotate_180)

        patterns.append(identity)
        patterns.append(rotate_90)
        patterns.append(rotate_180)
        patterns.append(rotate_270)

        patterns.append(flip(identity))
        patterns.append(flip(rotate_90))
        patterns.append(flip(rotate_180))
        patterns.append(flip(rotate_270))

        result = [list(row) for row in output.split('/')]

        outputs.append(result)
        outputs.append(result)
        outputs.append(result)
        outputs.append(result)

        outputs.append(result)
        outputs.append(result)
        outputs.append(result)
        outputs.append(result)

def print_pattern(pattern):
    for row in pattern:
        print(''.join(row))

    print()

def get_next(pattern):
    size = len(pattern[0])

    if size in (2, 3):
        return outputs[patterns.index(pattern)]

    next = []

    if size % 2 == 0:
        for i in range(0, size * 3, 2):
            row = []

            for j in range(0, size * 3, 2):
                row.append(None)

            next.append(row)

        for i in range(0, size, 2):
            for j in range(0, size, 2):
                subpattern = get_next([
                    [pattern[i][j], pattern[i][j + 1]],
                    [pattern[i + 1][j], pattern[i + 1][j + 1]],
                ])

                for k, row in enumerate(subpattern):
                    for l, character in enumerate(row):
                        next[int(i * 3 / 2) + k][int(j * 3 / 2) + l] = character

    else:
        for i in range(0, size * 4, 3):
            row = []

            for j in range(0, size * 4, 3):
                row.append(None)

            next.append(row)

        for i in range(0, size, 3):
            for j in range(0, size, 3):
                subpattern = get_next([
                    [pattern[i][j], pattern[i][j + 1], pattern[i][j + 2]],
                    [pattern[i + 1][j], pattern[i + 1][j + 1], pattern[i + 1][j + 2]],
                    [pattern[i + 2][j], pattern[i + 2][j + 1], pattern[i + 2][j + 2]],
                ])

                for k, row in enumerate(subpattern):
                    for l, character in enumerate(row):
                        next[int(i * 4 / 3) + k][int(j * 4 / 3) + l] = character

    return next

for i in range(18):
    current = get_next(current)

print(''.join(''.join(row) for row in current).count('#'))
