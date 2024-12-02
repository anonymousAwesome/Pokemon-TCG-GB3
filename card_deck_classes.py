'''
Contains the definitions for cards and decks
'''


class Card:
    '''I definitely need to split out the aspects of Card that only apply 
    to Pokemon.'''
    def __init__(self,name,hp,owner):
        self.name=name
        self.hp=hp
        self.owner=owner
        
    def attack(self, opponent, damage):
        if damage<0:
            damage=0
        opponent.hp-=damage
        if opponent.hp<=0:
            opponent.hp=0
            self.owner.lose_prize()
    

class CardCollection:
    def __init__(self,cards=None):
        self.cards=[cards]
    
    def __iter__(self):
        return iter(self.cards)
        
        
