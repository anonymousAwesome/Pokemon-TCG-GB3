import pygame
import numpy as np
import math

class Rotation:
    def __init__(self):
        self.current_angle = 0
        self.rotation_amount = 5
        # Precompute matrices
        self.rgb_to_xyz = np.array([
            [0.4124, 0.3576, 0.1805],
            [0.2126, 0.7152, 0.0722],
            [0.0193, 0.1192, 0.9505]
        ])
        self.xyz_to_rgb = np.array([
            [3.2406, -1.5372, -0.4986],
            [-0.9689, 1.8758, 0.0415],
            [0.0557, -0.2040, 1.0570]
        ])

    def rotate_hue(self, rgba_color):
        r, g, b, a = rgba_color
        # Convert to linear RGB with clipping to avoid negative values
        rgb = np.array([r, g, b]) / 255.0
        rgb_lin = np.where(
            rgb <= 0.04045,
            rgb / 12.92,
            ((rgb + 0.055) / 1.055) ** 2.4
        )
        
        # Convert to XYZ
        xyz = np.dot(self.rgb_to_xyz, rgb_lin)
        xyz /= np.array([0.95047, 1.0, 1.08883])  # D65 white point
        
        # Convert to Lab with epsilon to avoid log(0)
        epsilon = 1e-10
        xyz = np.where(xyz > 0.008856, xyz ** (1/3), (7.787 * xyz) + (16/116))
        L = np.maximum(0, 116 * xyz[1] - 16)
        a = 500 * (xyz[0] - xyz[1])
        b = 200 * (xyz[1] - xyz[2])
        
        # Rotate hue
        h_rad = np.radians(self.current_angle)
        new_a = a * np.cos(h_rad) - b * np.sin(h_rad)
        new_b = a * np.sin(h_rad) + b * np.cos(h_rad)
        
        # Convert back to XYZ
        y = (L + 16) / 116
        x = new_a / 500 + y
        z = y - new_b / 200
        
        xyz = np.where(
            np.array([x, y, z]) > 0.2068966,
            np.array([x, y, z]) ** 3,
            (np.array([x, y, z]) - 16/116) / 7.787
        )
        xyz *= np.array([0.95047, 1.0, 1.08883])
        
        # Convert back to linear RGB with clipping
        rgb_lin = np.dot(self.xyz_to_rgb, xyz)
        rgb_lin = np.clip(rgb_lin, 0, 1)  # Prevent negative values
        
        # Convert to sRGB
        srgb = np.where(
            rgb_lin <= 0.0031308,
            12.92 * rgb_lin,
            1.055 * (rgb_lin ** (1/2.4)) - 0.055
        )
        srgb = np.clip(np.round(srgb * 255), 0, 255).astype(np.uint8)
        
        return (*srgb, a)

    def modify_colors(self, surface):
        pixels = pygame.surfarray.pixels3d(surface)
        chosen_color = np.array([128, 255, 0])
        
        # Create mask for pixels matching chosen_color (with tolerance)
        mask = np.all(np.abs(pixels - chosen_color) < 10, axis=2)
        
        if np.any(mask):
            rotated_color = self.rotate_hue((*chosen_color, 255))
            pixels[mask] = rotated_color[:3]
        
        self.current_angle = (self.current_angle + self.rotation_amount) % 360
        del pixels  # Unlock surface
        return surface
