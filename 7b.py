import collections

programs = {}

class Program:
    def __init__(self, name, weight, children, parent=None):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = parent

def get_subtree_weight(program):
    try:
        return programs[program].subtree_weight
    except:
        programs[program].subtree_weight = programs[program].weight + sum([get_subtree_weight(child) for child in programs[program].children])
        return programs[program].subtree_weight

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

def get_correct_weight(parent, target_weight=0):
    weights = collections.Counter()

    for child in parent.children:
        weights[get_subtree_weight(child)] += 1

    if len(weights) > 1:
        odd_weight = weights.most_common()[1][0]

        odd_child = None
        for child in parent.children:
            if get_subtree_weight(child) == odd_weight:
                odd_child = child

        return get_correct_weight(programs[odd_child], weights.most_common()[0][0])
    else:
        return parent.weight - (get_subtree_weight(parent.name) - target_weight)

print(get_correct_weight(program))
