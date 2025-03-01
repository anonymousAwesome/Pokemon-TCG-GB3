import pygame
import random
import os







            
    

    def can_move(self, obstacles, direction):
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
        if next_rect.right > self.bg_image.get_width():
            return False

        # Check vertical bounds
        if next_rect.y < 0:
            return False
        if next_rect.bottom > self.bg_image.get_height():
            return False

        # Check for collisions with obstacles
        for obstacle in obstacles:
            if next_rect.colliderect(obstacle):
                return False

        # If all checks passed, the movement is valid
        return True



