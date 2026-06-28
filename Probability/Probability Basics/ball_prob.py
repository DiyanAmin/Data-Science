from matplotlib import pyplot as plt
from random import choice
from pathlib import Path

ran_file = Path(r'C:\Users\Admin\OneDrive\Desktop\Coding\Data Science\Probability\Probability Basics\times_ran.txt')
times_ran = 0
with open(ran_file,'r') as f:
    times_ran = int(f.read())

times_ran+=1
times_ran = str(times_ran)

with open(ran_file,'w') as f:
    f.write(times_ran)

#Random Ball Probability Experiment (Upgrade)
# Enhance your project:
# Add more balls
# Run experiment 100 times
# Calculate actual probability
# Example upgrades:
# Count how many times Red is picked
# Display percentage
# Plot graph of results

def ball_probability(items:list,wanted_winner):
    file = f'results {times_ran}.txt'
    with open(file,'w') as f:
        f.write('Test Results:')


    #Running hundred times
    times_winnner_picked = 0
    results = []
    value = 0
    while value!=100:
        result = choice(items)

        if result == wanted_winner:
            times_winnner_picked+=1
        else:
            pass

        results.append(result)

        with open(file,'a') as j:
            j.write(f'\n{result}')

        value+=1

    prob = items.count(wanted_winner)/len(items)

    print(f'\nTest Results:\n{wanted_winner} was picked {times_winnner_picked} times.\nProbability of {wanted_winner} winning: {prob}')

balls = ['Red','Blue','Yellow','Green']
balls_list = []

while len(balls_list)!=10:
    balls_list.append(choice(balls))

ball_probability(balls_list,'Red')