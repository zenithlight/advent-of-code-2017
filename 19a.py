letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
seen = []

maze = None
with open('19.input', 'r') as handle:
    maze = handle.readlines()

def get_point(coordinates):
    return maze[coordinates[0]][coordinates[1]]

def add_point(a, b):
    return (a[0] + b[0], a[1] + b[1])

position = (0, maze[0].index('|'))
heading = (1, 0)
last = position

while True:
    point = get_point(position)

    if point in letters:
        seen.append(point)

    if point == '|' and heading == (1, 0) or heading == (-1, 0):
        new_position = add_point(position, heading)

        while get_point(new_position) == '-' or get_point(new_position) in letters:
            if get_point(new_position) in letters:
                seen.append(get_point(new_position))

            new_position = add_point(new_position, heading)

    elif point == '-' and heading == (0, 1) or heading == (0, -1):
        new_position = add_point(position, heading)

        while get_point(new_position) == '|' or get_point(new_position) in letters:
            if get_point(new_position) in letters:
                seen.append(get_point(new_position))

            new_position = add_point(new_position, heading)

    elif point == '+':
        new_position = add_point(position, heading)

    if get_point(new_position) == ' ':
        dead_end = True

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if direction != heading and get_point(add_point(direction, position)) != ' ' and add_point(direction, position) != last:
                heading = direction
                new_position = add_point(direction, position)
                dead_end = False
                break

        if dead_end:
            print(''.join(seen))
            break

    last = position
    position = new_position
