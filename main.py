import pygame

pygame.init()
screen = pygame.display.set_mode((640, 576))
clock = pygame.time.Clock()

import overworld
#import duel
import paddlewar

overworld_context=overworld.Context(screen)

paddlewar_context=paddlewar.Context(screen)

#duel_context=duel.Context(screen)


class PhaseHandler:
    def __init__(self):
        self.game_phase = "overworld"

    def set_game_phase(self, new_phase):
        self.game_phase = new_phase

phase_handler = PhaseHandler()

running = True
while running:
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    if phase_handler.game_phase == "overworld":
        overworld_context.update(phase_handler,event_list)
    elif phase_handler.game_phase == "duel":
        duel_context.update(phase_handler,event_list)
    elif phase_handler.game_phase == "paddlewar":
        paddlewar_context.update(phase_handler,event_list)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
