import pygame
import random
import os
import key_mappings

TILE_SIZE=64
anim_speed=32

spritesheet_yellow_path = os.path.join("assets","npc sprites","pokemon yellow sprites recolored.png")
spritesheet_crystal_path = os.path.join("assets","npc sprites","pokemon crystal sprites recolored.png")
spritesheet_tcg2_path = os.path.join("assets","npc sprites","pokemon tcg2 sprites.png")
spritesheet_gb3_path = os.path.join("assets","npc sprites","GB3 sprites.png")
portrait_sheet_GB2_path=os.path.join("assets","duellists","GB2 profiles.png")

spritesheet_yellow=pygame.image.load(spritesheet_yellow_path).convert_alpha()
spritesheet_crystal=pygame.image.load(spritesheet_crystal_path).convert_alpha()
spritesheet_tcg2=pygame.image.load(spritesheet_tcg2_path).convert_alpha()
spritesheet_gb3=pygame.image.load(spritesheet_gb3_path).convert_alpha()

portrait_sheet_GB2=pygame.image.load(portrait_sheet_GB2_path).convert()

def load_portrait_from_sheet(portrait_sheet,row,column,max_width=48,max_height=48,image_width=48,image_height=48):
    portrait=portrait_sheet.subsurface(pygame.Rect(row*max_width, column*max_height, image_width, image_height))
    portrait=pygame.transform.scale(portrait, (image_width*4, image_height*4))
    return portrait

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
    def __init__(self, x, y, anim_frames,facing_direction):
        pygame.sprite.Sprite.__init__(self)
        self.anim_frames=anim_frames
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
        self.walking_side=True
        self.fast_walking=False
        self.up_command=False
        self.down_command=False
        self.left_command=False
        self.right_command=False
        self.accept_key=False
        self.visible=True

        self.facing_direction=facing_direction
        self.map_exit_change_facing()
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y

    def toggle_visibility(self):
        self.visible=not self.visible

    def draw(self, surface, camera_x_offset, camera_y_offset,inner_context):
        if self.visible:
            if inner_context.player_data.currently_greyscale:
                surface.blit(inner_context.perceptual_greyscale(self.image), (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))
            else:
                surface.blit(self.image, (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))

    def flip_walking_side(self):
        self.walking_side=not self.walking_side

    def cutscene_walk(self,direction):
        self.up_command=False
        self.down_command=False
        self.left_command=False
        self.right_command=False
        
        if direction=="left":
            self.left_command=True
        if direction=="right":
            self.right_command=True
        if direction=="up":
            self.up_command=True
        if direction=="down":
            self.down_command=True

    def still_walking(self):
        return self.pixels_remaining

    def map_exit_change_facing(self):
        if self.facing_direction=="up":
            self.image=self.facing_up
        elif self.facing_direction=="down":
            self.image=self.facing_down
        elif self.facing_direction=="left":
            self.image=self.facing_left
        elif self.facing_direction=="right":
            self.image=self.facing_right
        

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
    def __init__(self, x, y, anim_frames,facing_direction):
        super().__init__(x, y, anim_frames,facing_direction)

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

        if keys[key_mappings.affirm_key]:
            self.accept_key=True
        else:
            self.accept_key=False


class NPC(Character):
    def __init__(self, x, y, anim_frames,facing_direction):
        super().__init__(x, y, anim_frames,facing_direction)
        self.frame_duration=17
        self.loop_counter=random.randint(1,self.frame_duration*4)

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

    def manual_direction_change(self,direction):
        self.facing_direction=direction

    def walk_in_place(self):
        if self.facing_direction=="down":
            if self.loop_counter>self.frame_duration*4:
                self.loop_counter=1
            if self.loop_counter<=self.frame_duration:
                self.image=self.walking_down_1
            elif self.loop_counter<=self.frame_duration*2:
                self.image=self.facing_down
            elif self.loop_counter<=self.frame_duration*3:
                self.image=self.walking_down_2
            elif self.loop_counter<=self.frame_duration*4:
                self.image=self.facing_down
        if self.facing_direction=="up":
            if self.loop_counter>self.frame_duration*4:
                self.loop_counter=1
            if self.loop_counter<=self.frame_duration:
                self.image=self.walking_up_1
            elif self.loop_counter<=self.frame_duration*2:
                self.image=self.facing_up
            elif self.loop_counter<=self.frame_duration*3:
                self.image=self.walking_up_2
            elif self.loop_counter<=self.frame_duration*4:
                self.image=self.facing_up
        if self.facing_direction=="left":
            if self.loop_counter>self.frame_duration*2:
                self.loop_counter=1
            if self.loop_counter<=self.frame_duration:
                self.image=self.facing_left
            elif self.loop_counter<=self.frame_duration*2:
                self.image=self.walking_left
            elif self.loop_counter<=self.frame_duration*3:
                self.image=self.facing_left
            elif self.loop_counter<=self.frame_duration*4:
                self.image=self.walking_left
        if self.facing_direction=="right":
            if self.loop_counter>self.frame_duration*2:
                self.loop_counter=1
            if self.loop_counter<=self.frame_duration:
                self.image=self.facing_right
            elif self.loop_counter<=self.frame_duration*2:
                self.image=self.walking_right
            elif self.loop_counter<=self.frame_duration*3:
                self.image=self.facing_right
            elif self.loop_counter<=self.frame_duration*4:
                self.image=self.walking_right
        
        self.loop_counter+=1