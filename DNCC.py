'''dialogue, NPCs, cutscenes, clubs'''

import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 576
TILE_SIZE = 64
PLAYER_SIZE = 16
BACKGROUND_SCALE = 4
FPS = 60

# Colors
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)

# Initialize window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2D Top-Down Game")

# Load and scale background image
background = pygame.image.load("background.png")  # Replace with your image file
bg_width, bg_height = background.get_size()
background = pygame.transform.scale(background, (bg_width * BACKGROUND_SCALE, bg_height * BACKGROUND_SCALE))
background_rect = background.get_rect()

# Player setup
player = pygame.Rect(TILE_SIZE, TILE_SIZE, PLAYER_SIZE, PLAYER_SIZE)  # Start at (64, 64)
player_color = GREEN

# Magenta obstacles
obstacles = [
    pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
    for x in range(128, 512, TILE_SIZE)
    for y in range(128, 512, TILE_SIZE)
]

# Camera setup
camera_x, camera_y = 0, 0

def move_camera(player_rect, camera_rect):
    """Center the camera on the player but constrain it within the background bounds."""
    camera_rect.x = max(0, min(player_rect.centerx - WINDOW_WIDTH // 2, background_rect.width - WINDOW_WIDTH))
    camera_rect.y = max(0, min(player_rect.centery - WINDOW_HEIGHT // 2, background_rect.height - WINDOW_HEIGHT))

# Movement logic
def move_player(player_rect, direction, obstacles):
    """Move player and snap to grid while preventing collisions."""
    if direction == "up":
        target = player_rect.y - TILE_SIZE
        while player_rect.y > target:
            player_rect.y -= 1
            if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
                player_rect.y += 1
                break
    elif direction == "down":
        target = player_rect.y + TILE_SIZE
        while player_rect.y < target:
            player_rect.y += 1
            if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
                player_rect.y -= 1
                break
    elif direction == "left":
        target = player_rect.x - TILE_SIZE
        while player_rect.x > target:
            player_rect.x -= 1
            if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
                player_rect.x += 1
                break
    elif direction == "right":
        target = player_rect.x + TILE_SIZE
        while player_rect.x < target:
            player_rect.x += 1
            if any(player_rect.colliderect(obstacle) for obstacle in obstacles):
                player_rect.x -= 1
                break

# Game loop
clock = pygame.time.Clock()
running = True
camera = pygame.Rect(camera_x, camera_y, WINDOW_WIDTH, WINDOW_HEIGHT)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_player(player, "up", obstacles)
    elif keys[pygame.K_DOWN]:
        move_player(player, "down", obstacles)
    elif keys[pygame.K_LEFT]:
        move_player(player, "left", obstacles)
    elif keys[pygame.K_RIGHT]:
        move_player(player, "right", obstacles)

    # Update camera position
    move_camera(player, camera)

    # Draw background
    screen.blit(background, (-camera.x, -camera.y))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, MAGENTA, obstacle.move(-camera.x, -camera.y))

    # Draw player
    pygame.draw.rect(screen, player_color, player.move(-camera.x, -camera.y))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
