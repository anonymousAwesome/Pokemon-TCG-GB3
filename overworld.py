import pygame
import characters
import os

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import map_managers
import mapinfo


spritesheet_path = os.path.join("assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

sprites = characters.load_sprites_from_sheet(spritesheet, 6)


player_character=characters.Player(448,832, sprites)

current_map=mapinfo.MasonCenter(screen,"mason center")


collision_manager=map_managers.CollisionManager(current_map.bg_image,player_character,current_map.obstacles)

triggers=map_managers.MapTriggerManager(screen,player_character,interact_object_triggers=current_map.interact_object_dialogue)

current_dialogue=None

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
        if not current_dialogue:
            player_character.process_input(keys)
            can_move_bool=collision_manager.can_move()
            player_character.move_character(can_move_bool)
            current_dialogue=triggers.interact_object_dialogue(event_list)
        elif current_dialogue:
            current_dialogue.render(event_list)
        pygame.display.flip()
        clock.tick(60)