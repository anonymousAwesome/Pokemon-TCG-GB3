'''Note: I use several singleton classes because I replace objects in-
place a lot, and if I don't wrap each of them in a class and use class
functions to do that, Python won't play nice.'''

import pygame
import os
import functools
import overworld_event_managers as oem

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import characters
import ui
import map_managers
import mapinfo

#starting_map_class=mapinfo.MasonCenter
starting_map_class=mapinfo.TradingPost

pc_sprite = characters.load_sprites_from_sheet(characters.spritesheet_tcg2,0)

#player_character=characters.Player(448,832, pc_sprite)
player_character=characters.Player(320,320, pc_sprite)

map_holder=map_managers.CurrentMapContainer(starting_map_class)

current_dialogue=ui.Dialogue(screen,"")

collision_manager=map_managers.CollisionManager(map_holder.current_map.bg_image, player_character, map_holder.current_map.obstacles)

class TempExitList():
    '''called when the player moves into a new map, so I'm not 
    instantiating the trigger class 60 times a second.'''
    def __init__(self,map_holder,player_character):
        temp_list=[]
        triggers=getattr(map_holder.current_map,"step_triggers",[])
        
        for trigger in triggers:
            temp_list.append(trigger())
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


class CurrentNPCs:
    def __init__(self,current_map_class):
        self.spritesheet_yellow=characters.spritesheet_yellow
        self.spritesheet_crystal=characters.spritesheet_crystal
        self.spritesheet_tcg2=characters.spritesheet_tcg2

        self.reset(current_map_class)

    def reset(self,current_map_class):
        self.current_npcs=[]
        for npc in getattr(current_map_class(),"npcs",[]):
            self.current_npcs.append(npc())
        
current_npcs=CurrentNPCs(starting_map_class)

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

        for npc in current_npcs.current_npcs:
            npc.sprite.draw(screen,camera_x_offset, camera_y_offset)
        
        keys = pygame.key.get_pressed()
        player_character.draw(screen, camera_x_offset, camera_y_offset)

        if not map_input_lock:
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            player_character.move_character(can_move_bool)


        map_managers.check_all_interactions(map_holder,player_character,event_list,screen,map_input_lock,current_dialogue,temp_exit_list,overworld_event_manager,collision_manager,current_npcs)

        overworld_event_manager.run_next_event()
        pygame.display.flip()
        clock.tick(60)