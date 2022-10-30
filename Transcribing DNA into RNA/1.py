f = open("ROSALIND_Problems/Transcribing DNA into RNA/rosalind_rna.txt")

DNA = f.read()
RNA = []

for i, t in enumerate(DNA):
    if t == 'T':
        RNA.append('U')
    else:
        RNA.append(t)

print(''.join(str(u) for u in RNA))
