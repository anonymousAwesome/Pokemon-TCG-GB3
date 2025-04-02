import pygame

pygame.init()
screen = pygame.display.set_mode((640, 576))
clock = pygame.time.Clock()

import duel
import overworld
import paddlewar

class PhaseHandler:
    def __init__(self):
        self.game_phase = "overworld"
        self.set_duel_data()
        self.set_difficulty()
        self.won_last_duel=False
    
    def set_difficulty(self,difficulty="standard"):
        self.difficulty=difficulty
        
    def set_duel_data(self,player_deck=[], opponent_deck=[] ,final_boss=False, background_image=None):
        self.player_deck=player_deck
        self.opponent_deck=opponent_deck
        self.final_boss=final_boss
        self.background_image=background_image
  
    def set_game_phase(self, new_phase):
        self.game_phase = new_phase
        if self.game_phase=="duel":
            self.won_last_duel=False
            #currently unnecessary for story mode, but will become
            #necessary when adding duelling code
            #
            #if self.player_deck==[] or self.opponent_deck==[] or self.background_image==None:
            #    print("Error: duel information not loaded. Returning to overworld.")
            #    print(f"{self.player_deck=},{self.opponent_deck=},{self.background_image=}")
            #    self.game_phase = "overworld"

phase_handler = PhaseHandler()


overworld_context=overworld.Context(screen,phase_handler)

paddlewar_context=paddlewar.Context(screen,phase_handler)

duel_context=duel.Context(screen,phase_handler)



running = True
while running:
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    if phase_handler.game_phase == "overworld":
        overworld_context.update(event_list)
    elif phase_handler.game_phase == "duel":
        duel_context.update(event_list)
    elif phase_handler.game_phase == "paddlewar":
        paddlewar_context.update(event_list)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
