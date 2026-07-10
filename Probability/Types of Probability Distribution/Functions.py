import scipy.stats as stats

def convert_perc(num:float):
    return str(int(round(num,2)*100))+'%'

def find_prob_range(ranges:list,total:int):
    total_length = len(ranges)
    prob = 0
    for i in ranges:
        prob+=stats.poisson.pmf(i,total)
    return prob