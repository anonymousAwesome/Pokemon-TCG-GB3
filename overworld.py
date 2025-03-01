import pygame
import characters
import os
import map_triggers


if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import mapinfo
import ui


spritesheet_path = os.path.join("assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

sprites = characters.load_sprites_from_sheet(spritesheet, 6)


player_character=characters.Player(448,832, sprites)

current_map_name="mason center"

current_map_bg=map_triggers.get_bg_image(current_map_name)

loaded_map_info=getattr(mapinfo,"mason_center")

obstacles=loaded_map_info["obstacles"]
obstacles=[]

collision_manager=map_triggers.CollisionManager(current_map_bg,player_character,obstacles)

triggers=map_triggers.MapTriggerManager(player_character,step_triggers=loaded_map_info["interact_object_text"])

current_dialogue=None

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
        if not current_dialogue:
            player_character.process_input(keys)
            triggers.step_trigger()
            can_move_bool=collision_manager.can_move()
            player_character.move_character(can_move_bool)
        player_character.draw(screen, camera_x_offset, camera_y_offset)
        if current_dialogue:
            current_dialogue.render(keys)
        pygame.display.flip()
        clock.tick(60)