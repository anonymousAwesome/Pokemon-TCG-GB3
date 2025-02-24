import os

'''

Contains the user interface for Pokemon duels; the cursor, displaying things
on screen, selecting things on screen, etc.

to-do:
compensate for trainer/pokemon image size difference
add second screen
apply effects to benched pokemon
move elements around if there is or isn't a stadium in play;
either center the coin flips or scooch the active pokemon closer together

background from:
https://www.spriters-resource.com/pc_computer/rpgmaker95/sheet/100509/

other locations:
https://www.spriters-resource.com/snes/ff6/sheet/54685/
https://www.spriters-resource.com/pc_computer/rpgmaker2000/sheet/100455/
https://www.spriters-resource.com/game_boy_advance/finalfantasy4advance/sheet/5235/
https://www.spriters-resource.com/game_boy_advance/finalfantasy1dawnofsouls/sheet/25293/
https://www.spriters-resource.com/sega_genesis_32x/sf2/sheet/48892/
https://www.spriters-resource.com/snes/rpgtsukuru2rpgmaker2jpn/sheet/128717/
https://www.spriters-resource.com/game_boy_advance/sfgba/sheet/25081/
https://www.spriters-resource.com/snes/ff5/sheet/30401/
https://www.spriters-resource.com/sega_genesis_32x/sf1/sheet/41886/

med-res
https://www.spriters-resource.com/mobile/thebattlecats/sheet/81277/
https://www.spriters-resource.com/game_boy_advance/khcom/sheet/1045/

high-res, might need downscaling:
https://www.spriters-resource.com/pc_computer/rpgmakerxp/sheet/100495/
https://www.spriters-resource.com/playstation/lunar2ebc/sheet/30268/
https://www.spriters-resource.com/playstation/lunarssc/sheet/26636/
https://www.spriters-resource.com/pc_computer/finalfantasypixelremaster/sheet/159179/
https://www.spriters-resource.com/psp/finalfantasy2/sheet/43692/
https://www.spriters-resource.com/pc_computer/rpgmaker2003/sheet/100476/
https://www.spriters-resource.com/game_boy_advance/finalfantasy2dawnofsouls/sheet/25026/
https://www.spriters-resource.com/pc_computer/rpgmakerxp/sheet/100494/
https://www.spriters-resource.com/fullview/96002/
'''

import pygame

'''
duel_manager = cd.DuelManager(phase_handler)
player1 = cd.Player(duel_manager)
player2 = cd.Player(duel_manager)
deck1=decks.generate([[cards.water,17],[cards.dratini,4],[cards.hitmonchan,3],[cards.seel,1],[cards.machop,1]],player1)
deck2=decks.generate([[cards.water,17],[cards.dratini,4],[cards.hitmonchan,3],[cards.seel,1],[cards.machop,1]],player1)
player1.deck.cards=deck1
player2.deck.cards=deck2
player1.initial_draw()
player2.initial_draw()
player1.prizes.place()
player1.prizes.place()

#duel_manager.starting_coin()
duel_manager.turn="player" #manually let the player go first
'''

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 640, 576

font = pygame.font.Font(os.path.join("assets","pokemon-emerald.otf"), 40)
'''to-do: rework the font area to be more like the other screen: full
opacity, blue outlines, pokemon-emerald font.
Also, possibly swap the prizes and font areas to make space for the 
effects on the left side of the Pokemon. Maybe. Needs workshopping.
Maybe shrink the Pokemon images and add a border around each one showing
its type.'''


large_pkmn_card_dims=252,176
med_pkmn_card_dims=84,59
small_pkmn_card_dims=55,38
stadium_dims=112,61
card_back_dims=44,61

screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Pokemon Card Game Layout")

pkmn_card1=pygame.image.load("./assets/voltorb.jpg").convert()
pkmn_card2=pygame.image.load("./assets/ponyta.jpg").convert()
stadium_card=pygame.image.load("./assets/energy stadium.jpg").convert()
card_back=pygame.image.load("./assets/cardback.jpg").convert()
large_pkmn_card1=pygame.transform.scale(pkmn_card1, large_pkmn_card_dims)
large_pkmn_card2=pygame.transform.scale(pkmn_card2, large_pkmn_card_dims)
stadium_card=pygame.transform.scale(stadium_card, stadium_dims)
med_pkmn_card1=pygame.transform.scale(pkmn_card1, med_pkmn_card_dims)
med_pkmn_card2=pygame.transform.scale(pkmn_card2, med_pkmn_card_dims)
small_pkmn_card1=pygame.transform.scale(pkmn_card1, small_pkmn_card_dims)
small_pkmn_card2=pygame.transform.scale(pkmn_card2, small_pkmn_card_dims)
card_back=pygame.transform.scale(card_back, card_back_dims)

background=pygame.image.load("./assets/duel backgrounds/city skyline.jpg").convert()
'''
note: image was exported from png to jpg at ~50% quality. A little blurring,
but that is good and bad, depending on the location. And it cut the file 
size in half.
'''

background=pygame.transform.scale(background, (640,576))

player1_active_pokemon_position = (194,324)
player2_active_pokemon_position = (194,73)


player1_benched_pokemon_positions = [
    (84, 509),
    (181, 509),
    (278, 509),
    (375, 509),
    (472, 509)
]

player2_benched_pokemon_positions = [
    (84, 6),
    (181, 6),
    (278, 6),
    (375, 6),
    (472, 6)
]

player1_prize_card_positions = [
    (21, 300),
    (70, 300),
    (21, 366),
    (70, 366),
    (21, 432),
    (70, 432)
]


player2_prize_card_positions = [
    (526, 83),
    (575, 83),
    (526, 149),
    (575, 149),
    (526, 215),
    (575, 215)
]

text2a=" Hand: 6 "
text2b=" Discard: 0 "
text2c=" Deck: 48 "

text1a=" Hand: 6 "
text1b=" Discard: 77 "
text1c=" Deck: 48 "

text2_positions=[
(5, 71),
(5, 111),
(5, 151)
]


text1_positions=[
(452, 322),
(452, 362),
(452, 402),
]

fillcolor=(255,255,255,191)


text_surface_2a = font.render(text2a, True,(0,0,0))
text_surface_2b = font.render(text2b, True,(0,0,0))
text_surface_2c = font.render(text2c, True,(0,0,0))

text_surface_1a = font.render(text1a, True,(0,0,0))
text_surface_1b = font.render(text1b, True,(0,0,0))
text_surface_1c = font.render(text1c, True,(0,0,0))

text_bg=pygame.Surface((184,35),pygame.SRCALPHA)

text_bg.fill(fillcolor)

#screen.fill((255, 255, 255))

def render():

    screen.blit(background,(0,0))
    screen.blit(large_pkmn_card1, player1_active_pokemon_position)
    screen.blit(large_pkmn_card2, player2_active_pokemon_position)
    for position in player1_benched_pokemon_positions:
        screen.blit(med_pkmn_card1, position)
    for position in player2_benched_pokemon_positions:
        screen.blit(med_pkmn_card2, position)
    for position in player1_prize_card_positions:
        screen.blit(card_back, position)
    for position in player2_prize_card_positions:
        screen.blit(card_back, position)

    screen.blit(text_bg, (text2_positions[0][0],text2_positions[0][1]+2)) 
    screen.blit(text_bg, (text2_positions[1][0],text2_positions[1][1]+2)) 
    screen.blit(text_bg, (text2_positions[2][0],text2_positions[2][1]+2)) 
    screen.blit(text_bg, (text1_positions[0][0],text1_positions[0][1]+2)) 
    screen.blit(text_bg, (text1_positions[1][0],text1_positions[1][1]+2)) 
    screen.blit(text_bg, (text1_positions[2][0],text1_positions[2][1]+2)) 


    screen.blit(text_surface_2a, text2_positions[0]) 
    screen.blit(text_surface_2b, text2_positions[1]) 
    screen.blit(text_surface_2c, text2_positions[2]) 
    screen.blit(text_surface_1a, text1_positions[0]) 
    screen.blit(text_surface_1b, text1_positions[1]) 
    screen.blit(text_surface_1c, text1_positions[2]) 
    
    screen.blit(stadium_card,(264,256))

    pygame.display.update()
    clock.tick(60)


if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()