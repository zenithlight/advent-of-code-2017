# hardcoded for my input
# probably won't work for other inputs

import collections

state = 'A'
i = 0
memory = collections.defaultdict(int)

for step in range(12629077):
    if state == 'A':
        if memory[i] == 0:
            memory[i] = 1
            i += 1
            state = 'B'
        else:
            memory[i] = 0
            i -= 1
            state = 'B'

    elif state == 'B':
        if memory[i] == 0:
            i += 1
            state = 'C'
        else:
            memory[i] = 1
            i -= 1

    elif state == 'C':
        if memory[i] == 0:
            memory[i] = 1
            i += 1
            state = 'D'
        else:
            memory[i] = 0
            i -= 1
            state = 'A'

    elif state == 'D':
        if memory[i] == 0:
            memory[i] = 1
            state = 'E'
        else:
            state = 'F'

        i -= 1

    elif state == 'E':
        if memory[i] == 0:
            memory[i] = 1
            state = 'A'
        else:
            memory[i] = 0
            state = 'D'

        i -= 1

    elif state == 'F':
        if memory[i] == 0:
            memory[i] = 1
            i += 1
            state = 'A'
        else:
            i -= 1
            state = 'E'

print(list(memory.values()).count(1))
