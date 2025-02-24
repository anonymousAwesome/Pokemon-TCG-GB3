import pygame
import ui
import mapinfo
import os

pygame.init()
screen = pygame.display.set_mode((640,576))

import character

pygame.display.set_caption("Overworld Exploration")
clock = pygame.time.Clock()

class CurrentMap():
    def __init__(self,current_map_name):
        self.bg_image=current_map_name["bg_image"]
        self.bg_width=self.bg_image.get_width()
        self.bg_height=self.bg_image.get_height()
        self.scaled_bg_image = pygame.transform.scale(self.bg_image, (self.bg_width * 4, self.bg_height * 4))
        self.obstacles=current_map_name["obstacles"]
        self.player_starting_location=current_map_name["player_starting_location"]
    
    def update_map(self,current_map_name):
        self.__init__(current_map_name)

current_map=CurrentMap(mapinfo.test)

player_character=character.Player(
    current_map.player_starting_location[0],
    current_map.player_starting_location[1],
    character.sprites,
    current_map.scaled_bg_image)

#NPC=character.NPC(player_starting_location[0],player_starting_location[1],character.sprites,bg_image)


def render():

    keys = pygame.key.get_pressed()    

    player_character.update(keys,current_map.obstacles)
    #player_character.interact(keys)
    #player_character.step_exits(keys)
    #player_character.interact_exits(keys)

    #NPC.update(keys,obstacles)

    
    camera_x_offset = -max(0, min(current_map.bg_width * 4 - 640, (player_character.rect.centerx - 320)))
    camera_y_offset = -max(0, min(current_map.bg_height * 4 - 576, (player_character.rect.centery - 288)))
    screen.blit(current_map.scaled_bg_image, (camera_x_offset, camera_y_offset))
    #for ob in current_map["obstacles"]:
    #    pygame.draw.rect(screen, (255,0,0), ob.move(camera_x_offset, camera_y_offset))
    player_character.draw(screen, camera_x_offset, camera_y_offset)
    
    #NPC.draw(screen, camera_x_offset, camera_y_offset)
    

    """
    test_dialogue=ui.Dialogue(screen,"Pete Abrams",
    '/media/brendanj/Shared Partition/programming/pokemon tcg monte carlo/pokemon_tcg_fangame/assets/duellists/pete abrams 3.png',
    '''Test1
Test2
Aaaaa aaaa aaaaa aaa aaa aaa 4bbb 3ccc 2ddd 1e 0fffff .''',
    "/media/brendanj/Shared Partition/programming/pokemon tcg monte carlo/pokemon_tcg_fangame/assets/pokemon-emerald.otf")
    
    test_dialogue.render()
    """

    pygame.display.flip()
    clock.tick(60)

if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()