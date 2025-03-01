import pygame
import os

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()


class CurrentMap():
    def __init__(self,map_name):
        self.bg_image=pygame.image.load(os.path.join("..","assets", "maps", map_name+".png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

current_map=CurrentMap("mason center")


if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(current_map.bg_image, (0,0))
        pygame.display.flip()
        clock.tick(60)