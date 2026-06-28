from random import choice

def pick_ball(balls=['Blue','Red','Green'],prob='Red'):
    result = choice(balls)

    pro = balls.count(prob)/len(balls)
    print(f'Probability of Picking Red ball is: {pro}')

    if result==prob:
        return f'{prob} Ball was picked!'
    
    else:
        return f'{prob} Was not Picked.\nBetter Luck Next Time'
    
print(f'{pick_ball()}\n\n')


def roll_dice(faces=[1,2,3,4,5,6],prob=6):
    result = choice(faces)

    pro = faces.count(prob)/len(faces)
    print(f'Probability of {prob} being picked is: {pro}')
    if result==prob:
        return f'{prob} was picked!'
    else:
        return f'{prob} was not picked.\nBetter Luck Next Time'
    
print(roll_dice())

def calc_prob(items=[1,2,3,4,5,6],prob=6):
    pro = items.count(prob)/len(items)
    return f'Probability for getting {prob} in {items} is: {pro}'

print(f'\n\n{calc_prob()}\n\n')

def pick_winner():
    participants = []
    total_participants = int(input('Enter total number of participants: '))
    val = 1
    while val!=(total_participants+1):
        participant=input(f'Enter participant {val} name: ')
        participants.append(participant)
        val+=1
    
    print(f'{choice(participants)} is the winner.')

pick_winner()

