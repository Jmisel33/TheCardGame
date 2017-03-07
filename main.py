

import random
from card import Card
from deck import Deck




print("The Game is Black Jack. The Rules are simple, Its you vs. the dealer. You will be delt two cards and if you would like to get another type hit or if you'd like to stay type stay. Got it? ")

raw_input("Press enter to start the game")

print("Dealers hand")
dealershand = Deck()
dealershand. Shuffle()
currentcard = dealershand. TakeFromTop()
currentcard. displayCard()
currentcard = dealershand. TakeFromTop()
currentcard. displayCard()
raw_input("Would you like to hit for another card?")
if ("yes"):
    currentcard = dealershand. TakeFromTop()
    currentcard. displayCard()



print("Player Ones Deal")
p1hand = Deck()
p1hand. Shuffle()
currentcard = p1hand. TakeFromTop()
currentcard. displayCard()
currentcard = p1hand. TakeFromTop()
currentcard. displayCard()

raw_input("Would you like to hit for another card?")
if ("yes"):
    currentcard = dealershand. TakeFromTop()
    currentcard. displayCard()
