
import random

class Card:
 
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    
    def __init__(self,suit,rank):

        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit



class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.all_cards=[]
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.all_cards.append(Card(suit,rank))
                
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_top_card(self):
        return self.all_cards.pop(0)





class Player: #Player object has name, amount and a hand
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.all_cards = []
        
    def top_card(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,cards): #Pass a list of cards or a single card
        
        if type(cards) == type([]):
            return self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
    
    def place_bet(self): #Pass a bet size 
        valid_bet = False
        
        while not valid_bet: 
            bet_amount = enter_int()
        
            if self.amount < bet_amount:
                print('Thats too much. You only have {} coins left!'.format(self.amount))
            else:
                valid_bet = True
                print('You bet {} coins'.format(bet_amount))
                self.amount -= bet_amount
                return bet_amount
    
    def hand_value(self):
        ## calculate Blackjack sum.
        # if no ace --> sum
        # if aces --> determine max value for sum
        num_ace = 0
        a=[]
        for i in self.all_cards:
            a.append(i.value)
        num_ace = a.count(11)
        val = sum(a)

        while num_ace > 0:
            if val <= 21:
                break
            else:
                num_ace -= 1
                val -= 10
            
        return val
                 
            
    def __str__(self):
        tekst = ''
        for i in self.all_cards:
                tekst += str(i) 
                tekst += '\n'
        
        
        #blok til skjulte kort etc
        
        #tekst = ''
        #for i in self.all_cards:
        #    if self.all_cards.index(i)==0:
        #        tekst += str(i) + ' (On hand)'
        #        tekst += '\n'
        #    else:
        #        tekst += str(i) + ' (On the table)'
        #        tekst += '\n' 
        

        return 'Player {}\nCards:\n{}Hand value: {}\n '.format(self.name,tekst, self.hand_value())

def enter_int():
    while True:
        try:
            whole_num=int(input('How many coins do you wish to bet?: '))
        except:
            print('please enter a whole number of coins')
        else:
            return whole_num

def enter_yorn():
    while True:
        try:
            yorn=input()
            yornl=yorn.lower()
            if yornl != 'y' and yorn != 'n':
                print('please enter y or n')
                continue
        except:
            print('please enter y or n')
        else:
            return yornl

def enter_string():
    while True:
        try:
            name =input('Enter your name: ')
            namel =name.capitalize()
        except:
            print('please enter a valid name')
        else:
            return namel
