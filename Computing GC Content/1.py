f = open('ROSALIND_Problems/Computing GC Content/rosalind_gc.txt')

lines = f.readlines()

# Collect sequence data
seqs = {}
for l in lines:
    if l[0] == '>':
        seq = l
        seqs[seq] = ''
    else:
        l = l.strip()
        seqs[seq] = seqs[seq] + l

# Find max GC, l:labels, s:sequences
label = ''
max = float(0)
for l in seqs:
    GC = 0
    for t in seqs[l]:
        if t == 'G' or t == 'C':
            GC += 1
    val = GC / len(seqs[l])
    if max < val:
        max = val
        label = l

print(label, max)
