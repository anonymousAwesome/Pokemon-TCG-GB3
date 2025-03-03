import pygame
import characters
import os
import functools

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()

import ui
import map_managers
import mapinfo


spritesheet_yellow_path = os.path.join("assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet_crystal_path = os.path.join("assets","npc sprites","pokemon crystal sprites recolored.png")
spritesheet_tcg2_path = os.path.join("assets","npc sprites","pokemon tcg2 sprites.png")

spritesheet_yellow=pygame.image.load(spritesheet_yellow_path).convert_alpha()
spritesheet_crystal=pygame.image.load(spritesheet_crystal_path).convert_alpha()
spritesheet_tcg2=pygame.image.load(spritesheet_tcg2_path).convert_alpha()

pc_sprite = characters.load_sprites_from_sheet(spritesheet_tcg2,0)

player_character=characters.Player(448,832, pc_sprite)

map_holder=map_managers.CurrentMapContainer(mapinfo.MasonCenter,screen)

current_dialogue=ui.Dialogue(screen,"")

collision_manager=map_managers.CollisionManager(map_holder.current_map.bg_image, player_character, map_holder.current_map.obstacles)

triggers=map_managers.MapTriggerManager(screen, player_character, map_holder.current_map, current_dialogue)

triggered_functions=[print]


'''
main objects: player character, current dialogue, and current map. 
main loop should take these objects, feed them into the map manager(s),
check the appropriate triggers, put one or more functions into the list,
and trigger at least one function each loop, as appropriate.
'''


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
            
            #takes keyboad input, converts it to commands which are stored in the player_character object
            player_character.process_input(keys) 
            
            #checks to see if the current movement command would be blocked by an obstacle
            can_move_bool=collision_manager.can_move()
            
            #if not blocked, start movement. If blocked, change facing.
            player_character.move_character(can_move_bool)
            
            #replace the empty current dialogue with a new one if the map trigger manager says the player interacted with the object.
            temp_dialogue=triggers.interact_object_make_dialogue(event_list)
            if temp_dialogue:
                current_dialogue=temp_dialogue

            #if player steps on an exit trigger, change the current map and player location, then update the map managers.
            for trigger in map_holder.current_map.step_exit_triggers:
                if trigger(player_character).rect.contains(player_character.rect):
                    player_character.pixels_remaining=0
                    trigger(player_character).step_on_exit(map_holder,screen)
                    player_character.map_exit_change_facing()
                    collision_manager.__init__(map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles)
                    triggers.__init__(screen,player_character,map_holder.current_map,current_dialogue)

        elif current_dialogue:
            current_dialogue.render(event_list)
        pygame.display.flip()
        clock.tick(60)