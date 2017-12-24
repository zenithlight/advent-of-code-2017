components = []

with open('24.input', 'r') as handle:
    for line in handle:
        types = [int(type) for type in line.split('/')]
        components.append({
            'left': types[0],
            'right': types[1],
            'used': 0 # -1 for left side used, 1 for right side used
        })

bridges = []

def find_strongest(path=[]):
    bridges.append({
        'strength': sum(component['left'] + component['right'] for component in path),
        'length': len(path)
    })

    if len(path) == 0:
        unused = 0
    else:
        if path[-1]['used'] == -1:
            unused = path[-1]['right']
        else:
            unused = path[-1]['left']

    compatible = [component for component in components if (component['left'] == unused or component['right'] == unused) and component['used'] == 0]

    for component in compatible:
        if component['left'] == unused:
            component['used'] = -1
        else:
            component['used'] = 1

        find_strongest(path + [component])

        component['used'] = 0

find_strongest()

longest = max(bridge['length'] for bridge in bridges)

longest_bridges = [bridge for bridge in bridges if bridge['length'] == longest]

print(max(bridge['strength'] for bridge in longest_bridges))
