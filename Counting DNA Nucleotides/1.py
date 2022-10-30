f = open("ROSALIND_Problems/Counting DNA Nucleotides/rosalind_dna.txt")

DNA = f.read()

A = 0
G = 0
C = 0
T = 0

for dna in DNA:
    if dna == 'A':
        A += 1
    if dna == 'G':
        G += 1
    if dna == 'C':
        C += 1
    if dna == 'T':
        T += 1

print(A, C, G, T)
