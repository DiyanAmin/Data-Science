# Probability with weighted outcomes

# Objective:
# Create a spinner with different colors.

# Example:
# Red – 30%
# Blue – 40%
# Green – 20%
# Yellow – 10%

# Spin it multiple times and compare expected vs. actual results.

from random import choice as c


colors = {
    'Red':30,
    'Blue':40,
    'Green':20,
    'Yellow':10
}

spins_tracker = []

choice_list = []

while len(choice_list)!=100:
    while len(choice_list)!=30:
        choice_list.append('red')

    while len(choice_list)!=70:
        choice_list.append('blue')

    while len(choice_list)!=90:
        choice_list.append('green')

    while len(choice_list)!=100:
        choice_list.append('yellow')

while len(spins_tracker)!=50:
    spins_tracker.append(c(choice_list))

def calc_freq(container:list):
    '''
    Calculates the frequency for all unique values.
    
    :param container: The list which contains the data
    :type container: list

    Returns
    -------

    Dictionary with frequencies
    '''

    unique_values = []
    for i in container:
        if i not in unique_values:
            unique_values.append(i)
        else:
            continue
    
    frequencies = {}
    for i in unique_values:
        frequencies[i] = 0
    
    for j in container:
        frequencies[j]+=1

    return frequencies

frequencies = calc_freq(spins_tracker)

print(f'''
Frequencies
-----------
Red: {frequencies['red']}
Blue: {frequencies['blue']}
Green: {frequencies['green']}
Yellow: {frequencies['yellow']}
''')