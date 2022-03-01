

import random
from IPython.display import clear_output

class Card:
 
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
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
        '''
        tekst = ''
        for i in self.all_cards:
            if self.all_cards.index(i)==0:
                tekst += str(i) + ' (On hand)'
                tekst += '\n'
            else:
                tekst += str(i) + ' (On the table)'
                tekst += '\n' 
        '''
                
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

#GAME LOGIC
player_one = Player('Juan',100)
house = Player('House',0)
new_deck = Deck()
new_deck.shuffle()


game_on = True
round_on = True
first_round = True  



while game_on:
    while round_on:
        

        #Start ny runde
    
        if first_round:
            clear_output()
            print('{}, you have {} coins left,'.format(player_one.name,player_one.amount))
            bet = player_one.place_bet()
            player_one.all_cards =[]
            house.all_cards =[]
            player_one.add_cards(new_deck.deal_top_card())
            house.add_cards(new_deck.deal_top_card())
            print(player_one)
            print(house)
            first_round = False
        else:
            #print(player_one)
            print('Do you want another card? y/n')
            
            if enter_yorn() == 'n':
                break
            else:
                player_one.add_cards(new_deck.deal_top_card())
                clear_output()
                print(player_one)
                print(house)
        
        if player_one.hand_value() > 21:
            print('BUST!')
            break
        
    
    
    while house.hand_value() <= player_one.hand_value():
        house.add_cards(new_deck.deal_top_card())
        
    
    if player_one.hand_value() <=21:    
        print('House draw:')
        for i in house.all_cards:
            print(i)

    if player_one.hand_value() <=21 and house.hand_value() > 21:
        print('House busts!')
        
    
    if  player_one.hand_value() <= 21 and house.hand_value() <=21 and player_one.hand_value() < house.hand_value() :
        print('{} wins!'.format(house.name))
    elif player_one.hand_value() > 21:
        print('{} wins!'.format(house.name))
    else:     
        print('{} wins {} coins!'.format(player_one.name, bet))
        player_one.amount +=2*bet
        
     
                
    #round_on=False

    
#Tjek om self.amount > 0  
    print('Do you want to play another round? y/n')
    if enter_yorn() =='n':
        game_on = False
    else:
        first_round = True
        
#clear_output()
print('Game over. Thank you for playing...')







'''
Game logic:

WHILE GAME_ON

    if first round 
        1. Deal Player a card from the deck
            a. show player card and coins
            a. Ask player to place bet 
    if second or beyond
        1. Deal Player a card from the deck
            a. show player cards, display visibility
            b. determine if bust or not
        
    If first round


    3. Ask player if it wants another card or stop.
        a. Input
        b. if y go to 1, if n go to 4

    4. House round (write rules for House. Base rules on value of first player card)
        a. arg: player cards

    5. Determine winner, and add amount to their coins

    6. Ask player for another round


'''
print("")
    
    
    
    
    
     


    










