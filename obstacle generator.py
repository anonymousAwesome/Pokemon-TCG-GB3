"""
This code loads a tile-based background image and lets you click the 
obstacle tiles, turning them red. When you're ready, press the spacebar
and it will print a list of rects generated from those tiles.

The rects are combined into a row or a column where possible to reduce 
list size, though I admit it wasn't particularly necessary.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
INITIAL_TILE_SIZE = 16
IMAGE_SCALE=2
RECT_SCALE=2
TILE_SIZE=INITIAL_TILE_SIZE*IMAGE_SCALE
FPS = 60
SELECTION_COLOR = (255, 0, 0, 128)  # Red with transparency

# Load the tilemap
TILEMAP_PATH = "./assets/Neo Continent.png"  # Replace with your tilemap image path
tilemap = pygame.image.load(TILEMAP_PATH)
tilemap=pygame.transform.scale_by(tilemap,2)

SCREEN_HEIGHT=tilemap.get_height()
SCREEN_WIDTH=tilemap.get_width()

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tilemap Selector")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Store selected tiles as Pygame Rects
selected_tiles = []

def rect_exists(rect):
    """Check if a rect exists in the selected_tiles list."""
    return any(rect.collidepoint(tile_rect.topleft) for tile_rect in selected_tiles)

def generate_merged_rects(selected_tiles):
    """Generate merged rectangles from selected tiles."""
    remaining_tiles = selected_tiles[:]
    merged_rects = []

    while remaining_tiles:
        best_rect = None
        best_count = 0
        best_orientation = None

        # Check horizontally
        for rect in remaining_tiles:
            count = 1  # Start with the initial tile
            test_rect = rect.copy()
            while any(tile.topleft == test_rect.topright for tile in remaining_tiles):
                test_rect.width += TILE_SIZE
                count += 1
            if count > best_count:
                best_count = count
                best_rect = test_rect
                best_orientation = "horizontal"

        # Check vertically
        for rect in remaining_tiles:
            count = 1  # Start with the initial tile
            test_rect = rect.copy()
            while any(tile.topleft == test_rect.bottomleft for tile in remaining_tiles):
                test_rect.height += TILE_SIZE
                count += 1
            if count > best_count:
                best_count = count
                best_rect = test_rect
                best_orientation = "vertical"

        # If we found a best rect, finalize it
        if best_rect:
            if best_orientation == "horizontal":
                best_rect.width = TILE_SIZE * best_count
            elif best_orientation == "vertical":
                best_rect.height = TILE_SIZE * best_count
            merged_rects.append(best_rect)

            # Remove all tiles covered by the best_rect
            remaining_tiles = [
                rect for rect in remaining_tiles
                if not best_rect.colliderect(rect)
            ]
        else:
            # Add the remaining single tile as a rect
            merged_rects.append(remaining_tiles.pop(0))

    return merged_rects

def generate_code(merged_rects):
    """Generate Python code for creating merged rects."""
    rects_code = "obstacles=[\n"
    for rect in merged_rects:
        rects_code += f"    pygame.Rect({rect.x*RECT_SCALE}, {rect.y*RECT_SCALE}, {rect.width*RECT_SCALE}, {rect.height*RECT_SCALE}),\n"
        #rects_code += f"    pygame.Rect({rect.x//TILE_SIZE}, {rect.y//TILE_SIZE}, {rect.width//TILE_SIZE}, {rect.height//TILE_SIZE}),\n"
    rects_code += "]"
    return rects_code

def main():
    running = True
    global selected_tiles

    while running:
        screen.blit(tilemap, (0, 0))  # Draw the tilemap

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Get mouse position and calculate the tile rect
                mouse_x, mouse_y = event.pos
                tile_x = (mouse_x // TILE_SIZE) * TILE_SIZE
                tile_y = (mouse_y // TILE_SIZE) * TILE_SIZE
                tile_rect = pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)

                # Add or remove the tile from selected_tiles
                if rect_exists(tile_rect):
                    selected_tiles = [rect for rect in selected_tiles if not rect.collidepoint(tile_rect.topleft)]
                else:
                    selected_tiles.append(tile_rect)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Generate merged rectangles
                merged_rects = generate_merged_rects(selected_tiles)
                print("Selected tiles as rects:")
                print(generate_code(merged_rects))

        # Draw selected tiles as semi-transparent overlays
        for rect in selected_tiles:
            s = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)  # Create a surface with alpha channel
            s.fill(SELECTION_COLOR)
            screen.blit(s, rect.topleft)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
