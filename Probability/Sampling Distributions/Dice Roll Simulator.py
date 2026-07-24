# Dice Roll Simulator

# Concepts: Random numbers, probability

# Objective:
# Roll a die 100, 500, or 1000 times and find:
# Frequency of each number (1–6)
# Experimental probability of each outcome

# Extension:
# Display the result using a bar chart.

from random import choice as c
from matplotlib.pyplot import bar as b
import numpy as np

dice = [1,2,3,4,5,6]
roll_results = []

while len(roll_results)!=500:
    roll_results.append(c(dice))

one_freq=0
two_freq=0
three_freq=0
four_freq=0
five_freq=0
six_freq = 0

for j in roll_results:
    if j==1:
        one_freq+=1

    elif j==2:
        two_freq+=1

    elif j==3:
        three_freq+=1
    
    elif j==4:
        four_freq+=1

    elif j==5:
        five_freq+=1

    elif j==6:
        six_freq+=1
    
    else:
        print('Unknown Roll')
    
one_freq/=500
two_freq/=500
three_freq/=500
four_freq/=500
five_freq/=500
six_freq/=500

frequencies = [one_freq,two_freq,three_freq,four_freq,five_freq,six_freq]

index = 0
for k in frequencies:
    print(f'Frequence of {index+1} is : {frequencies[index]}')
    index+=1

frequencies = np.array(frequencies)

print(f'\nHighest Frequence: {frequencies.max()}\nLowest Frequency: {frequencies.min()}')