import pygame
import ui
import character

screen = character.screen
pygame.display.set_caption("Overworld Exploration")
clock = pygame.time.Clock()

#mapname="flying"
#mapname="neo continent"
#mapname="neo stadium"
#mapname="tcg island"
#mapname="ex card interior"
#mapname="ex card lobby"
#mapname="imakuni"
mapname="fighting club"
#mapname="fhqwhgads"

if mapname=="ex card interior":
    bg_image = pygame.image.load("./assets/maps/ex cards interior.png")
    obstacles=[
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
    pygame.Rect(128, 448, 192, 64),
]
    player_starting_location=(6*64,10*64)

elif mapname=="ex card lobby":
    bg_image = pygame.image.load("./assets/maps/ex cards lobby.png")
    obstacles=[
    pygame.Rect(0, 0, 64, 576),
    pygame.Rect(640, 0, 64, 576),
    pygame.Rect(64, 0, 192, 64),
    pygame.Rect(64, 448, 192, 64),
    pygame.Rect(64, 512, 192, 64),
    pygame.Rect(448, 448, 192, 64),
    pygame.Rect(448, 512, 192, 64),
    pygame.Rect(448, 0, 192, 64),
    pygame.Rect(192, 64, 64, 128),
    pygame.Rect(448, 64, 64, 128),
]
    player_starting_location=(5*64,7*64)
    
elif mapname=="flying":
    bg_image = pygame.image.load("./assets/maps/flying club.png")
    #flying club
    obstacles=[
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
        pygame.Rect(704, 320, 64, 128),
    ]
    player_starting_location=(6*64,13*64)

elif mapname =="neo continent":
    bg_image = pygame.image.load("./assets/maps/neo continent.png")
    obstacles=[
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
        pygame.Rect(512, 448, 64, 64),
    ]

    player_starting_location=(64,128)

elif mapname=="neo stadium":
    bg_image = pygame.image.load("./assets/maps/neo stadium.png")
    obstacles=[
    pygame.Rect(0, 0, 64, 1024),
    pygame.Rect(832, 0, 64, 1024),
    pygame.Rect(64, 0, 768, 64),
    pygame.Rect(512, 640, 320, 64),
    pygame.Rect(512, 896, 320, 64),
    pygame.Rect(512, 960, 320, 64),
    pygame.Rect(64, 960, 320, 64),
    pygame.Rect(64, 896, 320, 64),
    pygame.Rect(64, 640, 320, 64),
]

    player_starting_location=(6*64,14*64)

elif mapname=="tcg island":
    bg_image = pygame.image.load("./assets/maps/tcg island.png")
    obstacles=[
        pygame.Rect(0, 0, 640, 64),
        pygame.Rect(0, 64, 64, 512),
        pygame.Rect(256, 512, 384, 64),
        pygame.Rect(64, 64, 320, 64),
        pygame.Rect(576, 384, 64, 128),
        pygame.Rect(576, 64, 64, 64),
        pygame.Rect(64, 192, 64, 64),
        pygame.Rect(64, 384, 64, 64),
    ]



    player_starting_location=(1*64,7*64)

elif mapname=="imakuni":
    bg_image = pygame.image.load("./assets/maps/wandering imakuni.png")
    obstacles=[]
    player_starting_location=(6*64,6*64)

elif mapname=="fighting club":
    bg_image = pygame.image.load("./assets/maps/fighting club.png")
    obstacles=[]
    player_starting_location=(5*64,10*64)


else:
    bg_image = pygame.image.load("./assets/maps/map load error.png")
    obstacles=[]
    player_starting_location=(0*64,0*64)


bg_width, bg_height = bg_image.get_width(), bg_image.get_height()
bg_image = pygame.transform.scale(bg_image, (bg_width * 4, bg_height * 4))

player_image=pygame.image.load('./assets/player_image.png').convert_alpha()
player=character.Player(player_starting_location[0],player_starting_location[1],character.sprites,bg_image)



def render():

    keys = pygame.key.get_pressed()    

    player.update(keys,obstacles)
    
    camera_x_offset = -max(0, min(bg_width * 4 - 640, (player.rect.centerx - 320)))
    camera_y_offset = -max(0, min(bg_height * 4 - 576, (player.rect.centery - 288)))
    screen.blit(bg_image, (camera_x_offset, camera_y_offset))
    #for ob in obstacles:
    #    pygame.draw.rect(screen, (255,255,0), ob.move(camera_x_offset, camera_y_offset))
    player.draw(screen, camera_x_offset, camera_y_offset)

    
    test_dialogue=ui.Dialogue(screen,"Pete Abrams",
    '/media/brendanj/Shared Partition/programming/pokemon tcg monte carlo/pokemon_tcg_fangame/assets/duellists/pete abrams 3.png',
    '''Test1
Test2
Aaaaa aaaa aaaaa aaa aaa aaa 4bbb 3ccc 2ddd 1e 0fffff .''',
    "/media/brendanj/Shared Partition/programming/pokemon tcg monte carlo/pokemon_tcg_fangame/assets/pokemon-emerald.otf")
    
    test_dialogue.render()
    

    pygame.display.flip()
    clock.tick(60)

if __name__=="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()