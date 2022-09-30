
ps = True
x = 1
while ps:
    if x <= 10:
        print (x)
        x += 1
    else:
        ps = False

y = 1
while y <= 10:
    print (y)
    y += 1


for i in range(1, 50+1):
    is_prime = True
    if i > 1:
        for j in range(2, i):
            if (i%j == 0):
                is_prime = False
            if is_prime == True:
                print (i)
    


sequence = 'GGGAAATTT'
complement = ''
def complement_base(base):
    if base == 'A':
        output = 'T'
    elif base == 'T':
        output = 'A'
    elif base == 'C':
        output = 'G'
    elif base == 'G':
        output = 'C'
    else:
        output = 'N'
    return output

for base in sequence:
    complement = complement + complement_base(base)
print(complement)



seq = 'ATCGGT'
def reverse_seq(seq):
    reverse = ''
    for base in seq:
        reverse = base + reverse
    return reverse
print(reverse_seq(seq))



sequence = 'GGGAAATTT'
complememt = ''
def complement_base(base):
    if base == 'A':
        output = 'T'
    elif base == 'T':
        output = 'A'
    elif base == 'C':
        output = 'G'
    elif base == 'G':
        output = 'C'
    else:
        output = 'N'
    return output

    for base in sequence:
        complement += complement_base(base)
    return complement

        
    def reverse_complement(complement):
        reverse_complement = ''
        for base in complement:
            reverse_complement = base + reverse_complement
    return reverse_complement

print (reverse_complement(complement))














