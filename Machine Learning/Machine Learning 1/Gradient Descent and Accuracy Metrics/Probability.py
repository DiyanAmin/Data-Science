import random as r

# Two fair dice are rolled.
# What is the probability that the product
# is a multiple of 6 but not a multiple of 12?

print(f"Probability of getting a multiple of 6 but not one of 12 is: {1/3}")

# Two fair dice are rolled.
# What is the probability that
# the sum is greater than 8 and at least one die shows an
# even number?

def calc_prob():
    dice = [1,2,3,4,5,6]
    dice_1 = r.choice(dice)
    dice_2 = r.choice(dice)

    bool_prob_freq_8 = []
    bool_prob_freq_even = []

    for i in range(0,100):
        loops = 0
        if dice_1+dice_2>8:
            bool_prob_freq_8.append(True)
        else:
            bool_prob_freq_8.append(False)
        
        if dice_1%2==0 or dice_2%2==0:
            bool_prob_freq_even.append(True)
        else:
            bool_prob_freq_even.append(False)
        
        if loops>=100:
            break
        else:
            loops+=1
            continue

    prob = 0
    prob_8 = 0
    prob_even = 8

    for i in bool_prob_freq_8:
        if i:
            prob_8+=1
        else:
            continue
    
    prob_8/=101

    for i in bool_prob_freq_even:
        if i:
            prob_even+=1
        else:
            continue
    
    prob_even/=101

    prob = prob_8+prob_even

    return prob

print(f'Probability: {calc_prob()}')