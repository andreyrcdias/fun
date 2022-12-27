from itertools import groupby

dna = input()
dna_seq = list(dna)

def longest_repetition(dna_seq) -> int:
    repetitions = [(k, len(list(g))) for k, g in groupby(dna_seq)]
    return max(count for _, count in repetitions)

print(longest_repetition(dna_seq))

