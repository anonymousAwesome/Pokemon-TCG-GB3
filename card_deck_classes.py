'''
Contains the definitions for cards and decks
'''


class Card:
    '''I definitely need to split out the aspects of Card that only apply 
    to Pokemon.'''
    def __init__(self,name,hp,owner=None):
        self.name=name
        self.hp=hp
        self.owner=owner
        
    def attack(self, opponent, damage):
        if damage<0:
            damage=0
        opponent.hp-=damage
        if opponent.hp<=0:
            opponent.hp=0
            self.owner.prizes-=1
    

class CardCollection:
    def __init__(self,cards=None):
        self.cards=[cards]
    
    def __iter__(self):
        return iter(self.cards)
        
        
class Player:
    #Just put it here for now. Later, consider moving somewhere it would make more sense.
    def __init__(self,prizes,owned_pokemon:list=[]):
        self.prizes=prizes
        self.owned_pokemon=owned_pokemon