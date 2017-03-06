import random
from card import Card
from deck import Deck

print("The Game is Black Jack. The Rules are simple, Its you vs. the dealer. You will be delt two cards and if you would like to get another type hit or if you'd like to stay type stay. Got it? ")

raw_input("Press enter to start the game")

dealershand = Deck()
dealershand. Shuffle()
currentcard = dealershand. TakeFromTop()



p1hand = Deck()
p1hand. Shuffle()
p1hand. TakeFromTop()