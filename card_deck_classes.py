import logging
import random

'''
Contains the definitions for cards and decks
'''

class Card:
    def __init__(self, name,cardset,owner):
        self.name = name
        self.cardset=cardset
        self.owner=owner

''' At some point I think I'm likely to need a function that will check 
to see if a card is in any CardCollections.'''

class Trainer(Card):
    def __init__(self, name, cardset, owner):
        super().__init__(name, cardset, owner)

class Energy(Card):
    def __init__(self, name, cardset, owner):
        super().__init__(name, cardset, owner)

class Pokemon(Card):
    def __init__(self, name, cardset, owner, energy_type, evolution_level, hp, attack_cost, attack_dmg, retreat_cost, weakness=None, resistance=None,evolves_from=None):
        super().__init__(name,cardset, owner)
        self.energy_type=energy_type
        self.evolution_level=evolution_level
        self.hp = hp
        self.attack_cost=attack_cost
        self.attack_dmg = attack_dmg #this will need to go at some point
        self.retreat_cost = retreat_cost
        self.evolves_from=evolves_from
        self.effects=[]
        if weakness:
            self.effects.append(weakness_effect(weakness))
        if resistance:
            self.effects.append(resistance_effect(resistance))
        self.attached=CardCollection(owner)

        self.stored_pre_evolution=CardCollection(owner)

    def attack(self, opponent): #this will probably need replacing as well
        temp_dmg=self.attack_dmg
        if resistance_effect(self.energy_type) in opponent.effects:
            temp_dmg-=30
        if defender() in opponent.effects:
            temp_dmg-=20
        if temp_dmg<0:
            temp_dmg=0
        if weakness_effect(self.energy_type) in opponent.effects:
            temp_dmg*=2
        opponent.hp-=temp_dmg
        if opponent.hp<=0:
            opponent.hp=0
            self.owner.lose_prize()

    def attach_card(self,card):
        print(card)
        move_cards_to_from(card, self.attached)
        print(self.attached.cards)
        #may need an extra function to return just the energy cards
    
    def evolve(self, evolution_card,location):
        move_cards_to_from(self,evolution_card.stored_pre_evolution,location)
        move_cards_to_from(evolution_card,location)

class CardCollection:
    def __init__(self, owner, cards=None):
        self.owner=owner
        if cards is None:
            self.cards=[]
        elif isinstance(cards, Card):
            self.cards=[cards]
        elif isinstance(cards, list):
            self.cards=cards
        else:
            logging.error(f"Expected card or list of cards, got {cards}")


    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        #allows iteration: for card in cardcollection
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]


class Deck(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(owner, cards)

    def shuffle(self):
        random.shuffle(self.cards)

class Active(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(owner,cards)

class Bench(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(owner,cards)

class Hand(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(owner,cards)

class DiscardPile(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(owner,cards)


# stubbed effects, replace later
#
# "_effect" is redundant and should be removed, but then it might
# overshadow the weakness/resistance argument in the Pokemon class.

def defender():
    return("defender")

def weakness_effect(type):
    return(f"weakness: {type}")

def resistance_effect(type):
    return(f"resistance: {type}")



def move_cards_to_from(cardlist, destination_location,prev_location=None):
    if isinstance(cardlist, Card):
        cardlist=[cardlist]
    if isinstance(cardlist, list):
        for card in cardlist:
            destination_location.cards.append(card)
            if prev_location:
                prev_location.cards.remove(card)
    else:
        logging.error(f"Expected card or list of cards, got {cardlist}")