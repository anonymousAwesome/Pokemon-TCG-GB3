import pygame
import os
import characters
import ui
import key_mappings

class CurrentMapContainer():
    def __init__(self,current_map_class):
        self.current_map=current_map_class()

class CollisionManager():
    def __init__(self,background_image,player,screen,current_dialogue,event_manager,map_input_lock,obstacles=[],npcs=[]):
        self.background_image=background_image
        self.obstacles=obstacles
        for npc in npcs:
            self.obstacles.append(npc(screen,current_dialogue,event_manager,map_input_lock,player).sprite.rect)
        
        self.player=player

    def can_move(self):
        next_rect = self.player.rect.copy()

        if self.player.up_command:
            next_rect.y -= characters.TILE_SIZE
        elif self.player.down_command:
            next_rect.y += characters.TILE_SIZE
        elif self.player.left_command:
            next_rect.x -= characters.TILE_SIZE
        elif self.player.right_command:
            next_rect.x += characters.TILE_SIZE

        if next_rect.x < 0:
            return False
        if next_rect.right > self.background_image.get_width():
            return False

        if next_rect.y < 0:
            return False
        if next_rect.bottom > self.background_image.get_height():
            return False

        for obstacle in self.obstacles:
            if obstacle.contains(next_rect):
                return False

        return True

def check_all_interactions(map_holder,player_character,event_list,screen,map_input_lock,current_dialogue,temp_exit_list,overworld_event_manager,collision_manager,current_npcs):
    check_interact_with_object(map_holder,player_character,event_list,screen,map_input_lock,overworld_event_manager,current_dialogue)
    check_step_on_object(temp_exit_list,player_character,overworld_event_manager,map_holder,screen,collision_manager,current_npcs,current_dialogue,map_input_lock)
    check_interact_with_self(map_holder,player_character,event_list,screen,map_input_lock,overworld_event_manager,current_dialogue,collision_manager,temp_exit_list,current_npcs)
    
def check_interact_with_object(map_holder,player_character,event_list,screen,map_input_lock,overworld_event_manager,current_dialogue):
    interact_object=getattr(map_holder.current_map,"interact_object_triggers",False)
    npc_list=getattr(map_holder.current_map,"npcs",False)
    if not map_input_lock:
        if interact_object or npc_list:
            temp_interact_front_rect=player_character.rect.copy()
            if player_character.facing_direction=="down":
                temp_interact_front_rect.y+=characters.TILE_SIZE
            if player_character.facing_direction=="up":
                temp_interact_front_rect.y-=characters.TILE_SIZE
            if player_character.facing_direction=="left":
                temp_interact_front_rect.x-=characters.TILE_SIZE
            if player_character.facing_direction=="right":
                temp_interact_front_rect.x+=characters.TILE_SIZE
            for event in event_list:
                if event.type==pygame.KEYDOWN:
                    if event.key==key_mappings.affirm_key:
                        for map_object in interact_object:
                            temp_map_object=map_object(screen,current_dialogue,overworld_event_manager,map_input_lock,player_character)
                            if temp_map_object.rect.contains(temp_interact_front_rect):
                                temp_map_object.interact_object(event_list)
                        for npc in npc_list:
                            temp_npc=npc(screen,current_dialogue,overworld_event_manager,map_input_lock,player_character)
                            if temp_npc.sprite.rect.contains(temp_interact_front_rect):
                                temp_npc.interact_object(event_list)

def check_step_on_object(temp_exit_list,player_character,overworld_event_manager,map_holder,screen,collision_manager,current_npcs,current_dialogue,map_input_lock):
    for trigger in temp_exit_list.temp_list:
        if trigger.rect.contains(player_character.rect):
            overworld_event_manager.add_event(trigger.step_on,[map_holder,screen,overworld_event_manager,collision_manager,player_character,temp_exit_list,current_npcs,current_dialogue,map_input_lock])

def check_interact_with_self(map_holder,player_character,event_list,screen,map_input_lock,overworld_event_manager,current_dialogue,collision_manager,temp_exit_list,current_npcs):
    interact_object=getattr(map_holder.current_map,"interact_self_triggers",False)
    if not map_input_lock:
        if interact_object:
            for event in event_list:
                if event.type==pygame.KEYDOWN:
                    if event.key==key_mappings.affirm_key:
                        for map_object in interact_object:
                            temp_map_object=map_object()
                            if temp_map_object.rect.contains(player_character.rect):
                                temp_map_object.interact_self(map_holder, screen,overworld_event_manager,collision_manager,player_character,temp_exit_list,current_npcs,current_dialogue,map_input_lock)