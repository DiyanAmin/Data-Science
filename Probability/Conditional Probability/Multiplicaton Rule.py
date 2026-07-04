def prob(a,b):
    total = a+b

    prob_a = a/total
    prob_b_given_a = b/(total-1)

    prob_aANDb = prob_a*prob_b_given_a 

    return round(prob_aANDb,3)

orange = int(input('Enter number of orange balls: '))
blue = int(input('Enter total number of blue balls: '))

print(f'Probability of getting first orange then second blue ball:\n{prob(orange,blue)}')