import os
import pygame
from PIL import Image, ImageChops
import pytest
import overworld
import duel

'''
#currently more trouble than it's worth

def take_screenshot_and_compare(screen, name, golden_master_dir="golden_masters", diff_dir="diff_images"):
    # Ensure directories exist
    os.makedirs(golden_master_dir, exist_ok=True)
    os.makedirs(diff_dir, exist_ok=True)

    # Define paths for the screenshot and golden master images
    screenshot_path = os.path.join(diff_dir, f"{name}_screenshot.png")
    golden_master_path = os.path.join(golden_master_dir, f"{name}.png")
    diff_image_path = os.path.join(diff_dir, f"{name}_diff.png")

    # Save the screenshot as a PNG file
    pygame.image.save(screen, screenshot_path)

    # If the golden master does not exist, save the screenshot as the golden master
    if not os.path.exists(golden_master_path):
        pygame.image.save(screen, golden_master_path)
        return  # No need to compare, as this is the first screenshot

    # Otherwise, compare the screenshot with the golden master
    golden_master = Image.open(golden_master_path)

    # Convert the Pygame Surface to a Pillow Image using tobytes
    screen_bytes = pygame.image.tobytes(screen,"RGB")
    screen_width, screen_height = screen.get_size()
    #glitched
    #screenshot_image = Image.frombytes('RGB', (screen_width, screen_height), screen_bytes).transpose(Image.TRANSPOSE)
    
    #non-glitched
    screenshot_image = Image.frombytes('RGB', (screen_width, screen_height), screen_bytes)

    # Create the diff image
    diff = ImageChops.difference(screenshot_image, golden_master)

    # If images are different, save the diff and raise an error
    if diff.getbbox():  # There's a difference
        diff.save(diff_image_path)

        try:
            assert False, f"Images differ! See the diff at {diff_image_path}"
        except AssertionError:
            print(f"Assertion failed! Check the diff image at {diff_image_path}")
            diff.show()  # Display the diff image
            raise  # Re-raise to ensure pytest captures the failure

def test_hard_coded_duel_check_screen():
    overworld.render()
    take_screenshot_and_compare(overworld.screen,"overworld")
    '''