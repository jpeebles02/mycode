#!/usr/bin/python3
  
import random
deck = []

#build deck of cards
suits = ['DIAMOND', 'HEART', 'CLUB', 'SPADE']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
for suit in suits:
    for rank in ranks:
        deck.append(rank + " OF " + suit)

print(f'Your deck of cards: {deck}')

#shuffle deck of cards
random.shuffle(deck)

#print 2 random cards
print("Your cards are:")
for i in range(2):
    #print(deck[i][0] + deck[i][5])
    print(deck[i])
