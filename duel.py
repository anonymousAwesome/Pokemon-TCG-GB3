import logging

import main

class Duel:
    def __init__(self,phase_handler,user_won_starting_coin):
        self.phase_handler=phase_handler
        self.phase_handler.set_game_phase("duelling")
        if user_won_starting_coin is True:
            self.turn="player"
        elif user_won_starting_coin is False:
            self.turn="computer"
        else:logging.error(f"Expected boolean, got {user_won_starting_coin}")
            
    def advance_turn(self):
        if self.turn=="player":
            self.turn="computer"
        elif self.turn=="computer":
            self.turn="player"
        else:
            logging.error(f"Unexpected turn value: {self.turn}")

    def end_duel(self):
        self.phase_handler.set_game_phase("club")

class Player:
    def __init__(self,duel_handler,prizes):
        self.duel_handler=duel_handler
        self.prizes=prizes

    def lose_prize(self,quantity=1):
        self.prizes-=quantity
        if self.prizes<=0:
            self.duel_handler.end_duel()