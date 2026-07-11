import scipy.stats as stats

def convert_perc(num:float):
    return str(int(round(num,2)*100))+'%'

def find_prob_range(ranges:list,total:int):
    total_length = len(ranges)
    prob = 0
    for i in ranges:
        prob+=stats.poisson.pmf(i,total)
    return prob

def find_prob(data_container:dict,data):
    keys = list(data_container.keys())
    values =list(data_container.values())

    total = 0
    for i in values:
        total+=values
    
