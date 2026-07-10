import scipy.stats as stats
from Functions import convert_perc
from Functions import find_prob_range

print(f'''
The probability of getting more than 6 heads in 10 coin flips is: {1-(stats.binom.cdf(6,10,0.5))}
''')



prob1 = stats.poisson.pmf(6,10)
perc_1 = convert_perc(prob1)
print(f'Percentage probability of raining  for exactly 6 days: {perc_1}')



prob2 = find_prob_range([12,13,14],10)
perc_2 = convert_perc(prob2)
print(f'Percentage of probability of raining for 12-14 days: {perc_2}')