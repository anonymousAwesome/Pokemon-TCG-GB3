import mapinfo

'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

class PlayerData:
    def __init__(self,card_pool=[],event_flags=None,player_name="",removed_npcs=set(),currently_greyscale=False,current_map_class=mapinfo.MasonCenter):
        self.card_pool=[]
        if not event_flags:
            self.event_flags={
            "opening_cutscene":False,
            "mason disappeared":False
            }
        self.player_name=player_name
        self.removed_npcs=removed_npcs
        
        self.currently_greyscale=currently_greyscale
        self.current_map_class=current_map_class

        
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