def probAorB(a:set,b:set,all_possible_outcomes:set):
    prob_a = len(a)/len(all_possible_outcomes)
    prob_b = len(b)/len(all_possible_outcomes)

    inter = a.intersection(b)

    prob_inter = len(inter)/len(all_possible_outcomes)

    return (prob_a+prob_b-prob_inter)

evens = {2,4,6}
greater_than_2 = {3,4,5,6}
all_possible_roles = {1,2,3,4,5,6}

print(f'''
The Probability of Getting an even number or a number greater than two is:
{probAorB(evens,greater_than_2,all_possible_roles)}
''')