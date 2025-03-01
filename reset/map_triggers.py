import pygame

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import map_image
import player_movement

'''
class Map():
    def __init__(self,map_bg,obstacles=None):
        self.map_bg=map_bg
        self.obstacles=obstacles

    def move(self,keys,obstacles):
        #...
                if self.can_move(obstacles, "up"):
                #...
                if self.can_move(obstacles, "down"):
                #...
                if self.can_move(obstacles, "left"):
                #...
                if self.can_move(obstacles, "right"):
'''

def can_move(obstacles, basic_map, player):
    next_rect = player.rect.copy()

    if player.up_command:
        next_rect.y -= player_movement.TILE_SIZE
    elif player.down_command:
        next_rect.y += player_movement.TILE_SIZE
    elif player.left_command:
        next_rect.x -= player_movement.TILE_SIZE
    elif player.right_command:
        next_rect.x += player_movement.TILE_SIZE

    pygame.draw.rect(screen, (255,0,0), next_rect.move(camera_x_offset, camera_y_offset))

    # Check horizontal bounds
    if next_rect.x < 0:
        return False
    if next_rect.right > basic_map.bg_image.get_width():
        return False

    # Check vertical bounds
    if next_rect.y < 0:
        return False
    if next_rect.bottom > basic_map.bg_image.get_height():
        return False

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if obstacle.contains(next_rect):
            return False

    # If all checks passed, the movement is valid
    return True

bg_image=map_image.current_map

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


if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(map_image.current_map.bg_image.get_width() - 640, (player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(map_image.current_map.bg_image.get_height() - 576, (player_character.rect.centery - 288)))
        screen.blit(map_image.current_map.bg_image, (camera_x_offset, camera_y_offset))
        keys = pygame.key.get_pressed()
        player_character.process_input(keys)
        if can_move(obstacles,bg_image,player_character):
            player_character.move_character()
        player_character.draw(screen, camera_x_offset, camera_y_offset)
        pygame.display.flip()
        clock.tick(60)