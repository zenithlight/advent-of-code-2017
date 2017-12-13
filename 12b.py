programs = {}

with open('12.input', 'r') as handle:
    for line in handle.readlines():
        split_line = line.strip('\n').split(' <-> ')

        program = split_line[0]
        pipes = set(split_line[1].split(', '))

        programs[program] = pipes

def connected_to(program, known_connected=set()):
    this = set([program])
    not_known = programs[program].difference(known_connected)
    results = [connected_to(connection, known_connected.union(this)) for connection in not_known]

    return this.union(*results)

ungrouped_programs = set(programs.keys()) # the list of all programs that are yet to be separated into groups
groups = []

while len(ungrouped_programs) > 0:
    root = ungrouped_programs.pop()
    group = connected_to(root)
    ungrouped_programs -= group
    groups.append(group)

print(len(groups))
