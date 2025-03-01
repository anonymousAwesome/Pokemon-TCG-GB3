import pygame
import random
import os
import key_mappings

TILE_SIZE=64
anim_speed=32

def load_sprites_from_sheet(spritesheet, row):
    sprites = []
    for i in range(10):
        x = i*17 + 1
        y = row*17 + 1
        sprite=spritesheet.subsurface(pygame.Rect(x, y, 16, 16))
        sprite=pygame.transform.scale(sprite, (16*4, 16*4))
        sprites.append(sprite)
    return sprites


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, anim_frames):
        pygame.sprite.Sprite.__init__(self)
        self.anim_frames=anim_frames
        self.image = anim_frames[1]
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y

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
        self.move  = 4 #Just to be safe, keep it a factor of 64: 1, 2, 4, 8, 16, 32, or 64.
        self.pixels_remaining=0
        self.facing_direction="down"
        self.walking_side=True
        self.fast_walking=False
        self.up_command=False
        self.down_command=False
        self.left_command=False
        self.right_command=False

    def draw(self, surface, camera_x_offset, camera_y_offset):
        surface.blit(self.image, (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))

    def flip_walking_side(self):
        self.walking_side=not self.walking_side

    def change_facing(self):
        if self.up_command:
            self.facing_direction="up"
            self.image=self.facing_up
        elif self.down_command:
            self.facing_direction="down"
            self.image=self.facing_down
        elif self.left_command:
            self.facing_direction="left"
            self.image=self.facing_left
        elif self.right_command:
            self.facing_direction="right"
            self.image=self.facing_right

    def start_walking(self,move_speed):
        self.change_facing()
        if self.up_command:
            self.flip_walking_side()
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
        elif self.down_command:
            self.flip_walking_side()
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
        elif self.left_command:
            self.pixels_remaining=TILE_SIZE
            self.rect.x-=move_speed
            self.pixels_remaining-=move_speed
            if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                self.image=self.facing_left
            else:
                self.image=self.walking_left
        elif self.right_command:
            self.pixels_remaining=TILE_SIZE
            self.rect.x+=move_speed
            self.pixels_remaining-=move_speed
            if ((TILE_SIZE - self.pixels_remaining) // anim_speed) %2:
                self.image=self.facing_right
            else:
                self.image=self.walking_right
        
    def continue_walking(self,move_speed):
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


    def move_character(self,can_move):
        move_speed=self.move
        if self.fast_walking:
            move_speed=self.move*2
        if self.pixels_remaining<0:
            self.pixels_remaining=0
        if self.pixels_remaining==0:
            self.rect.x=TILE_SIZE*round(self.rect.x/TILE_SIZE)
            self.rect.y=TILE_SIZE*round(self.rect.y/TILE_SIZE)
            if can_move:
                self.start_walking(move_speed)
            else:
                self.change_facing()
        elif self.pixels_remaining>0:
            self.continue_walking(move_speed)

class Player(Character):
    def __init__(self, x, y, anim_frames):
        super().__init__(x, y, anim_frames)

    def process_input(self,keys):
        if keys[key_mappings.cancel_key]:
            self.fast_walking=True
        else:
            self.fast_walking=False

        if keys[key_mappings.up_key]:
            self.up_command=True
        else:
            self.up_command=False

        if keys[key_mappings.down_key]:
            self.down_command=True
        else:
            self.down_command=False

        if keys[key_mappings.left_key]:
            self.left_command=True
        else:
            self.left_command=False

        if keys[key_mappings.right_key]:
            self.right_command=True
        else:
            self.right_command=False

class NPC(Character):
    def __init__(self, x, y, anim_frames):
        super().__init__(x, y, anim_frames)

    def random_jitter(self):
        movementx=random.choice([-1,1])
        movementy=random.choice([-1,1])
        self.rect.y+=movementy
        self.rect.x+=movementx
        
    def random_input(self):
        self.right_command=False
        self.left_command=False
        self.up_command=False
        self.down_command=False

        rand_choices=random.randint(1,4)
        if rand_choices==1:
            self.right_command=True
        if rand_choices==2:
            self.left_command=True
        if rand_choices==3:
            self.up_command=True
        if rand_choices==4:
            self.down_command=True
        super().move_character()

    def walk_in_place(self):
        pass
