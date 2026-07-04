# Rolling a Die: Prime Number or Number Greater Than 4
# A die is rolled once.
# Event A = Prime number → {2,3,5}
# Event B = Number greater than 4 → {5,6}

evet_a = {2,3,5}
event_b={5,6}
all_outcomes = {1,2,3,4,5,6}

def probAorB(a:set,b:set,all_possible_outcomes:set):
    prob_a = len(a)/len(all_possible_outcomes)
    prob_b = len(b)/len(all_possible_outcomes)

    inter = a.intersection(b)

    prob_inter = len(inter)/len(all_possible_outcomes)

    return (prob_a+prob_b-prob_inter)

prob = probAorB(evet_a,event_b,all_outcomes)
print(f'Probability:\n{prob}')