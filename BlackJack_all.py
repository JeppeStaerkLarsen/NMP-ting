

#import random
from IPython.display import clear_output
import collections
from Modules.Blackjack import Blackjack_mod


#GAME LOGIC
player_one = Blackjack_mod.Player(Blackjack_mod.enter_string(),100)
house = Blackjack_mod.Player('House',0)
new_deck = Blackjack_mod.Deck()
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
            
            if Blackjack_mod.enter_yorn() == 'n':
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
    if Blackjack_mod.enter_yorn() =='n':
        game_on = False
    else:
        first_round = True
        
#clear_output()
print('Game over. Thank you for playing...')


#print("")
    
    
    
    
    
     


    










