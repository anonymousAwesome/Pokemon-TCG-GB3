import pygame
import os

class CurrentBG():
    def __init__(self,map_name):
        self.bg_image=pygame.image.load(os.path.join("..","assets", "maps", map_name+".png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

current_map=CurrentBG("mason center")
