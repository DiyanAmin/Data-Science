def aANDb(a,b):
    
    if a==1:
        prob_student=0.3
        if b == 1:
            prob_dining = 0.75

        else:
            prob_dining=0.25
    
    if a==2:
        prob_dining=0.7

        if b== 1:
            prob_dining=0.6

        else:
            prob_dining=0.4

    prob_aANDb = round((prob_student*prob_dining))

    probs = {
        'Dining':prob_dining,
        'Student':prob_student,
        'A and B':prob_aANDb
        }

    return probs

print('Check the Probability of an event occurring.Eter your coices')

print('Is the student Freshman? y/n')
a = input('Enter your choice: ')

if a=='y':
    a=1
elif a=='n':
    a=2
else:
    print('\nInvalid Input')

print(f'Is the student eating in the dining hall? y/n\n')
b=input('Enter your choice: ')

if b=='y':
    b=1
elif b=='n':
    b=2
else:
    print('Invalid Input')

probs = aANDb(a,b)

print(f'''
Here is the probability of;
Dining: {probs['Dining']}
Student: {probs['Student']}
Both the events occurring: {probs['A and B']}
''')