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

def check_interact_with_object(map_holder,player_character,event_list,screen,passed_definition,map_input_lock,event_manager,current_dialogue):
    interact_object=getattr(map_holder.current_map,"interact_object",False)
    if interact_object:
        temp_interact_front_rect=player_character.rect.copy()
        if player_character.facing_direction=="down":
            temp_interact_front_rect.y+=characters.TILE_SIZE
        if player_character.facing_direction=="up":
            temp_interact_front_rect.y-=characters.TILE_SIZE
        if player_character.facing_direction=="left":
            temp_interact_front_rect.x-=characters.TILE_SIZE
        if player_character.facing_direction=="right":
            temp_interact_front_rect.x+=characters.TILE_SIZE
        for event in event_list.events:
            if event.type==pygame.KEYDOWN:
                if event.key==key_mappings.affirm_key:
                    for map_object in interact_object:
                        temp_map_object=map_object(screen,passed_definition)
                        if temp_map_object.rect.contains(temp_interact_front_rect):
                            event_manager.add_event(temp_map_object.interact_object)
                            event_manager.add_event(current_dialogue.render,[event_list,map_input_lock],persistent_condition=current_dialogue.check_remaining_text)
                            map_input_lock.lock()