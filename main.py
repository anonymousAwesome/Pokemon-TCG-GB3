import duel
import pygame
import overworld

class PhaseHandler:
    def __init__(self):
        self.game_phase = "starting"

    def set_game_phase(self, new_phase):
        self.game_phase = new_phase
        '''to-do: add code that checks the new phase against a list of
        possible phases.'''

    def get_game_phase(self):
        return self.game_phase

phase_handler = PhaseHandler()

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #overworld.render()
        #duel.render()
    pygame.quit()