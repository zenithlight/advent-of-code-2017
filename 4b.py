import collections
import itertools

with open('4.input', 'r') as handle:
    passphrases = [[collections.Counter(word) for word in line.split()] for line in handle.readlines()]

valid_passphrases = [passphrase for passphrase in passphrases if all([combination[0] != combination[1] for combination in itertools.combinations(passphrase, 2)])]

print(len(valid_passphrases))
