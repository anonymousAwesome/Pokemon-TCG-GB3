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
    def __init__(self,current_map_info):
        self.current_map_info=current_map_info
        self.bg_image=current_map_info["bg_image"]
        self.bg_width=self.bg_image.get_width()
        self.bg_height=self.bg_image.get_height()
        self.bg_image = pygame.transform.scale(self.bg_image, (self.bg_width * 4, self.bg_height * 4))
        self.obstacles=current_map_info["obstacles"]
        self.player_starting_location=current_map_info["player_starting_location"]
    
    def change_map(self,new_map_info):
        self.__init__(new_map_info)

current_map=CurrentMap(mapinfo.mason_center)

player_character=character.Player(
    current_map.player_starting_location[0],
    current_map.player_starting_location[1],
    character.sprites,
    current_map.bg_image)

#NPC=character.NPC(player_starting_location[0],player_starting_location[1],character.sprites,bg_image)


def render():
    keys = pygame.key.get_pressed()    
    player_character.update(keys,current_map.obstacles)

    if "step triggers" in current_map.current_map_info:
        for trigger in current_map.current_map_info["step triggers"]:
            if trigger[0].contains(player_character.rect):
                player_character.pixels_remaining=0
                trigger[1](player_character,current_map)
                player_character.bg_image=current_map.bg_image
    if "interact self triggers" in current_map.current_map_info:
        for trigger in current_map.current_map_info["interact self triggers"]:
            if trigger[0].contains(player_character.rect):
                if keys[character.AFFIRM_KEY]:
                    player_character.pixels_remaining=0
                    trigger[1](player_character,current_map)
                    player_character.bg_image=current_map.bg_image
    #player_character.step_trigger(keys)
    #player_character.interact_self(keys)
    #player_character.interact_front(keys)

    #NPC.update(keys,obstacles)

    
    camera_x_offset = -max(0, min(current_map.bg_width * 4 - 640, (player_character.rect.centerx - 320)))
    camera_y_offset = -max(0, min(current_map.bg_height * 4 - 576, (player_character.rect.centery - 288)))
    screen.blit(current_map.bg_image, (camera_x_offset, camera_y_offset))
    #for ob in current_map.obstacles:
    #    pygame.draw.rect(screen, (255,0,0), ob.move(camera_x_offset, camera_y_offset))
    player_character.draw(screen, camera_x_offset, camera_y_offset)

    temp_interact_front_rect=player_character.rect.copy()
    if player_character.facing_direction=="down":
        temp_interact_front_rect.y+=character.TILE_SIZE
    if player_character.facing_direction=="up":
        temp_interact_front_rect.y-=character.TILE_SIZE
    if player_character.facing_direction=="left":
        temp_interact_front_rect.x-=character.TILE_SIZE
    if player_character.facing_direction=="right":
        temp_interact_front_rect.x+=character.TILE_SIZE
    
    pygame.draw.rect(screen, (255,0,0), temp_interact_front_rect.move(camera_x_offset, camera_y_offset))

    
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