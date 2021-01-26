'''chips class is for gambling tings'''

class Chips:
    '''chips class is for keeping track fo the amount of chips a player has and adjusting'''
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        '''if a player wins a bet then their total pot of chips is increased by their
        bet'''
        self.total += self.bet

    def lose_bet(self):
        '''and vice versa, if a player loses a bet then their total pot is reduced
        by the amount that they bet'''
        self.total -= self.bet
