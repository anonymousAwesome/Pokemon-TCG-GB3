"""
This code loads a tile-based background image and lets you click the 
obstacle tiles, turning them red. When you're ready, press the spacebar
and it will print a list of rects generated from those tiles.

The rects are combined into a row or a column where possible to reduce 
list size, though I admit it wasn't particularly necessary.

screen_scale is the scale factor of the tiles, the window, and the visible
rectangles. rect_scale only scales the output rects. The two variables 
should be mutually exclusive; the program applies one or the other, not both.
"""

import pygame
import sys

pygame.init()

tile_size = 16
screen_scale = 3
#screen_scale ranges from 2-4, depending on how the window fits onto 
#the screen.
visible_tile_size=tile_size*screen_scale
rect_scale = 4
fps = 60
selection_color = (255, 0, 0, 128)

TILEMAP_PATH = "./assets/maps/mason center.png"
tilemap = pygame.image.load(TILEMAP_PATH)
tilemap = pygame.transform.scale(tilemap, (tilemap.get_width() * screen_scale, tilemap.get_height() * screen_scale))


SCREEN_HEIGHT=tilemap.get_height()
SCREEN_WIDTH=tilemap.get_width()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tilemap Selector")

clock = pygame.time.Clock()

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
                test_rect.width += visible_tile_size
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
                test_rect.height += visible_tile_size
                count += 1
            if count > best_count:
                best_count = count
                best_rect = test_rect
                best_orientation = "vertical"

        # If we found a best rect, finalize it
        if best_rect:
            if best_orientation == "horizontal":
                best_rect.width = visible_tile_size * best_count
            elif best_orientation == "vertical":
                best_rect.height = visible_tile_size * best_count
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
    rects_code = "\"obstacles\":[\n"
    for rect in merged_rects:
        rects_code += f"    pygame.Rect({rect.x // screen_scale * rect_scale}, {rect.y // screen_scale * rect_scale}, {rect.width // screen_scale * rect_scale}, {rect.height // screen_scale * rect_scale}),\n"
        #rects_code += f"    pygame.Rect({rect.x//TILE_SIZE}, {rect.y//TILE_SIZE}, {rect.width//TILE_SIZE}, {rect.height//TILE_SIZE}),\n"
    rects_code += "]"
    return rects_code

def main():
    running = True
    global selected_tiles

    while running:
        screen.blit(tilemap, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                tile_x = (mouse_x // (visible_tile_size)) * visible_tile_size
                tile_y = (mouse_y // (visible_tile_size)) * visible_tile_size
                tile_rect = pygame.Rect(tile_x, tile_y, visible_tile_size, visible_tile_size)

                if rect_exists(tile_rect):
                    selected_tiles = [rect for rect in selected_tiles if not rect.collidepoint(tile_rect.topleft)]
                else:
                    selected_tiles.append(tile_rect)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                merged_rects = generate_merged_rects(selected_tiles)
                print("Selected tiles as rects:")
                print(generate_code(merged_rects))

        for rect in selected_tiles:
            s = pygame.Surface((visible_tile_size, visible_tile_size), pygame.SRCALPHA)
            s.fill(selection_color)
            screen.blit(s, rect.topleft)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
