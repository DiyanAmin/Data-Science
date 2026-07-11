# Marble Bag Experiment

# Scenario:
# A bag contains:
# 5 Red marbles
# 3 Blue marbles
# 2 Green marbles

# Tasks:
# Pick a random marble.
# Calculate theoretical probability.
# Repeat 1000 trials to compare experimental probability

from random import choice

bag = {'Red':5,
       'Blue':3,
       'Green':2}

marbles = ['Red','Blue','Green']
nums = [5,3,2]

total = 10

marble = choice(marbles)

