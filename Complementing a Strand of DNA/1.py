f = open('ROSALIND/Complementing a Strand of DNA/rosalind_revc.txt')

DNA = f.read()
comp = []

for dna in reversed(DNA):
    if dna == 'A':
        comp.append('T')
    if dna == 'T':
        comp.append('A')
    if dna == 'C':
        comp.append('G')
    if dna == 'G':
        comp.append('C')

print(''.join(str(t) for t in comp))