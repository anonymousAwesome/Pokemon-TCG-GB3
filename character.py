import pygame
pygame.init()
screen = pygame.display.set_mode((640,576))


TILE_SIZE=64
anim_speed=32

'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

def load_sprites_from_sheet(spritesheet, row):
    sprites = []
    for i in range(10):
        x = i*17 + 1
        y = row*17 + 1
        sprite=spritesheet.subsurface(pygame.Rect(x, y, 16, 16))
        sprite=pygame.transform.scale(sprite, (16*4, 16*4))
        sprites.append(sprite)
    return sprites

spritesheet_path = '/media/brendanj/Shared Partition/programming/pokemon tcg monte carlo/pokemon_tcg_fangame/assets/duellists/Pokemon TCG2 sprites.png'
spritesheet = pygame.image.load(spritesheet_path).convert_alpha()

sprites = load_sprites_from_sheet(spritesheet, 1)

class Player(pygame.sprite.Sprite):

    def __init__( self, x, y, anim_frames, bg_image):
        self.bg_image=bg_image #remember to update this whenever the map changes
        pygame.sprite.Sprite.__init__(self)

        self.walking_down_1=anim_frames[0]
        self.facing_down=anim_frames[1]
        self.walking_down_2=anim_frames[2]
        self.walking_up_1=anim_frames[3]
        self.facing_up=anim_frames[4]
        self.walking_up_2=anim_frames[5]
        self.facing_left=anim_frames[6]
        self.walking_left=anim_frames[7]
        self.facing_right=anim_frames[8]
        self.walking_right=anim_frames[9]

        self.image = self.facing_down
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        self.move  = 4 #Just to be safe, keep it a factor of 64: 1, 2, 4, 8, 16, 32, or 64.
        self.pixels_remaining=0
        self.facing_direction="down"
        
        self.walking_side=True

    def flip_walking_side(self):
        self.walking_side=not self.walking_side

    def update(self,keys,obstacles):
        move_speed=self.move
        if keys[pygame.K_LALT] or keys[pygame.K_RALT]:
            move_speed=self.move*2
        if self.pixels_remaining<0:
            self.pixels_remaining=0
        if self.pixels_remaining==0:
            if keys[pygame.K_UP]:
                self.flip_walking_side()
                self.facing_direction="up"
                self.image=self.facing_up
                if self.can_move(obstacles, "up",self.bg_image):
                    self.pixels_remaining=TILE_SIZE
                    self.rect.y-=move_speed
                    self.pixels_remaining-=move_speed
                    if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                        self.image=self.facing_up
                    else:
                        if self.walking_side:
                            self.image=self.walking_up_1
                        else:
                            self.image=self.walking_up_2
            elif keys[pygame.K_DOWN]:
                self.flip_walking_side()
                self.facing_direction="down"
                self.image=self.facing_down
                if self.can_move(obstacles, "down",self.bg_image):
                    self.pixels_remaining=TILE_SIZE
                    self.rect.y+=move_speed
                    self.pixels_remaining-=move_speed
                    if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                        self.image=self.facing_down
                    else:
                        if self.walking_side:
                            self.image=self.walking_down_1
                        else:
                            self.image=self.walking_down_2
            elif keys[pygame.K_LEFT]:
                self.facing_direction="left"
                self.image=self.facing_left
                if self.can_move(obstacles, "left",self.bg_image):
                    self.pixels_remaining=TILE_SIZE
                    self.rect.x-=move_speed
                    self.pixels_remaining-=move_speed
                    if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                        self.image=self.facing_left
                    else:
                        self.image=self.walking_left
            elif keys[pygame.K_RIGHT]:
                self.facing_direction="right"
                self.image=self.facing_right
                if self.can_move(obstacles, "right",self.bg_image):
                    self.pixels_remaining=TILE_SIZE
                    self.rect.x+=move_speed
                    self.pixels_remaining-=move_speed
                    if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                        self.image=self.facing_right
                    else:
                        self.image=self.walking_right

            self.rect.x=TILE_SIZE*round(self.rect.x/TILE_SIZE)
            self.rect.y=TILE_SIZE*round(self.rect.y/TILE_SIZE)
        elif self.pixels_remaining>0:
            if self.facing_direction=="up":
                self.rect.y-=move_speed
                if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                    self.image=self.facing_up
                else:
                    if self.walking_side:
                        self.image=self.walking_up_1
                    else:
                        self.image=self.walking_up_2

            if self.facing_direction=="down":
                self.rect.y+=move_speed
                if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                    self.image=self.facing_down
                else:
                    if self.walking_side:
                        self.image=self.walking_down_1
                    else:
                        self.image=self.walking_down_2
            if self.facing_direction=="left":
                self.rect.x-=move_speed
                if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                    self.image=self.facing_left
                else:
                    self.image=self.walking_left
            if self.facing_direction=="right":
                self.rect.x+=move_speed
                if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                    self.image=self.facing_right
                else:
                    self.image=self.walking_right

            self.pixels_remaining-=move_speed
    
        if self.pixels_remaining==0:
            if self.facing_direction=="up":
                if not keys[pygame.K_UP]:
                    self.image=self.facing_up
            if self.facing_direction=="down":
                if not keys[pygame.K_DOWN]:
                    self.image=self.facing_down
            if self.facing_direction=="left":
                if not keys[pygame.K_LEFT]:
                    self.image=self.facing_left
            if self.facing_direction=="right":
                if not keys[pygame.K_RIGHT]:
                    self.image=self.facing_right
            
    
    def draw(self, surface, camera_x_offset, camera_y_offset):
        surface.blit(self.image, (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))

    def can_move(self, obstacles, direction,bg_image):
        next_rect = self.rect.copy()
        if direction == "up":
            next_rect.y -= TILE_SIZE
        elif direction == "down":
            next_rect.y += TILE_SIZE
        elif direction == "left":
            next_rect.x -= TILE_SIZE
        elif direction == "right":
            next_rect.x += TILE_SIZE

        # Check horizontal bounds
        if next_rect.x < 0:
            return False
        if next_rect.right > bg_image.get_width():
            return False

        # Check vertical bounds
        if next_rect.y < 0:
            return False
        if next_rect.bottom > bg_image.get_height():
            return False

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if next_rect.colliderect(obstacle):
                return False

        # If all checks passed, the movement is valid
        return True
