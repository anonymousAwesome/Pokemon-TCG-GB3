'''Note: I use several singleton classes because I replace objects in-
place a lot, and if I don't wrap each of them in a class and use class
functions to do that, Python won't play nice.'''

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

class TempExitList():
    '''called when the player moves into a new map, so I'm not 
    instantiating the trigger class 60 times a second.'''
    def __init__(self,map_holder,player_character):
        temp_list=[]
        triggers=getattr(map_holder.current_map,"step_triggers",[])
        
        for trigger in triggers:
            temp_list.append(trigger(player_character))
        self.temp_list=temp_list


temp_exit_list=TempExitList(map_holder,player_character)

class MovementLock():
    def __init__(self,locked=False):
        self.locked=locked
    
    def __bool__(self):
        if self.locked:
            return True
        else:
            return False
    
    def lock(self):
        self.locked=True
        
    def unlock(self):
        self.locked=False

map_input_lock=MovementLock()


overworld_event_manager = oem.OverworldEventManager(map_input_lock)

event_list=[]

if __name__=="__main__":
    running = True
    while running:
        event_list[:]=pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(collision_manager.background_image.get_width() - 640, (player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(collision_manager.background_image.get_height() - 576, (player_character.rect.centery - 288)))
        screen.blit(collision_manager.background_image, (camera_x_offset, camera_y_offset))
        keys = pygame.key.get_pressed()
        player_character.draw(screen, camera_x_offset, camera_y_offset)

        if not map_input_lock:
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            player_character.move_character(can_move_bool)


            map_managers.check_all_interactions(map_holder,player_character,event_list,screen,map_input_lock,current_dialogue,temp_exit_list,overworld_event_manager,collision_manager)

        elif map_input_lock:
            overworld_event_manager.run_all_events()
        pygame.display.flip()
        clock.tick(60)