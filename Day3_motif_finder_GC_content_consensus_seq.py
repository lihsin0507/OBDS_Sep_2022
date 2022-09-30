# Excercise 1. Motif Finder
# Write an algorithm to find all occurrences of a 'TATA' motif in a promoter sequence

sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
motif = 'TATA'
length = len(motif)

pos = 0
for base in sequence:
    if sequence[pos : pos + length] == motif:
        print(f'start position:{pos+1}, end position:{pos+length}')
    pos +=1

pos = 0
total = 0
for base in sequence:
    if sequence[pos : pos + length] == motif:
        total += 1
    pos +=1
print ('The total number of TATA motof is:', total)


# Exercise 2 – GC Content
# Write an algorithm to compute the GC content of a DNA sequence

sequence_2 = 'GTGGCTTAAGAGGGGAGTCGTCACAGGCGTCAAGTCTTCTTTCTAAAGCCGGGGACCTGG'

GC = 0
all_bases = 0
for base in sequence_2:
    if base == 'G' or base == 'C':
        GC += 1
        all_bases +=1
    else:
        all_bases +=1

print (GC)
print (all_bases)

print ('GC content of the sequence is:', GC/all_bases*100,'%')

# Exercise 3 – Hamming Distance
# Write an algorithm to calculate the hamming distance between two DNA sequences

seq_1 = 'GAGCCTACTAACGGGAT'
seq_2 = 'CATCGTAATGACGGCCT'

hamming = 0
position = 0
for base_1 in seq_1:
    if base_1 != seq_2[position]:
        hamming += 1
print ('hammig distance between the two sequences is:', hamming)


# Exercise 4 – Consensus Motif

# Generate motif profile table

s1 = 'CATATGGG'
s2 = 'GATCTGGT'
s3 = 'CATATGAT'
s4 = 'CTTCCGGC'
s5 = 'CATGAGGC'
s6 = 'CAAATGGC'
s7 = 'CATATGGC'

list_of_motifs = [s1, s2, s3, s4, s5, s6, s7]

total_A = [0, 0, 0, 0, 0, 0, 0,]
total_T = [0, 0, 0, 0, 0, 0, 0,]
total_C = [0, 0, 0, 0, 0, 0, 0,]
total_G = [0, 0, 0, 0, 0, 0, 0,]

for position in range(len(list_of_motifs[0])):
    for motif in list_of_motifs:
        base = motif[position]
        if base == 'A':
            total_A[position] +=1
        elif base == 'T':
            total_T[position] +=1
        elif base == 'C':
            total_C[position] +=1
        elif base == 'G':
            total_G[position] +=1

print (total_A)
print (total_T)
print (total_G)
print (total_C)

# Finding a consensus sequence






        


































