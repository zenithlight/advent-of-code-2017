import sys
import itertools
from operator import add

target = int(sys.argv[1])

values = {(0, 0) : 1}

def get_stride(start, stride_length, axis, reverse):
    if axis == 0 and reverse == False:
        return [(start[0] + i + 1, start[1]) for i in range(stride_length)]

    if axis == 1 and reverse == False:
        return [(start[0], start[1] + i + 1) for i in range(stride_length)]

    if axis == 0 and reverse == True:
        return [(start[0] - i - 1, start[1]) for i in range(stride_length)]

    if axis == 1 and reverse == True:
        return [(start[0], start[1] - i - 1) for i in range(stride_length)]

def get_neighbor_sum(values, coordinate):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    neighbors = [tuple(map(add, coordinate, offset)) for offset in offsets]

    return sum([(values[neighbor] if neighbor in values else 0) for neighbor in neighbors])

current = (0, 0)
stride_length = 1
while True:
    stride = get_stride(current, stride_length, 0, False)
    for coordinate in stride:
        value = get_neighbor_sum(values, coordinate)

        if value > target:
            print(value)
            quit()

        values[coordinate] = value

    current = stride[-1]

    stride = get_stride(current, stride_length, 1, False)
    for coordinate in stride:
        value = get_neighbor_sum(values, coordinate)

        if value > target:
            print(value)
            quit()

        values[coordinate] = value

    current = stride[-1]

    stride_length += 1

    stride = get_stride(current, stride_length, 0, True)
    for coordinate in stride:
        value = get_neighbor_sum(values, coordinate)

        if value > target:
            print(value)
            quit()

        values[coordinate] = value

    current = stride[-1]

    stride = get_stride(current, stride_length, 1, True)
    for coordinate in stride:
        value = get_neighbor_sum(values, coordinate)

        if value > target:
            print(value)
            quit()

        values[coordinate] = value

    current = stride[-1]

    stride_length += 1
