import pygame
import os

'''I'm really not happy having to hard-code each exit, but the alternative
involved a circular dependency that I couldn't figure out how to break.'''

def exit_to_tcg_island(player_character,current_map):
    current_map.change_map(tcg_island)
    player_character.facing_direction="down"
    player_character.rect.x=tcg_island["player_starting_location"][0]
    player_character.rect.y=tcg_island["player_starting_location"][1]

def exit_to_mason_left_from_center1(player_character,current_map):
    current_map.change_map(mason_left)
    player_character.rect.x=mason_left["player_starting_location"][0]
    player_character.rect.y=mason_left["player_starting_location"][1]

def exit_to_mason_left_from_center2(player_character,current_map):
    current_map.change_map(mason_left)
    player_character.rect.x=mason_left["player_starting_location"][0]
    player_character.rect.y=mason_left["player_starting_location"][1]+64

def exit_to_mason_center_from_left1(player_character,current_map):
    current_map.change_map(mason_center)
    player_character.rect.x=64
    player_character.rect.y=320

def exit_to_mason_center_from_left2(player_character,current_map):
    current_map.change_map(mason_center)
    player_character.rect.x=64
    player_character.rect.y=384

def exit_to_mason_right_from_center1(player_character,current_map):
    current_map.change_map(mason_right)
    player_character.rect.x=mason_right["player_starting_location"][0]
    player_character.rect.y=mason_right["player_starting_location"][1]

def exit_to_mason_right_from_center2(player_character,current_map):
    current_map.change_map(mason_right)
    player_character.rect.x=mason_right["player_starting_location"][0]
    player_character.rect.y=mason_right["player_starting_location"][1]+64

def exit_to_mason_center_from_right1(player_character,current_map):
    current_map.change_map(mason_center)
    player_character.rect.x=768
    player_character.rect.y=320

def exit_to_mason_center_from_right2(player_character,current_map):
    current_map.change_map(mason_center)
    player_character.rect.x=768
    player_character.rect.y=384

def enter_mason_center_from_overworld(player_character,current_map):
    current_map.change_map(mason_center)
    player_character.rect.x=448
    player_character.rect.y=832
    player_character.facing_direction="up"


mason_center={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "mason center.png")),
    "obstacles":[
        pygame.Rect(0, 0, 896, 64),
        pygame.Rect(0, 448, 64, 512),
        pygame.Rect(832, 448, 64, 512),
        pygame.Rect(64, 832, 384, 64),
        pygame.Rect(64, 896, 384, 64),
        pygame.Rect(0, 64, 320, 64),
        pygame.Rect(576, 64, 320, 64),
        pygame.Rect(576, 832, 256, 64),
        pygame.Rect(576, 896, 256, 64),
        pygame.Rect(640, 448, 192, 64),
        pygame.Rect(0, 128, 64, 192),
        pygame.Rect(832, 128, 64, 192),
        pygame.Rect(192, 448, 128, 64),
        pygame.Rect(192, 512, 128, 64),
        pygame.Rect(64, 704, 64, 128),
    ],
    "step triggers":[
        (pygame.Rect(448, 896, 128, 64), exit_to_tcg_island),
        (pygame.Rect(0, 320, 64, 64),exit_to_mason_left_from_center1),
        (pygame.Rect(0, 320+64, 64, 64),exit_to_mason_left_from_center2),
        (pygame.Rect(832, 320, 64, 64),exit_to_mason_right_from_center1),
        (pygame.Rect(832, 320+64, 64, 64),exit_to_mason_right_from_center2),
        
        ],
    "player_starting_location":(448,832)}


mason_left={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "mason left.png")),
    "obstacles":[
        pygame.Rect(0, 0, 64, 1024),
        pygame.Rect(64, 0, 832, 64),
        pygame.Rect(64, 960, 832, 64),
        pygame.Rect(64, 896, 832, 64),
        pygame.Rect(832, 64, 64, 640),
        pygame.Rect(192, 192, 384, 64),
        pygame.Rect(192, 256, 384, 64),
        pygame.Rect(192, 512, 384, 64),
        pygame.Rect(192, 576, 384, 64),
        pygame.Rect(832, 832, 64, 64),
    ],
    "step triggers":[
        (pygame.Rect(832, 704, 64, 64),exit_to_mason_center_from_left1),
        (pygame.Rect(832, 768, 64, 64),exit_to_mason_center_from_left2),
        ],
    "player_starting_location":(768, 704)}

mason_right={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "mason right.png")),
    "obstacles":[
        pygame.Rect(704, 0, 64, 960),
        pygame.Rect(0, 0, 704, 64),
        pygame.Rect(0, 64, 704, 64),
        pygame.Rect(0, 896, 704, 64),
        pygame.Rect(0, 832, 704, 64),
        pygame.Rect(0, 448, 64, 384),
        pygame.Rect(448, 256, 256, 64),
        pygame.Rect(448, 320, 256, 64),
        pygame.Rect(448, 512, 256, 64),
        pygame.Rect(448, 576, 256, 64),
        pygame.Rect(0, 128, 64, 192),
        pygame.Rect(64, 512, 128, 64),
        pygame.Rect(64, 576, 128, 64),
    ],
    "step triggers":[
        (pygame.Rect(0, 320, 64, 64),exit_to_mason_center_from_right1),
        (pygame.Rect(0, 320+64, 64, 64),exit_to_mason_center_from_right2),
        ],
    "player_starting_location":(64,320)}

tcg_island={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "tcg island.png")),
    "obstacles":[
        pygame.Rect(0, 0, 640, 64),
        pygame.Rect(0, 64, 64, 512),
        pygame.Rect(64, 512, 576, 64),
        pygame.Rect(64, 64, 320, 64),
        pygame.Rect(576, 384, 64, 128),
        pygame.Rect(576, 64, 64, 64),
        pygame.Rect(64, 192, 64, 64),
        pygame.Rect(64, 384, 64, 64)],
    "interact self triggers":[
        (pygame.Rect(64, 448, 64, 64),enter_mason_center_from_overworld),
        ],
    "tcg club names":[
        (pygame.Rect(64, 448, 64, 64),"Mason's Lab"),
        (pygame.Rect(192, 448, 64, 64),"Fighting Club"),
        (pygame.Rect(128, 320, 64, 64),"Lightning Club"),
        ],
    "player_starting_location":(1*64,7*64)}



airport_neo_side={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "airport neo side.png")),
    "obstacles":[],
    "player_starting_location":(2*64,2*64)}

airport_tcg_side={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "airport tcg side.png")),
    "obstacles":[],
    "player_starting_location":(2*64,2*64)}

ex_card_interior={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "ex cards interior.png")),
    "obstacles":[
        pygame.Rect(0, 0, 832, 64),
        pygame.Rect(0, 64, 832, 64),
        pygame.Rect(0, 128, 64, 640),
        pygame.Rect(768, 128, 64, 640),
        pygame.Rect(64, 128, 64, 320),
        pygame.Rect(704, 128, 64, 320),
        pygame.Rect(64, 704, 256, 64),
        pygame.Rect(64, 640, 256, 64),
        pygame.Rect(512, 640, 256, 64),
        pygame.Rect(512, 704, 256, 64),
        pygame.Rect(320, 192, 192, 64),
        pygame.Rect(320, 256, 192, 64),
        pygame.Rect(512, 448, 192, 64),
        pygame.Rect(128, 448, 192, 64)],
    "player_starting_location":(6*64,10*64)}

ex_card_lobby={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "ex cards lobby.png")),
    "obstacles":[
        pygame.Rect(0, 0, 64, 576),
        pygame.Rect(640, 0, 64, 576),
        pygame.Rect(64, 0, 192, 64),
        pygame.Rect(64, 448, 192, 64),
        pygame.Rect(64, 512, 192, 64),
        pygame.Rect(448, 448, 192, 64),
        pygame.Rect(448, 512, 192, 64),
        pygame.Rect(448, 0, 192, 64),
        pygame.Rect(192, 64, 64, 128),
        pygame.Rect(448, 64, 64, 128)],
    "player_starting_location":(5*64,7*64)}
    
flying={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "flying club.png")),
    "obstacles":[
        pygame.Rect(0, 0, 64, 960),
        pygame.Rect(832, 0, 64, 960),
        pygame.Rect(64, 0, 768, 64),
        pygame.Rect(512, 896, 320, 64),
        pygame.Rect(512, 832, 320, 64),
        pygame.Rect(64, 832, 320, 64),
        pygame.Rect(64, 896, 320, 64),
        pygame.Rect(256, 192, 64, 256),
        pygame.Rect(640, 320, 64, 256),
        pygame.Rect(64, 640, 192, 64),
        pygame.Rect(64, 704, 192, 64),
        pygame.Rect(64, 768, 128, 64),
        pygame.Rect(192, 192, 64, 128),
        pygame.Rect(320, 192, 64, 128),
        pygame.Rect(576, 320, 64, 128),
        pygame.Rect(704, 320, 64, 128)],
    "player_starting_location":(6*64,13*64)}

neo_continent={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "neo continent.png")),
    "obstacles":[
        pygame.Rect(0, 576, 896, 64),
        pygame.Rect(0, 0, 64, 576),
        pygame.Rect(768, 0, 64, 576),
        pygame.Rect(832, 0, 64, 576),
        pygame.Rect(256, 320, 448, 64),
        pygame.Rect(64, 192, 64, 384),
        pygame.Rect(128, 192, 64, 384),
        pygame.Rect(512, 256, 256, 64),
        pygame.Rect(512, 192, 256, 64),
        pygame.Rect(512, 512, 256, 64),
        pygame.Rect(256, 448, 192, 64),
        pygame.Rect(512, 64, 192, 64),
        pygame.Rect(256, 64, 192, 64),
        pygame.Rect(256, 128, 192, 64),
        pygame.Rect(256, 192, 192, 64),
        pygame.Rect(64, 64, 128, 64),
        pygame.Rect(64, 0, 128, 64),
        pygame.Rect(256, 384, 128, 64),
        pygame.Rect(512, 448, 64, 64)],
    "player_starting_location":(64,128)}


neo_stadium={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "neo stadium.png")),
    "obstacles":[
        pygame.Rect(0, 0, 64, 1024),
        pygame.Rect(832, 0, 64, 1024),
        pygame.Rect(64, 0, 768, 64),
        pygame.Rect(512, 896, 320, 64),
        pygame.Rect(512, 960, 320, 64),
        pygame.Rect(64, 960, 320, 64),
        pygame.Rect(64, 896, 320, 64)],
    "player_starting_location":(6*64,14*64)}


'''
elif mapname=="imakuni":
    bg_image = pygame.image.load(os.path.join("assets", "maps", "wandering imakuni.png"))
    obstacles=[]
    player_starting_location=(6*64,6*64)

elif mapname=="fighting":
    bg_image = pygame.image.load(os.path.join("assets", "maps", "fighting club.png"))
    obstacles=[]
    player_starting_location=(5*64,10*64)

elif mapname=="normal":
    bg_image = pygame.image.load(os.path.join("assets", "maps", "normal club.png"))
    obstacles=[]
    player_starting_location=(4*64,12*64)

elif mapname=="ground":
    bg_image = pygame.image.load(os.path.join("assets", "maps", "ground club.png"))
    obstacles=[]
    player_starting_location=(4*64,12*64)

elif mapname=="temp":
    bg_image = pygame.image.load(os.path.join("assets", "maps", "dark club.png"))
    obstacles=[]
    player_starting_location=(4*64,4*64)

else:
    bg_image = pygame.image.load(os.path.join("assets", "maps", "map load error.png"))
    obstacles=[]
    player_starting_location=(0*64,0*64)
'''
