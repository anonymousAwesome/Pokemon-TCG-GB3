import pygame
pygame.init()
screen = pygame.display.set_mode((640,576))
pygame.display.set_caption("club exploration")
clock = pygame.time.Clock()
TILE_SIZE=64


mapname="flying"
#mapname="neo continent"
#mapname="neo stadium"
#mapname="tcg island"

if mapname=="flying":
    bg_image = pygame.image.load("./assets/maps/flying club.png")
    #flying club
    obstacles=[
        pygame.Rect(0, 0, 64, 960),
        pygame.Rect(832, 0, 64, 960),
        pygame.Rect(64, 0, 768, 64),
        pygame.Rect(512, 896, 320, 64),
        pygame.Rect(512, 832, 320, 64),
        pygame.Rect(64, 832, 320, 64),
        pygame.Rect(64, 896, 320, 64),
        pygame.Rect(256, 192, 64, 256),
        pygame.Rect(640, 320, 64, 256),
        pygame.Rect(64, 640, 192, 64),
        pygame.Rect(64, 704, 192, 64),
        pygame.Rect(64, 768, 128, 64),
        pygame.Rect(192, 192, 64, 128),
        pygame.Rect(320, 192, 64, 128),
        pygame.Rect(576, 320, 64, 128),
        pygame.Rect(704, 320, 64, 128),
    ]
    player_starting_location=(6*64,13*64)

elif mapname =="neo continent":
    bg_image = pygame.image.load("./assets/maps/neo continent.png")
    obstacles=[
        pygame.Rect(0, 576, 896, 64),
        pygame.Rect(0, 0, 64, 576),
        pygame.Rect(768, 0, 64, 576),
        pygame.Rect(832, 0, 64, 576),
        pygame.Rect(256, 320, 448, 64),
        pygame.Rect(64, 192, 64, 384),
        pygame.Rect(128, 192, 64, 384),
        pygame.Rect(512, 256, 256, 64),
        pygame.Rect(512, 192, 256, 64),
        pygame.Rect(512, 512, 256, 64),
        pygame.Rect(256, 448, 192, 64),
        pygame.Rect(512, 64, 192, 64),
        pygame.Rect(256, 64, 192, 64),
        pygame.Rect(256, 128, 192, 64),
        pygame.Rect(256, 192, 192, 64),
        pygame.Rect(64, 64, 128, 64),
        pygame.Rect(64, 0, 128, 64),
        pygame.Rect(256, 384, 128, 64),
        pygame.Rect(512, 448, 64, 64),
    ]

    player_starting_location=(64,128)

elif mapname=="neo stadium":
    bg_image = pygame.image.load("./assets/maps/neo stadium.png")
    obstacles=[
    pygame.Rect(0, 0, 64, 1024),
    pygame.Rect(832, 0, 64, 1024),
    pygame.Rect(64, 0, 768, 64),
    pygame.Rect(512, 640, 320, 64),
    pygame.Rect(512, 896, 320, 64),
    pygame.Rect(512, 960, 320, 64),
    pygame.Rect(64, 960, 320, 64),
    pygame.Rect(64, 896, 320, 64),
    pygame.Rect(64, 640, 320, 64),
]

    player_starting_location=(6*64,14*64)

elif mapname=="tcg island":
    bg_image = pygame.image.load("./assets/maps/tcg island.png")
    obstacles=[
    pygame.Rect(0, 0, 640, 64),
    pygame.Rect(0, 512, 640, 64),
    pygame.Rect(0, 64, 64, 448),
    pygame.Rect(576, 64, 64, 448),
    pygame.Rect(64, 64, 320, 64),
    pygame.Rect(64, 384, 64, 64),
]

    player_starting_location=(1*64,7*64)



class Player( pygame.sprite.Sprite ):

    def __init__( self, x, y, player_image ):
        pygame.sprite.Sprite.__init__( self )
        self.image = player_image
        self.image=pygame.transform.scale_by(self.image,4)
        self.rect  = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        self.move  = 4 #Just to be safe, keep it a factor of 64: 1, 2, 4, 8, 16, 32, or 64.
        self.pixels_remaining=0
        self.moving_direction=None

    def update( self,pressed_keys ):
        move_speed=self.move
        if keys[pygame.K_LALT] or keys[pygame.K_RALT]:
            move_speed=self.move*2
        if self.pixels_remaining<=0:
            if keys[pygame.K_UP] and can_move(player_sprite.rect, obstacles, "up"):
                self.pixels_remaining=TILE_SIZE
                self.rect.y-=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="up"
            if keys[pygame.K_DOWN]and can_move(player_sprite.rect, obstacles, "down"):
                self.pixels_remaining=TILE_SIZE
                self.rect.y+=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="down"
            if keys[pygame.K_LEFT]and can_move(player_sprite.rect, obstacles, "left"):
                self.pixels_remaining=TILE_SIZE
                self.rect.x-=move_speed
                self.pixels_remaining-=move_speed
                self.moving_direction="left"
            if keys[pygame.K_RIGHT]and can_move(player_sprite.rect, obstacles, "right"):
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
        # Draw the player adjusted for the clamped camera offsets
        surface.blit(self.image, (self.rect.x + camera_x_offset, self.rect.y + camera_y_offset))

def can_move(rect, obstacles, direction):
    next_rect = rect.copy()
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


player_image   = pygame.image.load( './assets/player_image.png' ).convert_alpha()
player_sprite  = Player(player_starting_location[0],player_starting_location[1],player_image)


bg_width, bg_height = bg_image.get_width(), bg_image.get_height()
bg_image = pygame.transform.scale(bg_image, (bg_width * 4, bg_height * 4))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()    

    player_sprite.update(keys)
    
    camera_x_offset = -max(0, min(bg_width * 4 - 640, (player_sprite.rect.centerx - 320)))
    camera_y_offset = -max(0, min(bg_height * 4 - 576, (player_sprite.rect.centery - 288)))
    screen.blit(bg_image, (camera_x_offset, camera_y_offset))
    #for ob in obstacles:
    #    pygame.draw.rect(screen, (255,255,0), ob.move(camera_x_offset, camera_y_offset))
    player_sprite.draw(screen, camera_x_offset, camera_y_offset)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
