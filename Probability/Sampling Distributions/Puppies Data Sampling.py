import numpy as np

np.random.seed(42)

puppy_types = [0,1]
puppies_list = []

while len(puppies_list)!=20:
    puppies_list.append(np.random.choice(puppy_types))

puppies = np.array(puppies_list)
print(puppies)


print(f'Mean: {puppies.mean()}')

print(f'Standard Deviation: {puppies.std()}')
print(f'Variance: {puppies.var()}')

np.random.choice(puppies, size=(1,5),replace=True)
np.random.choice(puppies, size=(1,5),replace=True).mean()

print('\nSampling Distribution with size 5\n')

sp = []

for i in range(10000):
    sp.append(np.random.choice(puppies, 5,replace=True).mean())

sp = np.array(sp)

print(f'''
Mean: {sp.mean()}
Standard Deviation: {sp.std()}
Variance: {sp.var()}
''')

print('\nSampling distribution with size 5\n')
tsp = []
for j in range(10000):
    tsp.append(np.random.choice(puppies, 20,replace=True).mean())
tsp = np.array(tsp)

print(f'''
New Mean: {tsp.mean()}
New Standard Deviation: {tsp.std()}
New Variance: {tsp.var()}
''')