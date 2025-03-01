import pygame
import os

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import map_image
import player_movement

def get_bg_image(map_name):
    bg_image=pygame.image.load(os.path.join("..","assets", "maps", map_name+".png"))
    bg_image=pygame.transform.scale(bg_image, (bg_image.get_width() * 4, bg_image.get_height() * 4))
    return bg_image

class Map():
    def __init__(self,map_name,player,obstacles=None):
        self.background_image=get_bg_image(map_name)
        self.obstacles=obstacles
        self.player=player

    def can_move(self):
        next_rect = self.player.rect.copy()

        if self.player.up_command:
            next_rect.y -= player_movement.TILE_SIZE
        elif self.player.down_command:
            next_rect.y += player_movement.TILE_SIZE
        elif self.player.left_command:
            next_rect.x -= player_movement.TILE_SIZE
        elif self.player.right_command:
            next_rect.x += player_movement.TILE_SIZE

        pygame.draw.rect(screen, (255,0,0), next_rect.move(camera_x_offset, camera_y_offset))

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


obstacles=[
    pygame.Rect(0, 0, 896, 64),
    pygame.Rect(0, 448, 64, 512),
    pygame.Rect(832, 448, 64, 512),
    pygame.Rect(64, 832, 384, 64),
    pygame.Rect(64, 896, 384, 64),
    pygame.Rect(0, 64, 320, 64),
    pygame.Rect(576, 64, 320, 64),
    pygame.Rect(576, 832, 256, 64),
    pygame.Rect(576, 896, 256, 64),
    pygame.Rect(640, 448, 192, 64),
    pygame.Rect(0, 128, 64, 192),
    pygame.Rect(832, 128, 64, 192),
    pygame.Rect(192, 448, 128, 64),
    pygame.Rect(192, 512, 128, 64),
    pygame.Rect(64, 704, 64, 128),
    ]

player_character=player_movement.Player(448,832, player_movement.player_sprite_camera.sprites)

current_map=Map("mason center",player_character,obstacles)

if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(current_map.background_image.get_width() - 640, (current_map.player.rect.centerx - 320)))
        camera_y_offset = -max(0, min(current_map.background_image.get_height() - 576, (current_map.player.rect.centery - 288)))
        screen.blit(current_map.background_image, (camera_x_offset, camera_y_offset))
        keys = pygame.key.get_pressed()
        current_map.player.process_input(keys)
        can_move_bool=current_map.can_move()
        current_map.player.move_character(can_move_bool)
        current_map.player.draw(screen, camera_x_offset, camera_y_offset)
        pygame.display.flip()
        clock.tick(60)