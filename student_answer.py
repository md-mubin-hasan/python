# Python Class 3590
# Lesson 5 Problem 1
# Author: AB2500 (1051343)

import random

class UnoCard(object):
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9
      color: string'''

    def __init__(self, rank, color):
        '''UnoCard(rank, color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        return(str(self.color) + ' ' + str(self.rank))

    def is_match(self, other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        return (self.color == other.color) or (self.rank == other.rank)
    
class ActionCard(UnoCard):
    ''' subclass of Unocard, inherits its attributes of rank 
    and color but adds new attribute called action.
    Has functions to verify if the topcard is any of the action cards.
    '''
    actionList = ['s', 'r', 'd2']
    def __init__(self, action, color, rank):
        if action not in ActionCard.actionList:
           raise ValueError("This is not a valid action card.")
        self.action = action
        super(ActionCard, self).__init__(rank, color)
     
    def __str__(self):
        return (str(self.color) + ' ' + str(self.rank) + ' ' + self.action)
    def isSkip(self):
        return self.action == 's'
    
    def isReverse(self):
        return self.action == 'r'
    
    def isDraw2(self):
        return self.action == 'd2'
    

class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0, color))  # one 0 of each color
            for i in range(2):
                for n in range(1, 10):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n, color))
                ''' appends 2 of each action card of each color into the deck 
                so that 24 new cards are added.
                '''
                for a in ActionCard.actionList:
                    self.deck.append(ActionCard(a,color,i))
        random.shuffle(self.deck)  # shuffle the deck
        

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck)) + ' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self, pile):
        '''UnoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        if len(self.deck) != 0:
            return
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck
        


class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self, deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has ' + str(self.pile[-1]) + ' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self, card):
        '''UnoPile.add_card(card) -> None
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self, name, deck):
        '''UnoPlayer(name, deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self, deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self, card, pile):
        '''UnoPlayer.play_card(card, pile) -> None
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)
        
    
     
    def take_turn(self, deck, pile):
        '''UnoPlayer.take_turn(deck, pile) -> None
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        # print player infov
        print(self.name + ", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        
        matches = [card for card in self.hand if card.is_match(topcard)]
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
                # print the playable cards with their number
                print(str(index + 1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            self.play_card(matches[choice - 1], pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            print("You drew: "+str(newcard))
            if newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")
            input("Press enter to continue.")

def play_uno(numPlayers):
    '''play_uno(numPlayers) -> None
    plays a game of Uno with numPlayers'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []
    for n in range(numPlayers):
        # get each player's name, then create an UnoPlayer
        name = input('Player #' + str(n + 1) + ', enter your name: ')
        playerList.append(UnoPlayer(name,deck))
    # randomly assign who goes first
    currentPlayerNum = random.randrange(numPlayers)
    # play the game
    skip = False
    reverse = False
    
    
    while True:
        # print the game status
        print('-------')
        for player in playerList:
            print(player)
        print('-------')
        topcard = pile.top_card()
        ''' First checks if topcard is an action card.
        If it is, the verification functions from action card class are put in to 
        make sure the action is carried out.
        Boolean variable is assigned to skip and reverse so that the 
        topcard doesn't forever stay the action card 
        when the variable is reassigned to the opposite Boolean value.
        '''
        if isinstance(topcard, ActionCard):
            if topcard.isSkip() and not skip:
                #changes the current player by 2 so that the 3rd person goes instead of the second
                (currentPlayerNum + 1) % numPlayers
                #indicates that the skip card has already been played and the game can move on.
                skip = True
                continue
            #changes the value of skip bool  to false so that it is possible for skip to be played again
            skip = False
            
            if topcard.isReverse():
                #Toggle reverse value of True or false depending on who plays the reverse card
                #if a reverse is already played and another one has just been played, the value is switched
                    #the reverse function then is canceled and the order of players is returned to normal
                reverse = not reverse 
            
            if topcard.isDraw2():
                #current player after the person who put the d2 card is made to take 2 cards
                #reuses the code from skip to remove the current player's turn
                currentPlayerNum.hand.append(random.draw_card(deck, 2))
                (currentPlayerNum + 1) % numPlayers
                skip = True
                continue
            
            skip = False
               
    
        # take a turn
        playerList[currentPlayerNum].take_turn(deck, pile)
        
        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing!")
            break
        # go to the next player
        #before going to next player, if the card is a reverse action card, the order of players is reversed.
        #instead of adding 1 to the playernum, it subtracts 1 and goes in the reverse order until another reverse is played
        if reverse:
            currentPlayerNum = (currentPlayerNum - 1) % numPlayers
        else:
            currentPlayerNum = (currentPlayerNum + 1) % numPlayers
        
        
play_uno(3)
