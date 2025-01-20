import pygame
import ui


pygame.init()
screen = pygame.display.set_mode((640,576))
clock = pygame.time.Clock()
background=pygame.image.load("./assets/bg3.jpg").convert()
background=pygame.transform.scale(background, (640,576))

font = pygame.font.Font("./assets/pokemon-emerald.otf", 40)
test_options="  Game Board   Attack      Hand      Retreat\n  Pkmn power   End turn   Resign"


# Constants for screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 576

# Constants for the dialogue box
BOX_WIDTH = 600
BOX_HEIGHT = 124
BOX_MARGIN_BOTTOM = 24  # Distance from the bottom of the screen
BOX_BORDER_WIDTH = 6
BOX_HIGHLIGHT_WIDTH = 2

# Colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 200)
COLOR_HIGHLIGHT = (125, 125, 255)
COLOR_BLACK = (0,0,0)

# Calculated box position
BOX_X = (SCREEN_WIDTH - BOX_WIDTH) // 2
BOX_Y = SCREEN_HEIGHT - BOX_HEIGHT - BOX_MARGIN_BOTTOM

background=pygame.image.load("./assets/bg3.jpg").convert()
background=pygame.transform.scale(background, (640,576))


def render():

    screen.blit(background,(0,0))

    ui.bg_box(screen,BOX_X,BOX_Y,BOX_WIDTH,BOX_HEIGHT)

    # Render dialogue text

    vert_margin=15
    hor_margin=16

    lines = test_options.split("\n")
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, COLOR_BLACK)
        text_x = BOX_X + hor_margin
        text_y = BOX_Y + vert_margin + i * 45
        screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    render()
pygame.quit()