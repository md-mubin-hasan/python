import random

class UnoCard:
    '''represents an Uno card'''

    def __init__(self,rank,color):
        '''UnoCard(rank,color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color
        self.wildcolor = None

    def __str__(self):
        '''str(Unocard) -> str'''
        if self.rank in ['wild','wild draw four']:
            if self.wildcolor is None:
                return self.rank
            return self.rank + ' (' + self.wildcolor + ' color)'
        return(str(self.color)+' '+str(self.rank))

    def is_match(self,other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if self can be played after other, False otherwise.'''
        # wild cards may be played after any card, but the card after must match
        # the wildcolor or be wild itself
        return ((self.color in (other.color, other.wildcolor))
                or (self.rank == other.rank)
                or (self.rank == 'wild') or (self.rank == 'wild draw four'))

    def is_color_match(self,other):
        '''UnoCard.is_color_match(UnoCard) -> boolean
        returns True if colors match, False otherwise'''
        return (self.color == other.color)

    def get_rank(self):
        '''UnoCard.get_action() -> str
        returns the rank of the card'''
        return self.rank

    def set_wild_color(self,color):
        '''UnoCard.set_wild_color(color)
        sets the wild card color'''
        self.wildcolor = color

    def clear_wild_color(self):
        '''UnoCard.clear_wild_color(color)
        clears the wild card color'''
        self.wildcolor = None

class UnoDeck:
    '''represents a deck of Uno cards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0,color))  # one 0 of each color
            for i in range(2):
                for n in range(1,10):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n,color))
                for action in ['skip','reverse','draw two']:
                    self.deck.append(UnoCard(action,color))
        # wild cards
        for i in range(4):
            self.deck.append(UnoCard('wild',''))
            self.deck.append(UnoCard('wild draw four',''))
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck))+' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()  # deal from the "bottom"

    def reset_deck(self,pile):
        '''UnoDeck.reset_deck(pile)
        resets the deck from the pile'''
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno'''

    def __init__(self,deck):
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

    def add_card(self,card):
        '''UnoPile.add_card(card)
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
    '''represents a player of Uno'''

    def __init__(self,name,isHuman,deck):
        '''UnoPlayer(name,isHuman,deck -> UnoPlayer
        creates a new player with an new hand'''
        self.name = name
        self.isHuman = isHuman
        if not isHuman:
            self.name += '(Computer)'
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name)+' has '+str(len(self.hand))+' cards.'

    def is_human(self):
        '''UnoPlayer.is_human() -> bool
        returns True if human, False if computer'''
        return self.isHuman

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += '  ' + str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self,deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self,card,pile):
        '''UnoPlayer.play_card(card,pile)
        plays a card from the player hand to the pile
        CAUTION: does not check if the play is legal!'''
        pile.top_card().clear_wild_color()  # clear any wildcolor on top card
        self.hand.remove(card)
        pile.add_card(card)
        # get player choice of color for a wild card
        if card.get_rank() in ['wild','wild draw four']:
            if self.isHuman:  # humans get to choose
                print('What color do you choose?')
                colorChoice = ''
                while colorChoice not in ['red','blue','yellow','green']:
                    colorChoice = input('Pick one of red, blue, yellow, or green: ')
            else:  # computer player picks at random
                colorChoice = random.choice(['red','blue','yellow','green'])
            card.set_wild_color(colorChoice)

    def take_turn(self,deck,pile):
        '''UnoPlayer.take_turn(deck,pile) -> str
        takes the player turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile
        returns rank of card played'''
        # print player info
        print(self.name+", it's your turn.")
        print(pile)
        if self.isHuman:  # only show hand to human player
            print("Your hand: ")
            print(self.get_hand())
        else:
            input("Press enter for the computer to play.")
        # get a list of cards that can be played
        topcard = pile.top_card()
        # draw four can only be played if there's no matching color card
        drawFourOK = (len([card for card in self.hand if \
                           card.is_color_match(topcard)]) == 0)
        # collect matches -- check for wild draw four playability
        matches = [card for card in self.hand if card.is_match(topcard) \
                   and (card.get_rank() != 'wild draw four' or drawFourOK)]
        if len(matches) > 0:  # can play
            if self.isHuman:  # let the human select
                counter = 1   # to number the cards that can be played
                print("These cards can be played:")
                for card in matches:
                    # print the playable cards with their number
                    print(str(counter)+": "+str(card))
                    counter += 1
                # get player choice of which card to play
                choice = 0
                while choice < 1 or choice > len(matches):
                    choicestr = input("Which do you want to play? ")
                    if choicestr.isdigit():
                        choice = int(choicestr)
            else:  # computer player, pick a random card
                choice = random.randrange(1,len(matches)+1)
            # play the chosen card from hand, add it to the pile
            chosencard = matches[choice-1]
            if not self.isHuman:  # print the computer's chosen card
                print(self.name+" plays "+str(chosencard))
            self.play_card(chosencard,pile)
            return chosencard.get_rank()
        else:  # can't play
            if self.isHuman:
                print("You can't play, so you have to draw.")
                input("Press enter to draw.")
            else:
                print(self.name+" can't play and must draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            if self.isHuman:
                print("You drew: "+str(newcard))
            if newcard.is_match(topcard): # can be played
                print("The drawn card can be played")
                self.play_card(newcard,pile)
                rank = newcard.get_rank()
            else:   # still can't play
                print("Still can't play.")
                rank = None
            input("Press enter to continue.")
            return rank

def play_uno(numPlayers):
    '''play_uno(numPlayers)
    plays a game of Uno
    numPlayers is an int for the number of players'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []
    for n in range(numPlayers):
        # get each player name, then create an UnoPlayer
        name = input('Player #'+str(n+1)+', enter your name: ')
        computerPlayer = 'x'
        while computerPlayer not in 'yn':
            computerPlayer = input('Is this a computer player (y/n)? ')
        playerList.append(UnoPlayer(name,computerPlayer=='n',deck))
    # randomly assign who deals
    currentPlayerNum = random.randrange(numPlayers)
    print(playerList[currentPlayerNum].get_name()+" is the dealer.")
    # set up direction (for reversing)
    direction = 1
    # first card actions
    firstCardAction = pile.top_card().get_rank()
    while firstCardAction == 'wild draw four':
        # draw another card
        pile.add_card(deck.deal_card())
        firstCardAction = pile.top_card().get_rank()
    print("The initial card on the pile is: "+str(pile.top_card()))
    if firstCardAction == 'skip':
        currentPlayerNum = (currentPlayerNum + direction) % numPlayers
        print(playerList[currentPlayerNum].get_name()+" gets skipped!")
    elif firstCardAction == 'reverse':
        print("Reverse direction!")
        direction *= -1
    elif firstCardAction == 'draw two':
        currentPlayerNum = (currentPlayerNum + direction) % numPlayers
        print(playerList[currentPlayerNum].get_name()+" must draw 2!")
        input("Press enter to draw.")
        for i in range(2):
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = playerList[currentPlayerNum].draw_card(deck)
            if playerList[currentPlayerNum].is_human():
                print("You drew: "+str(newcard))
    elif firstCardAction == 'wild':
        # get player choice of color for a wild card
        if playerList[currentPlayerNum].is_human():  # humans get to choose
            print('What color do you choose?')
            colorChoice = ''
            while colorChoice not in ['red','blue','yellow','green']:
                colorChoice = input('Pick one of red, blue, yellow, or green: ')
        else:  # computer player picks at random
            colorChoice = random.choice(['red','blue','yellow','green'])
        pile.set_wild_color(colorChoice)
    # go to the first player
    currentPlayerNum = (currentPlayerNum + direction) % numPlayers
    # play the game
    while True:
        # print the game status
        print('-------')
        for player in playerList:
            print(player)
        print('-------')
        # take a turn
        action = playerList[currentPlayerNum].take_turn(deck,pile)
        # check for a winner
        if playerList[currentPlayerNum].has_won():
            print(playerList[currentPlayerNum].get_name()+" wins!")
            print("Thanks for playing!")
            break
        # perform action, if any
        if action == 'skip':
            currentPlayerNum = (currentPlayerNum + direction) % numPlayers
            print(playerList[currentPlayerNum].get_name()+" gets skipped!")
        elif action == 'reverse':
            print("Reverse direction!")
            direction *= -1
        elif action == 'draw two':
            currentPlayerNum = (currentPlayerNum + direction) % numPlayers
            print(playerList[currentPlayerNum].get_name()+" must draw 2!")
            input("Press enter to draw.")
            for i in range(2):
                # check if deck is empty -- if so, reset it
                if deck.is_empty():
                    deck.reset_deck(pile)
                # draw a new card from the deck
                newcard = playerList[currentPlayerNum].draw_card(deck)
                if playerList[currentPlayerNum].is_human():
                    print("You drew: "+str(newcard))
        elif action == 'wild draw four':
            currentPlayerNum = (currentPlayerNum + direction) % numPlayers
            print(playerList[currentPlayerNum].get_name()+" must draw 4!")
            input("Press enter to draw.")
            for i in range(4):
                # check if deck is empty -- if so, reset it
                if deck.is_empty():
                    deck.reset_deck(pile)
                # draw a new card from the deck
                newcard = playerList[currentPlayerNum].draw_card(deck)
                if playerList[currentPlayerNum].is_human():
                    print("You drew: "+str(newcard))
        # go to the next player
        currentPlayerNum = (currentPlayerNum + direction) % numPlayers
play_uno(3)
