import pygame

ex_card_interior={
    "bg_image": pygame.image.load("./assets/maps/ex cards interior.png"),
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
    "bg_image": pygame.image.load("./assets/maps/ex cards lobby.png"),
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
    "bg_image": pygame.image.load("./assets/maps/flying club.png"),
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
    "bg_image": pygame.image.load("./assets/maps/neo continent.png"),
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
    "bg_image": pygame.image.load("./assets/maps/neo stadium.png"),
    "obstacles":[
        pygame.Rect(0, 0, 64, 1024),
        pygame.Rect(832, 0, 64, 1024),
        pygame.Rect(64, 0, 768, 64),
        pygame.Rect(512, 896, 320, 64),
        pygame.Rect(512, 960, 320, 64),
        pygame.Rect(64, 960, 320, 64),
        pygame.Rect(64, 896, 320, 64)],
    "player_starting_location":(6*64,14*64)}

tcg_island={
    "bg_image": pygame.image.load("./assets/maps/tcg island.png"),
    "obstacles":[
        pygame.Rect(0, 0, 640, 64),
        pygame.Rect(0, 64, 64, 512),
        pygame.Rect(64, 512, 576, 64),
        pygame.Rect(64, 64, 320, 64),
        pygame.Rect(576, 384, 64, 128),
        pygame.Rect(576, 64, 64, 64),
        pygame.Rect(64, 192, 64, 64),
        pygame.Rect(64, 384, 64, 64)],
    "player_starting_location":(1*64,7*64)}

'''
elif mapname=="imakuni":
    bg_image = pygame.image.load("./assets/maps/wandering imakuni.png")
    obstacles=[]
    player_starting_location=(6*64,6*64)

elif mapname=="fighting":
    bg_image = pygame.image.load("./assets/maps/fighting club.png")
    obstacles=[]
    player_starting_location=(5*64,10*64)

elif mapname=="normal":
    bg_image = pygame.image.load("./assets/maps/normal club.png")
    obstacles=[]
    player_starting_location=(4*64,12*64)

elif mapname=="ground":
    bg_image = pygame.image.load("./assets/maps/ground club.png")
    obstacles=[]
    player_starting_location=(4*64,12*64)

elif mapname=="temp":
    bg_image = pygame.image.load("./assets/maps/dark club.png")
    obstacles=[]
    player_starting_location=(4*64,4*64)

else:
    bg_image = pygame.image.load("./assets/maps/map load error.png")
    obstacles=[]
    player_starting_location=(0*64,0*64)
'''
