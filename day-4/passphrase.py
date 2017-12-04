from collections import Counter

def is_passphrase_valid(passphrase):
    counter = Counter(passphrase.split())
    for word, count in counter.items():
        if count > 1:
            return False
    return True

def count_valid_phrases_from_file(filename):
    with open(filename) as f:
        return sum([is_passphrase_valid(line) for line in f.readlines()])
