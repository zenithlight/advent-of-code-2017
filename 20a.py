particles = None
with open('20.input', 'r') as handle:
    particles = [{
        'position': [int(magnitude) for magnitude in line.strip().split(', ')[0][3:-1].split(',')],
        'velocity': [int(magnitude) for magnitude in line.strip().split(', ')[1][3:-1].split(',')],
        'acceleration': [int(magnitude) for magnitude in line.strip().split(', ')[2][3:-1].split(',')],
        'index': i  
    } for i, line in enumerate(handle)]

def sort_particles(a, b):
    if a['acceleration'] != b['acceleration']:
        a_distance = sum(abs(axis * axis) for axis in a['acceleration'])
        b_distance = sum(abs(axis * axis) for axis in b['acceleration'])

        return 1 if a_distance > b_distance else -1

    if a['velocity'] != b['velocity']:
        a_distance = sum(abs(axis) for axis in a['velocity'])
        b_distance = sum(abs(axis) for axis in b['velocity'])

        return 1 if a_distance > b_distance else -1

    if a['position'] != b['position']:
        a_distance = sum(abs(axis) for axis in a['position'])
        b_distance = sum(abs(axis) for axis in b['position'])

        return 1 if a_distance > b_distance else -1

    return 0

particles.sort(cmp=sort_particles)

print(particles[0]['index'])
