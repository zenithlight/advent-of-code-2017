import math
import sys

address = int(sys.argv[1])

dimension = math.ceil(math.sqrt(address))
dimension += (dimension + 1) % 2 # spiral needs an odd dimension

corner = dimension * dimension # address of the bottom-right corner

half_dimension = math.floor(dimension / 2)
midpoints = [
    corner - half_dimension,
    corner - 3 * half_dimension,
    corner - 5 * half_dimension,
    corner - 7 * half_dimension,
]

closest_midpoint = max([midpoint for midpoint in midpoints if address >= midpoint])
difference = address - closest_midpoint

print(half_dimension + difference)
