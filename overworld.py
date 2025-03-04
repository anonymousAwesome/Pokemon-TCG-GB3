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
    def __init__(self,temp_list=[]):
        self.temp_list=temp_list

    def generate_temp_exit_list(self,map_holder,player_character):
        temp_list=[]
        for trigger in map_holder.current_map.step_exit_triggers:
            temp_list.append(trigger(player_character))
        self.temp_list=temp_list


temp_exit_list=TempExitList()

temp_exit_list.generate_temp_exit_list(map_holder,player_character)

overworld_event_manager = oem.OverworldEventManager()


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

        if not map_input_lock:
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            player_character.move_character(can_move_bool)
            
            #replace the empty current dialogue with a new one if the map trigger manager says the player interacted with the object.
            map_managers.process_step_on_trigger(map_holder,player_character,event_list,screen,current_dialogue,"class object",map_input_lock)

            #if player steps on an exit trigger, change the current map 
            #and player location, re-init the map managers, and re-generate the temp exit list.
            for trigger in temp_exit_list.temp_list:
                if trigger.rect.contains(player_character.rect):
                    player_character.pixels_remaining=0
                    trigger.step_on_exit(map_holder,screen)
                    collision_manager.__init__(map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles)
                    temp_exit_list.generate_temp_exit_list(map_holder,player_character)

        elif map_input_lock:
            current_dialogue.render(event_list,map_input_lock)
        pygame.display.flip()
        clock.tick(60)