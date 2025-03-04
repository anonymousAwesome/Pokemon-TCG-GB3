import pygame
import os
import characters
import ui
import key_mappings

class CurrentMapContainer():
    def __init__(self,current_map_class,screen):
        self.current_map=current_map_class(screen)


class CollisionManager():
    def __init__(self,background_image,player,obstacles=None):
        self.background_image=background_image
        self.obstacles=obstacles
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


class MapTriggerManager():
    def __init__(self,screen,player,current_map,current_dialogue):
        self.screen=screen
        self.player=player
        self.current_dialogue=current_dialogue

        self.interact_object=getattr(current_map,"interact_object",False)

        self.step_exit_triggers=getattr(current_map,"step_exit_triggers",False)
       
    def manager_interact_self(self):
        pass
    
    def manager_interact_object(self,event_list,map_input_lock,passed_definition,definition_type):
        if self.interact_object:
            temp_interact_front_rect=self.player.rect.copy()
            if self.player.facing_direction=="down":
                temp_interact_front_rect.y+=characters.TILE_SIZE
            if self.player.facing_direction=="up":
                temp_interact_front_rect.y-=characters.TILE_SIZE
            if self.player.facing_direction=="left":
                temp_interact_front_rect.x-=characters.TILE_SIZE
            if self.player.facing_direction=="right":
                temp_interact_front_rect.x+=characters.TILE_SIZE
            for event in event_list:
                if event.type==pygame.KEYDOWN:
                    if event.key==key_mappings.affirm_key:
                        for map_object in self.interact_object:
                            temp_map_object=map_object(self.screen,passed_definition,definition_type)
                            if temp_map_object.rect.contains(temp_interact_front_rect):
                                temp_map_object.interact_object(map_input_lock)