'''the deck class generates a deck and allows for the removal of cards from the deck,
	dealing'''
from random import shuffle
from card import suits
from card import ranks
from card import Card


class Deck:
    '''as described above'''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        '''uses the shufle method from random to shuffle the deck'''
        shuffle(self.deck)

    def deal(self):
        '''sets the single_card variable to the top item from the list '''
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffle()
print(test_deck)
