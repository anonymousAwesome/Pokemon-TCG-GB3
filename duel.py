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

'''to-do: rework the font area to be more like the other screen: full
opacity, blue outlines, pokemon-emerald font.
Also, possibly swap the prizes and font areas to make space for the 
effects on the left side of the Pokemon. Maybe. Needs workshopping.
Maybe shrink the Pokemon images and add a border around each one showing
its type.'''


'''
to-do: check for invalid result when using a stored duel result
that's neither win nor lose.'''

import os
import pygame
import key_mappings


class Context:
    def __init__(self,screen,phase_handler):
        self.screen=screen
        self.phase_handler=phase_handler
        
        self.font = pygame.font.Font(os.path.join("assets","pokemon-emerald.otf"), 40)
        self.large_pkmn_card_dims=252,176
        self.med_pkmn_card_dims=84,59
        self.small_pkmn_card_dims=55,38
        self.stadium_dims=112,61
        self.card_back_dims=44,61

        pkmn_card1=pygame.image.load("./assets/voltorb.jpg").convert()
        pkmn_card2=pygame.image.load("./assets/ponyta.jpg").convert()
        stadium_card=pygame.image.load("./assets/energy stadium.jpg").convert()
        card_back=pygame.image.load("./assets/cardback.jpg").convert()
        self.large_pkmn_card1=pygame.transform.scale(pkmn_card1, self.large_pkmn_card_dims)
        self.large_pkmn_card2=pygame.transform.scale(pkmn_card2, self.large_pkmn_card_dims)
        self.stadium_card=pygame.transform.scale(stadium_card, self.stadium_dims)
        self.med_pkmn_card1=pygame.transform.scale(pkmn_card1, self.med_pkmn_card_dims)
        self.med_pkmn_card2=pygame.transform.scale(pkmn_card2, self.med_pkmn_card_dims)
        self.small_pkmn_card1=pygame.transform.scale(pkmn_card1, self.small_pkmn_card_dims)
        self.small_pkmn_card2=pygame.transform.scale(pkmn_card2, self.small_pkmn_card_dims)
        self.card_back=pygame.transform.scale(card_back, self.card_back_dims)

        background=pygame.image.load("./assets/duel backgrounds/city skyline.jpg").convert()
        '''
        note: image was exported from png to jpg at ~50% quality. A little blurring,
        but that is good and bad, depending on the location. And it cut the file 
        size in half.
        '''

        self.background=pygame.transform.scale(background, (640,576))

        self.player1_active_pokemon_position = (194,324)
        self.player2_active_pokemon_position = (194,73)


        self.player1_benched_pokemon_positions = [
            (84, 509),
            (181, 509),
            (278, 509),
            (375, 509),
            (472, 509)
        ]

        self.player2_benched_pokemon_positions = [
            (84, 6),
            (181, 6),
            (278, 6),
            (375, 6),
            (472, 6)
        ]

        self.player1_prize_card_positions = [
            (21, 300),
            (70, 300),
            (21, 366),
            (70, 366),
            (21, 432),
            (70, 432)
        ]


        self.player2_prize_card_positions = [
            (526, 83),
            (575, 83),
            (526, 149),
            (575, 149),
            (526, 215),
            (575, 215)
        ]

        self.text2a=" Hand: 6 "
        self.text2b=" Discard: 0 "
        self.text2c=" Deck: 54 "

        self.text1a=" Hand: 6 "
        self.text1b=" Discard: 0 "
        self.text1c=" Deck: 54 "

        self.text2_positions=[
        (5, 71),
        (5, 111),
        (5, 151)
        ]


        self.text1_positions=[
        (452, 322),
        (452, 362),
        (452, 402),
        ]

        fillcolor=(255,255,255,191)


        self.text_surface_2a = self.font.render(self.text2a, True,(0,0,0))
        self.text_surface_2b = self.font.render(self.text2b, True,(0,0,0))
        self.text_surface_2c = self.font.render(self.text2c, True,(0,0,0))

        self.text_surface_1a = self.font.render(self.text1a, True,(0,0,0))
        self.text_surface_1b = self.font.render(self.text1b, True,(0,0,0))
        self.text_surface_1c = self.font.render(self.text1c, True,(0,0,0))

        self.text_bg=pygame.Surface((184,35),pygame.SRCALPHA)

        self.text_bg.fill(fillcolor)

        #screen.fill((255, 255, 255))

    def update(self,eventlist):

        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.large_pkmn_card1, self.player1_active_pokemon_position)
        self.screen.blit(self.large_pkmn_card2, self.player2_active_pokemon_position)
        for position in self.player1_benched_pokemon_positions:
            self.screen.blit(self.med_pkmn_card1, position)
        for position in self.player2_benched_pokemon_positions:
            self.screen.blit(self.med_pkmn_card2, position)
        for position in self.player1_prize_card_positions:
            self.screen.blit(self.card_back, position)
        for position in self.player2_prize_card_positions:
            self.screen.blit(self.card_back, position)

        self.screen.blit(self.text_bg, (self.text2_positions[0][0],self.text2_positions[0][1]+2)) 
        self.screen.blit(self.text_bg, (self.text2_positions[1][0],self.text2_positions[1][1]+2)) 
        self.screen.blit(self.text_bg, (self.text2_positions[2][0],self.text2_positions[2][1]+2)) 
        self.screen.blit(self.text_bg, (self.text1_positions[0][0],self.text1_positions[0][1]+2)) 
        self.screen.blit(self.text_bg, (self.text1_positions[1][0],self.text1_positions[1][1]+2)) 
        self.screen.blit(self.text_bg, (self.text1_positions[2][0],self.text1_positions[2][1]+2)) 


        self.screen.blit(self.text_surface_2a, self.text2_positions[0]) 
        self.screen.blit(self.text_surface_2b, self.text2_positions[1]) 
        self.screen.blit(self.text_surface_2c, self.text2_positions[2]) 
        self.screen.blit(self.text_surface_1a, self.text1_positions[0]) 
        self.screen.blit(self.text_surface_1b, self.text1_positions[1]) 
        self.screen.blit(self.text_surface_1c, self.text1_positions[2]) 
        
        self.screen.blit(self.stadium_card,(264,256))


        keys = pygame.key.get_pressed()
        if keys[key_mappings.cancel_key]:
            self.phase_handler.won_last_duel=True
            self.phase_handler.set_game_phase("overworld")
