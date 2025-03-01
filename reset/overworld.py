import pygame
import moving_characters
import os

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import map_triggers


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


spritesheet_path = os.path.join("..","assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

sprites = moving_characters.load_sprites_from_sheet(spritesheet, 6)


player_character=moving_characters.Player(448,832, sprites)

collision_manager=map_triggers.CollisionManager("mason center",player_character,obstacles)



if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(collision_manager.background_image.get_width() - 640, (player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(collision_manager.background_image.get_height() - 576, (player_character.rect.centery - 288)))
        screen.blit(collision_manager.background_image, (camera_x_offset, camera_y_offset))
        keys = pygame.key.get_pressed()
        player_character.process_input(keys)
        can_move_bool=collision_manager.can_move()
        player_character.move_character(can_move_bool)
        player_character.draw(screen, camera_x_offset, camera_y_offset)
        pygame.display.flip()
        clock.tick(60)