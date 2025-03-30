'''Note: I use several singleton classes because I replace variables in-
place a lot, and if I try to manually change it, Python sometimes breaks
the connection to the replaced object.

Instead, I wrap the variable in a class and call class functions to replace
the variable without breaking the connections to the wrapper object.'''

import pygame
import os
import overworld_event_managers as oem
import characters
import ui
import map_managers
import mapinfo
import player

import pygame
import numpy as np

class TempExitList():
    '''called when the player moves into a new map, so I'm not 
    instantiating the trigger class 60 times a second.'''
    def __init__(self,map_holder,player_character):
        temp_list=[]
        triggers=getattr(map_holder.current_map,"step_triggers",[])
        
        for trigger in triggers:
            temp_list.append(trigger())
        self.temp_list=temp_list

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

class CurrentNPCs:
    def __init__(self,screen,current_map_class,current_dialogue,overworld_event_manager,map_input_lock,player_character,player_data):
        self.current_dialogue=current_dialogue
        self.overworld_event_manager=overworld_event_manager
        self.map_input_lock=map_input_lock
        self.player_character=player_character
        self.spritesheet_yellow=characters.spritesheet_yellow
        self.spritesheet_crystal=characters.spritesheet_crystal
        self.spritesheet_tcg2=characters.spritesheet_tcg2
        self.screen=screen
        self.player_data=player_data
        self.reset(current_map_class)

    def reset(self,current_map_class):
        self.current_npcs=[]
        for npc in getattr(current_map_class(),"npcs",[]):
            if npc not in self.player_data.removed_npcs:
                self.current_npcs.append(npc())

class InnerContext:
    def __init__(self,map_holder,player_character,event_list,screen,map_input_lock,current_dialogue,temp_exit_list,event_manager,collision_manager,current_npcs,phase_handler,player_data):
        self.map_holder=map_holder
        self.player_character=player_character
        self.event_list=event_list
        self.screen=screen
        self.map_input_lock=map_input_lock
        self.current_dialogue=current_dialogue
        self.temp_exit_list=temp_exit_list
        self.event_manager=event_manager
        self.collision_manager=collision_manager
        self.current_npcs=current_npcs
        self.phase_handler=phase_handler
        self.player_data=player_data
        
        self.just_stepped_on_exit=False
        
    def reset_exit_flag(self):
        self.just_stepped_on_exit = False

    def perceptual_greyscale(self,surface):
        """Convert a surface to greyscale efficiently using numpy and preserve transparency."""
        arr = pygame.surfarray.pixels3d(surface)
        alpha = pygame.surfarray.pixels_alpha(surface)

        grey = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
        grey_arr = np.stack((grey, grey, grey), axis=-1)

        grey_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        pygame.surfarray.blit_array(grey_surface, grey_arr)
        pygame.surfarray.pixels_alpha(grey_surface)[:] = alpha

        return grey_surface


class Context:
    def __init__(self,screen,phase_handler):

        self.screen=screen
        self.starting_map_class=mapinfo.MasonCenter
        #self.starting_map_class=mapinfo.TradingPost

        self.pc_sprite = characters.load_sprites_from_sheet(characters.spritesheet_tcg2,0)

        self.player_character=characters.Player(448,832, self.pc_sprite,"up")
        #self.player_character=characters.Player(320,320, self.pc_sprite,"up")

        self.map_holder=map_managers.CurrentMapContainer(self.starting_map_class)

        self.current_dialogue=ui.Dialogue(self.screen,"")

        self.temp_exit_list=TempExitList(self.map_holder,self.player_character)
         
        self.map_input_lock=MovementLock()

        self.overworld_event_manager = oem.OverworldEventManager(self.map_input_lock)

        self.event_list=[]

        self.player_data=player.PlayerData()
                
        self.current_npcs=CurrentNPCs(self.screen,self.starting_map_class,self.current_dialogue,self.overworld_event_manager,self.map_input_lock,self.player_character,self.player_data)

        self.collision_manager=map_managers.CollisionManager(self.map_holder.current_map.bg_image, self.player_character,self.screen,self.current_dialogue,self.overworld_event_manager,self.map_input_lock,obstacles=self.map_holder.current_map.obstacles,npcs=self.current_npcs)

        self.inner_context=InnerContext(self.map_holder,self.player_character,self.event_list,self.screen,self.map_input_lock,self.current_dialogue,self.temp_exit_list,self.overworld_event_manager,self.collision_manager,self.current_npcs,phase_handler,self.player_data)

        if self.player_data.currently_greyscale:
            self.map_holder.current_map.bg_image.blit(self.inner_context.perceptual_greyscale(self.map_holder.current_map.bg_image),(0,0))


    def update(self,event_list):
        self.event_list[:]=event_list
        for event in self.event_list:
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(self.collision_manager.background_image.get_width() - 640, (self.player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(self.collision_manager.background_image.get_height() - 576, (self.player_character.rect.centery - 288)))
        self.screen.blit(self.collision_manager.background_image, (camera_x_offset, camera_y_offset))

        for npc in self.current_npcs.current_npcs:
            if not npc.sprite.pixels_remaining:
                npc.sprite.walk_in_place()
            npc.sprite.draw(self.screen,camera_x_offset, camera_y_offset,self.inner_context)
        
        keys = pygame.key.get_pressed()
        
        self.player_character.draw(self.screen, camera_x_offset, camera_y_offset,self.inner_context)


        if not self.map_input_lock:
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            self.player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=self.collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            self.player_character.move_character(can_move_bool)


        map_managers.check_all_interactions(self.inner_context)

        self.overworld_event_manager.run_next_event()
