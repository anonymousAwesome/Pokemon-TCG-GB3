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
        if npcs:
            for npc in npcs.current_npcs:
                self.obstacles.append(npc.sprite.rect)
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


def check_all_interactions(inner_context,phase_handler):
    check_interact_with_object(inner_context,phase_handler)
    check_step_on_object(inner_context)
    check_interact_with_self(inner_context)
    
def check_interact_with_object(inner_context,phase_handler):
    interact_object=getattr(inner_context.map_holder.current_map,"interact_object_triggers",False)
    if not inner_context.map_input_lock:
        if interact_object or inner_context.current_npcs.current_npcs:
            temp_interact_front_rect=inner_context.player_character.rect.copy()
            if inner_context.player_character.facing_direction=="down":
                temp_interact_front_rect.y+=characters.TILE_SIZE
            if inner_context.player_character.facing_direction=="up":
                temp_interact_front_rect.y-=characters.TILE_SIZE
            if inner_context.player_character.facing_direction=="left":
                temp_interact_front_rect.x-=characters.TILE_SIZE
            if inner_context.player_character.facing_direction=="right":
                temp_interact_front_rect.x+=characters.TILE_SIZE
            for event in inner_context.event_list:
                if event.type==pygame.KEYDOWN:
                    if event.key==key_mappings.affirm_key:
                        for map_object in interact_object:
                            temp_map_object=map_object()
                            if temp_map_object.rect.contains(temp_interact_front_rect):
                                temp_map_object.interact_object(inner_context,phase_handler)
                        for npc in inner_context.current_npcs.current_npcs:
                            if npc.sprite.rect.contains(temp_interact_front_rect):
                                npc.interact_object(inner_context,phase_handler)

def check_step_on_object(inner_context):
    for trigger in inner_context.temp_exit_list.temp_list:
        if trigger.rect.contains(inner_context.player_character.rect):
            inner_context.event_manager.add_event(trigger.step_on,[inner_context])

def check_interact_with_self(inner_context):
    interact_object=getattr(inner_context.map_holder.current_map,"interact_self_triggers",False)
    if not inner_context.map_input_lock:
        if interact_object:
            for event in inner_context.event_list:
                if event.type==pygame.KEYDOWN:
                    if event.key==key_mappings.affirm_key:
                        for map_object in interact_object:
                            temp_map_object=map_object()
                            if temp_map_object.rect.contains(inner_context.player_character.rect):
                                temp_map_object.interact_self(inner_context)