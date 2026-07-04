# Probability of Drawing a Red Card or Face Card
# A deck has 52 cards.
# Event A = Drawing a red card
# Event B = Drawing a face card (J, Q, K)
# Find:
# P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

all_possible_outcomes = []
hand = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

while len(all_possible_outcomes)!=52:
    for j in hand:
        all_possible_outcomes.append(j)

red_cards = set(range(1, 27)) # Assume 26 red cards
face_cards = {11,12,13,24,25,26,37,38,39,50,51,52}
all_cards = set(range(1,53))