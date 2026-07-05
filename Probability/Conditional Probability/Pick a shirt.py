from random import choice 

red_shirts =2
blue_shirts =4
white_shirts= 9
total_num = red_shirts+blue_shirts+white_shirts
total = []
while len(total)!=total_num:
    while len(total)!=red_shirts:
        total.append('red')
    while len(total)!= (red_shirts+blue_shirts):
        total.append('blue')
    while len(total)!=total_num:
        total.append('white')


def prob(a:int,b:int,total):
    prob_a = a/total
    prob_bga = b/(total-1)

    return round(
        (prob_a*prob_bga),
        2
    )
x
probability = (prob(blue_shirts,red_shirts,total_num))*100
prob_percentage = str(int(probability))+'%'

print(f'Probability of first shirt being blue and second being red:\n{prob_percentage}')