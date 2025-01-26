import pygame

TILE_SIZE=64

'''
Contains player name, player decks, player medals, and event flags triggered. Maybe save/load functionality.
'''

class Player( pygame.sprite.Sprite ):

    def __init__( self, x, y, player_image,bg_image):
        self.bg_image=bg_image
        pygame.sprite.Sprite.__init__( self )
        self.image = player_image
        self.image=pygame.transform.scale_by(self.image,4)
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        self.move  = 4 #Just to be safe, keep it a factor of 64: 1, 2, 4, 8, 16, 32, or 64.
        self.pixels_remaining=0
        self.moving_direction=None

    def update(self,keys,obstacles):
        move_speed=self.move
        if keys[pygame.K_LALT] or keys[pygame.K_RALT]:
            move_speed=self.move*2
        if self.pixels_remaining<=0:
            if keys[pygame.K_UP] and self.can_move(obstacles, "up",self.bg_image):
                self.pixels_remaining=TILE_SIZE
                self.rect.y-=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="up"
            if keys[pygame.K_DOWN]and self.can_move(obstacles, "down",self.bg_image):
                self.pixels_remaining=TILE_SIZE
                self.rect.y+=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="down"
            if keys[pygame.K_LEFT]and self.can_move(obstacles, "left",self.bg_image):
                self.pixels_remaining=TILE_SIZE
                self.rect.x-=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="left"
            if keys[pygame.K_RIGHT]and self.can_move(obstacles, "right",self.bg_image):
                self.pixels_remaining=TILE_SIZE
                self.rect.x+=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="right"
            self.rect.x=TILE_SIZE*round(self.rect.x/TILE_SIZE)
            self.rect.y=TILE_SIZE*round(self.rect.y/TILE_SIZE)
        if self.pixels_remaining>0:
            if self.moving_direction=="up":
                self.rect.y-=move_speed
            if self.moving_direction=="down":
                self.rect.y+=move_speed
            if self.moving_direction=="left":
                self.rect.x-=move_speed
            if self.moving_direction=="right":
                self.rect.x+=move_speed

            self.pixels_remaining-=move_speed
    
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

'''
class Player:
    def __init__(self,anim_frames):
        self.walking_down_1=anim_frames[0]
        self.facing_down=anim_frames[1]
        self.walking_down_2=anim_frames[2]
        self.walking_up_1=anim_frames[3]
        self.facing_up=anim_frames[4]
        self.walking_up_2=anim_frames[5]
        self.facing_left=anim_frames[6]
        self.walking_left=anim_frames[7]
        self.facing_right=anim_frames[8]
        self.walking_right=anim_frames[9]        '''