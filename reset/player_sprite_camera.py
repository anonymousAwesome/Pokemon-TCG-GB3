import pygame
import map_image
import os



if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((640,576))
    clock = pygame.time.Clock()


def load_sprites_from_sheet(spritesheet, row):
    sprites = []
    for i in range(10):
        x = i*17 + 1
        y = row*17 + 1
        sprite=spritesheet.subsurface(pygame.Rect(x, y, 16, 16))
        sprite=pygame.transform.scale(sprite, (16*4, 16*4))
        sprites.append(sprite)
    return sprites

spritesheet_path = os.path.join("..","assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

sprites = load_sprites_from_sheet(spritesheet, 6)


class StaticCharacter(pygame.sprite.Sprite):

    def __init__(self, x, y, anim_frames):
        pygame.sprite.Sprite.__init__(self)
        self.anim_frames=anim_frames
        self.image = anim_frames[1]
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        
    def draw(self, surface, camera_x_offset, camera_y_offset):
        surface.blit(self.image, (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))

player_character=StaticCharacter(448,832, sprites)

if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        camera_x_offset = -max(0, min(map_image.current_map.bg_image.get_width() - 640, (player_character.rect.centerx - 320)))
        camera_y_offset = -max(0, min(map_image.current_map.bg_image.get_height() - 576, (player_character.rect.centery - 288)))
        screen.blit(map_image.current_map.bg_image, (camera_x_offset, camera_y_offset))
        player_character.draw(screen, camera_x_offset, camera_y_offset)
        pygame.display.flip()
        clock.tick(60)