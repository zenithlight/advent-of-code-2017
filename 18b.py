import sys
import collections
import zmq

letters = list('abcdefghijklmnopqrstuvwxyz')

instructions = []
registers = collections.defaultdict(int)

registers['p'] = int(sys.argv[1])

context = zmq.Context()

publish = context.socket(zmq.PUB)
subscribe = context.socket(zmq.SUB)

try:
    publish.bind('tcp://127.0.0.1:8000')
except:
    publish.connect('tcp://127.0.0.1:8000')

subscribe.connect('tcp://127.0.0.1:8000')

subscribe.setsockopt(zmq.SUBSCRIBE, sys.argv[2].encode('utf-8'))

input() # both instances need to be connected before running for this to work

with open('18.input', 'r') as handle:
    for line in handle:
        instructions.append(line.strip().split())

def get_value(input):
    if input in letters:
        return registers[input]
    else:
        return int(input)

index = 0
number_of_sends = 0

while 0 <= index < len(instructions):
    symbols = instructions[index]
    print(registers, symbols)

    if symbols[0] == 'snd':
        number_of_sends += 1
        publish.send_multipart([
            sys.argv[1].encode('utf-8'),
            str(get_value(symbols[1])).encode('utf-8')
        ])

    if symbols[0] == 'rcv':
        registers[symbols[1]] = int(subscribe.recv())

    if symbols[0] == 'set':
        registers[symbols[1]] = get_value(symbols[2])

    if symbols[0] == 'add':
        registers[symbols[1]] += get_value(symbols[2])

    if symbols[0] == 'mul':
        registers[symbols[1]] *= get_value(symbols[2])

    if symbols[0] == 'mod':
        registers[symbols[1]] %= get_value(symbols[2])

    if symbols[0] == 'jgz':
        if get_value(symbols[1]) > 0:
            index += get_value(symbols[2])
            continue

    index += 1

print(number_of_sends)
