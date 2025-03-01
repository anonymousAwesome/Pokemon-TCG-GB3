import pygame
import mapinfo
import os
import player
pygame.init()
screen = pygame.display.set_mode((640,576))

import ui
import character

pygame.display.set_caption("Overworld Exploration")
clock = pygame.time.Clock()

input_lock=False
current_dialogue=None


#class CurrentMap():
#...
        self.obstacles=current_map_info["obstacles"]
    
    def change_map(self,player_character,new_map_info,new_x,new_y,new_facing=None):
        self.__init__(new_map_info)
        player_character.rect.x=new_x
        player_character.rect.y=new_y
        if new_facing:
            player_character.facing_direction=new_facing
        player_character.pixels_remaining=0
        player_character.bg_image=self.bg_image
        


#NPC_sprites=character.load_sprites_from_sheet(character.spritesheet, 12)
#NPC=character.NPC(256,256,NPC_sprites)


def render(input_lock, current_dialogue, event_list):
    
    keys = pygame.key.get_pressed()    
    if not input_lock:

        player_character.update(keys,current_map.obstacles)

        if "step exit triggers" in current_map.current_map_info:
            for trigger in current_map.current_map_info["step exit triggers"]:
                if trigger[0].contains(player_character.rect):
                    if "direction" in trigger[1]:
                        current_map.change_map(player_character, getattr(mapinfo,trigger[1]["mapname"]), trigger[1]["x"], trigger[1]["y"],trigger[1]["direction"])
                    else:
                        current_map.change_map(player_character, getattr(mapinfo,trigger[1]["mapname"]), trigger[1]["x"], trigger[1]["y"])

        if "interact self exit triggers" in current_map.current_map_info:
            for trigger in current_map.current_map_info["interact self exit triggers"]:
                if trigger[0].contains(player_character.rect):
                    for event in event_list:
                        if event.type==pygame.KEYDOWN:
                            if event.key==character.AFFIRM_KEY:
                                if "direction" in trigger[1]:
                                    current_map.change_map(player_character, getattr(mapinfo,trigger[1]["mapname"]), trigger[1]["x"], trigger[1]["y"],trigger[1]["direction"])
                                else:
                                    current_map.change_map(player_character, getattr(mapinfo,trigger[1]["mapname"]), trigger[1]["x"], trigger[1]["y"])

        #player_character.interact_front(keys)

        #NPC.update(keys,current_map.obstacles)

    


    #show_obstacles=True
    show_obstacles=False
    
    if show_obstacles:
        for ob in current_map.obstacles:
            red_rect = pygame.Surface((ob.width,ob.height))
            red_rect.set_alpha(200)
            red_rect.fill((255,0,0))
            screen.blit(red_rect, ob.move(camera_x_offset, camera_y_offset))

    #NPC.draw(screen, camera_x_offset, camera_y_offset)

    temp_interact_front_rect=player_character.rect.copy()
    if player_character.facing_direction=="down":
        temp_interact_front_rect.y+=character.TILE_SIZE
    if player_character.facing_direction=="up":
        temp_interact_front_rect.y-=character.TILE_SIZE
    if player_character.facing_direction=="left":
        temp_interact_front_rect.x-=character.TILE_SIZE
    if player_character.facing_direction=="right":
        temp_interact_front_rect.x+=character.TILE_SIZE
    
    #pygame.draw.rect(screen, (255,0,0), temp_interact_front_rect.move(camera_x_offset, camera_y_offset))

    if not input_lock:
        if "tcg club names" in current_map.current_map_info:
            for trigger in current_map.current_map_info["tcg club names"]:
                if trigger[0].colliderect(player_character.rect):
                    ui.club_name_render(screen,trigger[1])

        if "interact object text" in current_map.current_map_info:
            for trigger in current_map.current_map_info["interact object text"]:
                if trigger[0].contains(temp_interact_front_rect):
                    for event in event_list:
                        if event.type==pygame.KEYDOWN:
                            if event.key==character.AFFIRM_KEY:
                                input_lock=True
                                if len(trigger)>=3:
                                    if "player_condition" in trigger[2]:
                                        if getattr("player",trigger[2]["player_condition"]):
                                            current_dialogue=ui.Dialogue(screen, **trigger[1])
                                else:
                                    current_dialogue=ui.Dialogue(screen, **trigger[1])

    elif input_lock:
        if current_dialogue:
            current_dialogue.render(event_list)
        else:
            input_lock=False
            current_dialogue=None


    pygame.display.flip()
    clock.tick(60)
    return input_lock, current_dialogue

if __name__=="__main__":
    running = True
    while running:
        event_list=list(pygame.event.get())
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        input_lock, current_dialogue=render(input_lock, current_dialogue,event_list)
    pygame.quit()