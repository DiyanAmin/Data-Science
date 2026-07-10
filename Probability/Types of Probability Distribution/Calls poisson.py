import scipy.stats as stats

def convert_perc(num:float):
    return str(int(round(num,2)*100))+'%'

def find_prob_range(ranges:list,total:int):
    total_length = len(ranges)
    prob = 0
    for i in ranges:
        prob+=stats.poisson.pmf(i,total)
    return prob

prob1 = stats.poisson.pmf(20,15)
perc1 = convert_perc(prob1)
print(perc1)

prob2 = stats.poisson.pmf(21,15) - stats.poisson.pmf(16,15)
perc2 = convert_perc(prob2)
print(perc2)