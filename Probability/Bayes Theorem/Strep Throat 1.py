def find_prob(a,b):

    if a==1:
        prob_a=0.2

        if  b==1:
            prob_bga=0.85
        
        elif b==2:
            prob_bga = 0.15

        else:
            print('Invalid Choice')

        probs = {
            'bga': prob_bga,
            'pab': prob_a*prob_bga
        }

    elif a==2:
        prob_a=0.8

        if b==1:
            prob_bga=0.02

        elif b==2:
            prob_bga=0.98
        else:
            print('Invalid Choice')
        
        prob_a_b = prob_a*prob_bga
    
        probs = {
            'bga': prob_bga,
            'pab': prob_a_b
        }

    else:
        print("Invalid Choice")

    return probs

print('Please Enter choices for events:')

try:
    has = int(input('Person has step throat?\n1. Yes\n2. No\nYour Choice: '))
    test_res = int(input('Person has tested positive?\n1. Yes\n2. No\nYour Choice: '))

    probs = find_prob(has,test_res)

    print(f'\n\nProbabilities for event a and b are:\n{probs['pab']}\n\nProbability for b given a:\n{probs['bga']}')

except ValueError as e:
    print(f'Please Enter numbers Only;\n{e}')