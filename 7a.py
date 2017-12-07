programs = {}

class Program:
    def __init__(self, name, weight, children, parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent

with open('7.input', 'r') as handle:
    for line in handle.readlines():
        split_line = line.strip('\n').split(' -> ')

        name, weight = split_line[0].split(' ')
        weight = int(weight.strip('()'))

        children = []
        if len(split_line) > 1:
            children = split_line[1].split(', ')

        programs[name] = Program(name, weight, children)
        
for name, program in programs.items():
    for child in program.children:
        programs[child].parent = name

program = next(iter(programs.values()))

while program.parent:
    program = programs[program.parent]

print(program.name)
