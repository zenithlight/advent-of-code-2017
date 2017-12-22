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

def get_next(pattern):
    size = len(pattern[0])

    if size in (2, 3):
        return outputs[patterns.index(pattern)]

    if size % 2 == 0:
        next = ([None] * int(size * 3 / 2)) * int(size * 3 / 2)

        for i in range(int(size / 2)):
            for j in range(int(size / 2)):
                subpattern = get_next([
                    [pattern[i * 2][j * 2], pattern[i * 2][j * 2 + 1]],
                    [pattern[i * 2 + 1][j * 2], pattern[i * 2 + 1][j * 2 + 1]],
                ])

                for k, row in enumerate(subpattern):
                    for l, character in enumerate(row):
                        next[i * 3 + k][j * 3 + l] = character

                print(next)

for i in range(3):
    current = get_next(current)

print(''.join(''.join(row) for row in current).count('#'))
