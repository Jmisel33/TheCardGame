

import random
from card import Card
from deck import Deck

score = 0



print("The Game is Black Jack. The Rules are simple, Its you vs. the dealer. You will be delt two cards and if you would like to get another type hit or if you'd like to stay type stay. Got it? ")

raw_input("Press enter to start the game")

print("Dealers hand")
raw_input("Press enter for the deal")
dealershand = Deck()
dealershand. Shuffle()
currentcard = dealershand. TakeFromTop()
currentcard. displayCard()
currentcard = dealershand. TakeFromTop()
currentcard. displayCard()




raw_input("Press enter for the deal")
print("Player Ones Deal")


p1hand = Deck()
p1hand. Shuffle()
currentcard = p1hand. TakeFromTop()
score = currentcard.orderRank + score
currentcard. displayCard()
currentcard = p1hand. TakeFromTop()
score = currentcard.orderRank + score
currentcard. displayCard()
extracard = raw_input("Would you like to hit for another card?")
if extracard == "yes":
    currentcard = p1hand. TakeFromTop()
    score = currentcard.orderRank + score
    currentcard. displayCard()

print(score)
if score > 21:
    print("BUST")

