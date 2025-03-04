import pygame
import characters
import os
import functools
import overworld_event_managers as oem

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import ui
import map_managers
import mapinfo


spritesheet_yellow_path = os.path.join("assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet_crystal_path = os.path.join("assets","npc sprites","pokemon crystal sprites recolored.png")
spritesheet_tcg2_path = os.path.join("assets","npc sprites","pokemon tcg2 sprites.png")

spritesheet_yellow=pygame.image.load(spritesheet_yellow_path).convert_alpha()
spritesheet_crystal=pygame.image.load(spritesheet_crystal_path).convert_alpha()
spritesheet_tcg2=pygame.image.load(spritesheet_tcg2_path).convert_alpha()

pc_sprite = characters.load_sprites_from_sheet(spritesheet_tcg2,0)

player_character=characters.Player(448,832, pc_sprite)

map_holder=map_managers.CurrentMapContainer(mapinfo.MasonCenter,screen)

current_dialogue=ui.Dialogue(screen,"")

collision_manager=map_managers.CollisionManager(map_holder.current_map.bg_image, player_character, map_holder.current_map.obstacles)

class TempTriggerList():
    '''called when the player moves into a new map, so I'm not 
    instantiating the trigger class 60 times a second.'''
    def __init__(self,temp_list=[]):
        self.temp_list=temp_list

    def generate_temp_trigger_list(self,map_holder,player_character):
        temp_list=[]
        for trigger in map_holder.current_map.step_exit_triggers:
            temp_list.append(trigger(player_character))
        self.temp_list=temp_list


temp_trigger_list=TempTriggerList()

temp_trigger_list.generate_temp_trigger_list(map_holder,player_character)

triggers=map_managers.MapTriggerManager(screen, player_character, map_holder.current_map, current_dialogue)


overworld_triggered_event_queue = oem.OverworldEvents()


if __name__=="__main__":
    running = True
    while running:
        event_list=pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(collision_manager.background_image.get_width() - 640, (player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(collision_manager.background_image.get_height() - 576, (player_character.rect.centery - 288)))
        screen.blit(collision_manager.background_image, (camera_x_offset, camera_y_offset))
        keys = pygame.key.get_pressed()
        player_character.draw(screen, camera_x_offset, camera_y_offset)

        if not current_dialogue:
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            player_character.move_character(can_move_bool)
            
            #replace the empty current dialogue with a new one if the map trigger manager says the player interacted with the object.
            temp_dialogue=triggers.interact_object_make_dialogue(event_list)
            if temp_dialogue:
                current_dialogue=temp_dialogue

            #if player steps on an exit trigger, change the current map and player location, then update the map managers.
            for trigger in temp_trigger_list.temp_list:
                if trigger.rect.contains(player_character.rect):
                    player_character.pixels_remaining=0
                    trigger.step_on_exit(map_holder,screen)
                    collision_manager.__init__(map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles)
                    triggers.__init__(screen,player_character,map_holder.current_map,current_dialogue)
                    temp_trigger_list.generate_temp_trigger_list(map_holder,player_character)

        elif current_dialogue:
            current_dialogue.render(event_list)
        pygame.display.flip()
        clock.tick(60)