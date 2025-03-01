import pygame
import os
import moving_characters

def get_bg_image(map_name):
    bg_image=pygame.image.load(os.path.join("..","assets", "maps", map_name+".png"))
    bg_image=pygame.transform.scale(bg_image, (bg_image.get_width() * 4, bg_image.get_height() * 4))
    return bg_image

class CollisionManager():
    def __init__(self,map_name,player,obstacles=None):
        self.background_image=get_bg_image(map_name)
        self.obstacles=obstacles
        self.player=player

    def can_move(self):
        next_rect = self.player.rect.copy()

        if self.player.up_command:
            next_rect.y -= moving_characters.TILE_SIZE
        elif self.player.down_command:
            next_rect.y += moving_characters.TILE_SIZE
        elif self.player.left_command:
            next_rect.x -= moving_characters.TILE_SIZE
        elif self.player.right_command:
            next_rect.x += moving_characters.TILE_SIZE

        #pygame.draw.rect(screen, (255,0,0), next_rect.move(camera_x_offset, camera_y_offset))

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

