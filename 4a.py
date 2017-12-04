valid_passphrases = None

with open('4.input', 'r') as handle:
    valid_passphrases = [line for line in handle.readlines() if len(set(line.split())) == len(line.split())]

print(len(valid_passphrases))
