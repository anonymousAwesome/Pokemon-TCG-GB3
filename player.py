'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

class PlayerData:
    def __init__(self):
        self.cardpool=[]
        self.event_flags={
        "first event":False
        }