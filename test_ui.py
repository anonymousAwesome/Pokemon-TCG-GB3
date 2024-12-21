import pygame
import pytest
import ui

DOWN=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
UP=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
LEFT=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
RIGHT=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
RETURN=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)


def test_go_down_one_item_and_hit_enter():
    menu = ui.Menu(["status","diary","deck","mini-com","coins"],1)
    events = [DOWN,RETURN]
    
    for event in events:
        menu.handle_input(event)

    assert menu.location == "diary"


def test_over_and_down_in_3x2():
    menu = ui.Menu(["status","diary","deck","mini-com","coins"],3)
    events = [DOWN, RETURN]

    for event in events:
        menu.handle_input(event)

    assert menu.location=="mini-com"

'''
to-do:
left, right, up and down tests
block movement onto a "" cell, otherwise wrap around.
'''