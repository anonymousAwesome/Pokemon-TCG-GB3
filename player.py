'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

class PlayerData:
    def __init__(self):
        self.cardpool=[]
        self.event_flags={
        "first event":False
        }
        self.player_name=None
    def set_flag(self,flagname):
        self.event_flags[flagname]=True
    
    def add_cards(self,cards):
        if isinstance(cards,list):
            for card in cards:
                self.cardpool.append(card)
        else:
            raise TypeError("expected a list")
    
    def display_cards(self):
        print(self.cardpool)
        
    def set_name(self,name):
        self.player_name=name