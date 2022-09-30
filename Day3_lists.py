# 1. Create a list called 'participants' containing the of the names of your fellow trainee
participants = ['Li-Hsin','Nicole','Susann','Matt', 'Christina','Emiily','Kinam']
print(participants)

# 2. Create the following new variables participants_2 and participants_3 by typing
participants_2 = participants
participants_3 = participants.copy()
 ## .copy doesn't work in Python2

# 3. Add the names of today's trainers to the list 'participants' using append
participants.append('David')
participants.append('Andrea')

# 4. Print the 'participants', 'participants_2' and 'participants_3' lists \\
print(participants)
print(participants_2)
print(participants_3)

# 5. Select the 3rd and 5th names from your participants list
participants[2]
participants[4]

# 6. Sort your list & select the 3rd to the 5th names from your participants list
participants.sort()
print('sorted', participants)
participants[2:5]


# 7. Select the first 2 letters of the string in the third value of your participants list
pa2 = participants[2]
print (pa2[:2])

# 8. Iterate over the participants list and set the names to keys in a dictionary with the value as 'trainee’ or ‘trainer’ depending on thier role.
ab = {}
for name in participants:
    if name == 'David' or name == 'Andrea':
        ab[name] = 'trainer'
    else:
        ab[name] = 'trainee'
print (ab)
if 'Li-Hsin' in ab:
    print ("Li-Hsin is a", ab['Li-Hsin'])
for name in participants:
    print (name)

# 9. Use a for loop to iterate over your dictionary and print the values of the keys only if they are trainees
for name in ab.keys():
    if ab.get(name, 0) == 'trainee':
        print(name)

for name, roles in ab.items():
    if roles == 'trainee':
        print(name, roles)

# 10.1 Repeat exercises 1-7 but create a tuple for 'participants' in step1 instead of a list – what do you notice about the behaviour of tuples compared to lists?
participants = ('Li-Hsin','Nicole','Susann','Matt', 'Christina','Emiily','Kinam')
print(participants)

# 10.2. Create the following new variables participants_2 and participants_3 by typing
participants_2 = participants
participants_3 = participants.copy()


# 10.3. Add the names of today's trainers to the list 'participants' using append
participants.append('David')
participants.append('Andrea')

# 10.4. Print the 'participants', 'participants_2' and 'participants_3' lists \\
print(participants)
print(participants_2)
print(participants_3)

# 10.5. Select the 3rd and 5th names from your participants list
participants[2]
participants[4]

# 10.6. Sort your list & select the 3rd to the 5th names from your participants list
participants.sort()
print('sorted', participants)
participants[2:5]

# 10.7. Select the first 2 letters of the string in the third value of your participants list
pa2 = participants[2]
print (pa2[:2])


    
    
