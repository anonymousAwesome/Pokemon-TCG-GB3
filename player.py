'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

class PlayerData:
    def __init__(self):
        self.card_pool=[]
        self.event_flags={
        "first event":False
        }
        self.player_name=None
        self.removed_npcs=set()
        
        self.currently_greyscale=False
        
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
        
    def remove_npc(self,npc):
        self.removed_npcs.add(npc)
    
    def undelete_npc(self,npc):
        self.removed_npcs.remove(npc)
    
    def toggle_greyscale(self):
        self.currently_greyscale=not self.currently_greyscale