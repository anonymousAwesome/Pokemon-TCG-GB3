import pygame
import os
import characters
import ui
import key_mappings


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
    def __init__(self,screen,player,interact_object_triggers=None,interact_self_triggers=None,step_triggers=None):
        self.screen=screen
        self.player=player
        self.interact_object_triggers=interact_object_triggers
        self.interact_self_triggers=interact_self_triggers
        self.step_triggers=step_triggers

    def interact_object(self):
        pass
        
    def interact_self(self):
        pass
    
    def interact_object_dialogue(self,event_list):
        if self.interact_object_triggers:
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
                        for pair in self.interact_object_triggers:
                            if pair[0].contains(temp_interact_front_rect):
                                return(ui.Dialogue(self.screen,pair[1]))
            return None

    '''
    def step_trigger(self):
        if self.step_triggers:
            for pair in self.step_triggers:
                if pair[0].contains(self.player.rect):
                    getattr(pair[1]["location"],pair[1]["function"])(*pair[1]["args"],**pair[1]["kwargs"])
                    '''