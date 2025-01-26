import pygame
import ui
import player

#to-do:
#load "new game, save/load, delete save" menu. Possibly with TCG Island background.
#for new game, pull up character customization ui
#then change phase to "overworld" or possibly "cutscene", trigger the first cutscene.

pygame.init()
screen = pygame.display.set_mode((640,576))
pygame.display.set_caption("Game Start")
clock = pygame.time.Clock()

def render():
    pass


if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()