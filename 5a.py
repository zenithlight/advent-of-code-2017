values = None

with open('5.input', 'r') as handle:
    values = [int(pointer) for pointer in handle.readlines()]

address = 0
total = 0

while 0 <= address < len(values):
    old_address = address
    address += values[address]
    values[old_address] += 1
    total += 1

print(total)
