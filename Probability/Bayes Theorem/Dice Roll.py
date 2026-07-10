from numpy.random import choice as c
die_sides = int(input('Enter number of sides for dice(6/12): '))
num_rolls = int(input('Enter number of times you want to roll dice: '))
print(c(range(1,die_sides+1),size=num_rolls,replace=True))