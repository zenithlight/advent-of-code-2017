import operator
import itertools

particles = None
with open('20.input', 'r') as handle:
    particles = [{
        'position': [int(magnitude) for magnitude in line.strip().split(', ')[0][3:-1].split(',')],
        'velocity': [int(magnitude) for magnitude in line.strip().split(', ')[1][3:-1].split(',')],
        'acceleration': [int(magnitude) for magnitude in line.strip().split(', ')[2][3:-1].split(',')],
        'collided': False    
    } for line in handle]

def cannot_collide(a, b):
    relative_position = map(operator.sub, a['position'], b['position'])

    # are they moving towards each other?
    relative_velocity = map(operator.sub, a['velocity'], b['velocity'])
    
    # take the dot product
    if sum(map(operator.mul, relative_position, relative_velocity)) < 0:
        return False

    # are they accelerating towards each other?
    relative_acceleration = map(operator.sub, a['acceleration'], b['acceleration'])
    
    if sum(map(operator.mul, relative_position, relative_acceleration)) < 0:
        return False

    return True

while True:
    if all(cannot_collide(a, b) for a, b in itertools.combinations(particles, 2)):
        break

    for particle in particles:
        particle['velocity'] = list(map(operator.add, particle['acceleration'], particle['velocity']))
        particle['position'] = list(map(operator.add, particle['velocity'], particle['position']))

    for a, b in itertools.combinations(particles, 2):
        if a['position'] == b['position']:
            a['collided'] = True
            b['collided'] = True

    particles = [particle for particle in particles if not particle['collided']]

print(len(particles))
