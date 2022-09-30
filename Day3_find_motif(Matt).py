sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
motif = 'TATA'
length = len(motif)
pos = 0
for base in sequence:
    if sequence[pos:pos + length] == motif:
        print(f'start: {pos+1}, end: {pos + length}')
    pos+=1



