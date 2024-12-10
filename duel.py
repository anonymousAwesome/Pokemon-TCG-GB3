import logging

import main

import card_deck_classes as cdc

class DuelManager:
    def __init__(self,phase_handler,prizes):
        self.prizes=prizes
        self.phase_handler=phase_handler
        self.phase_handler.set_game_phase("duelling")
        self.turn=None

    def user_won_starting_coin(self, coin_results:bool):
        if coin_results is True:
            self.turn="player"
        elif coin_results is False:
            self.turn="computer"
        else:logging.error(f"Unexpected value in DuelManager.__init__() -- expected boolean for user_won_starting_coin, got {user_won_starting_coin}")
      
    def advance_turn(self):
        if not self.turn:
            logging.error(f"Can't advance the turns; haven't run user_won_starting_coin() yet.")
        if self.turn=="player":
            self.turn="computer"
        elif self.turn=="computer":
            self.turn="player"
        else:
            logging.error(f"Unexpected value in DuelManager.advance_turn() -- expected \"player\" or \"computer\", got {self.turn}")

    def end_duel(self):
        self.phase_handler.set_game_phase("club")

class Player:
    def __init__(self,duel_handler):
        self.duel_handler=duel_handler
        self.prizes=duel_handler.prizes
        self.deck=cdc.Deck(self)
        self.active=cdc.Active(self)
        self.bench=cdc.Bench(self)
        self.hand=cdc.Hand(self)
        self.discard_pile=cdc.DiscardPile(self)
        self.choices={}
        self.location="starting"

    def lose_prize(self,quantity=1):
        self.prizes-=quantity
        if self.prizes<=0:
            self.duel_handler.end_duel()
    
    def collect_choices(self):
        if self.location=="starting":
            self.choices={0: "hand", 1: "check", 2: "retreat", 3: "attack", 4: "pokemon power", 5: "end turn"}
        if self.location=="checking hand":
            self.choices={}
            for i,card in enumerate(self.hand):
                self.choices[i]=card.name
            self.choices[i+1]="cancel"

    def request_decision(self):
        for i in range(len(self.choices)):
            print(f"{i}: {self.choices[i]}")
        user_choice=int(input())
        if user_choice==0:
            self.location="checking hand"