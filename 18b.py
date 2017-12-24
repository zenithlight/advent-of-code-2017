import sys
import collections
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue=sys.argv[1])
channel.queue_declare(queue=sys.argv[2])

letters = list('abcdefghijklmnopqrstuvwxyz')

instructions = []
registers = collections.defaultdict(int)

registers['p'] = int(sys.argv[1])

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

    if symbols[0] == 'snd':
        number_of_sends += 1
        print(number_of_sends)
        channel.basic_publish(exchange='', routing_key=sys.argv[2], body=str(get_value(symbols[1])))

    if symbols[0] == 'rcv':
        placeholder = channel.basic_get(queue=sys.argv[1])[2]

        while placeholder is None:
            placeholder = channel.basic_get(queue=sys.argv[1])[2]

        registers[symbols[1]] = int(placeholder)

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

connection.close()
