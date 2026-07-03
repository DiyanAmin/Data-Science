import random as r
from string import ascii_letters

possible_guests = []
a = False
for i in ascii_letters:
    if i=='z':
        a=True
        continue
    if a:
        possible_guests.append(i)


b = r.choice([6,7])

guests1 = []
guests2 = []
for i in range(1,b):
    guests1.append(
        r.choice(possible_guests)
    )

print(f'Guests 1:\n{guests1}')

b = r.choice([6,7])

for i in range(1,b):
    guests2.append(
        r.choice(possible_guests)
    )

print(f'\nGuests 2:\n{guests2}\n')

set1 = set(guests1)
set2 = set(guests2)

union = set1.union(set2)

total_guests = tuple(union)

print(f'\n\nTotal number of guests to be invited: {len(total_guests)}\nList of guests:\n{total_guests}\n\n')

intersection = set1.intersection(set2)

total_guests = tuple(intersection)
print(f'Total number of guests to be invited are: {len(total_guests)}\nList of guests:\n{total_guests}\n\n')