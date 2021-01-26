from card import *
from deck import *
from hand import *
from chips import *


def take_bet(chips):
    '''take_bet implements some basic error handling in order to
    ask the player how much they'd like to bet'''
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet: "))
        except:
            print("Sorry, please provide an integer (number)")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have {chips.total}')
