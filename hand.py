'''hand module implements hand class and objects for each player,
this will allow players to keep track of the value of their hands, adjust for
aces and also access their hand as a list'''
from card import values

class Hand:
    '''hand classes generates a list of cards per
     player and keeps track of value and aces'''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        '''card passed in from the deck, implements the deal method used in deck class'''
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Aces':
            self.aces += 1


    def adjust_for_ace(self):
        '''this will adjust the value of the hand should it have aces and have
        value over 21'''
        #if total value > 21 and still have an ace
        #then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1
