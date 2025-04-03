import pygame
import os
import ui
import map_helpers
import map_objects
import map_npcs
import animation

glitch_effect=map_helpers.GlitchEffect()
empty_event=map_helpers.EmptyEvent(0)



class BaseExitClass:
    def __init__(self):
        pass

    def step_on(self, inner_context):
        inner_context.player_character.rect.x = self.new_x
        inner_context.player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            inner_context.player_character.facing_direction = self.facing_direction
            inner_context.player_character.map_exit_change_facing()
        map_helpers.reload_map(inner_context,self.replacement_map)



class BaseOverworldClubClass:
    def __init__(self):
        pass
    def step_on(self, inner_context):
        ui.club_name_render(inner_context.screen,self.club_text)
    def interact_self(self, inner_context):
        inner_context.player_character.rect.x = self.new_x
        inner_context.player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            inner_context.player_character.facing_direction = self.facing_direction
            inner_context.player_character.map_exit_change_facing()
        map_helpers.reload_map(inner_context,self.replacement_map)
        



class TestMap:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "FF entrance.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
        ]

        self.step_triggers=[]


class TcgIsland:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "tcg island.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))
        self.obstacles=[
            pygame.Rect(0, 0, 640, 64),
            pygame.Rect(0, 64, 64, 512),
            pygame.Rect(64, 512, 576, 64),
            pygame.Rect(64, 64, 320, 64),
            pygame.Rect(576, 384, 64, 128),
            pygame.Rect(576, 64, 64, 64),
            pygame.Rect(64, 192, 64, 64),
            pygame.Rect(64, 384, 64, 64)]
        self.step_triggers=[
        MasonsLabOverworldEntrance,
        FightingClubOverworldEntrance,
        FireClubOverworldEntrance,
        GrassClubOverworldEntrance,
        LightningClubOverworldEntrance,
        PsychicClubOverworldEntrance,
        RockClubOverworldEntrance,
        ScienceClubOverworldEntrance,
        WaterClubOverworldEntrance,
        AirportOverworldEntrance,
        ChallengeHallOverworldEntrance,
        IshiharasHouseOverworldEntrance,
        PokemonDomeOverworldEntrance,
        ]
        self.interact_self_triggers=self.step_triggers
        self.npcs=[]


class MasonsLabOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):
        self.rect=pygame.Rect(64, 448, 64, 64)
        self.new_x=448
        self.new_y=832
        self.replacement_map=MasonCenter
        self.facing_direction="up"
        self.club_text="Mason Lab"

class FightingClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):
        self.rect=pygame.Rect(192, 448, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=FightingClub
        self.facing_direction="up"
        self.club_text="Fighting Club"

class FireClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(448, 64, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=FireClub
        self.facing_direction="up"
        self.club_text="Fire Club"
    
class GrassClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):
        self.rect=pygame.Rect(512, 256, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=GrassClub
        self.facing_direction="up"
        self.club_text="Grass Club"
    
class LightningClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(128, 320, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=LightningClub
        self.facing_direction="up"
        self.club_text="Lightning Club"
    
class PsychicClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(384, 192, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=PsychicClub
        self.facing_direction="up"
        self.club_text="Psychic Club"
    
class RockClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(64, 256, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=RockClub
        self.facing_direction="up"
        self.club_text="Rock Club"
    
class ScienceClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(512, 128, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=ScienceClub
        self.facing_direction="up"
        self.club_text="Science Club"
    
class WaterClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(448, 384, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=WaterClub
        self.facing_direction="up"
        self.club_text="Water Club"
    
class AirportOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(320, 448, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=Airport
        self.facing_direction="up"
        self.club_text="Airport"
    
class ChallengeHallOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(256, 128, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=ChallengeHall
        self.facing_direction="up"
        self.club_text="Challenge Hall"
    
class IshiharasHouseOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(64, 128, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=IshiharasHouse
        self.facing_direction="up"
        self.club_text="Ishihara's House"
    
class PokemonDomeOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(256, 256, 64, 64)
        self.new_x=0
        self.new_y=0
        self.replacement_map=PokemonDome
        self.facing_direction="up"
        self.club_text="Pokemon Dome"
    



class MasonCenter:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "mason center.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
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
        ]
       
        
        self.interact_object_triggers=[
            map_objects.MasonCenterTree,
            map_objects.MasonCenterBlackboard,
            map_objects.MasonCenterPC,
            map_objects.MasonCenterBooks1,
            map_objects.MasonCenterBooks2,
            ]
              
        self.step_triggers=[
            MasonCenterLeftExit1,
            MasonCenterLeftExit2,
            MasonCenterBottomExit,
            MasonCenterRightExit1,
            MasonCenterRightExit2
            ]

        self.npcs=[
            map_npcs.DrMason,
            ]


class MasonCenterLeftExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 768
        self.new_y = 704
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320, 64, 64)

class MasonCenterLeftExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 768
        self.new_y = 704+64
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320+64, 64, 64)

class MasonCenterBottomExit(BaseExitClass):
    def __init__(self):
        self.new_x = 1*64
        self.new_y = 7*64
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(448, 896, 128, 64)
    
class MasonCenterRightExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 1*64
        self.new_y = 5*64
        self.replacement_map = MasonRight
        self.rect=pygame.Rect(832, 320, 64, 64)

class MasonCenterRightExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 1*64
        self.new_y = 6*64
        self.replacement_map = MasonRight
        self.rect=pygame.Rect(832, 384, 64, 64)


class MasonLeft:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "mason left.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
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
            ]

        self.npcs=[]

        self.step_triggers=[
            MasonLeftExit1,
            MasonLeftExit2
            ]

class MasonLeftExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 320
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(832, 704, 64, 64)

class MasonLeftExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 320+64
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(832, 704+64, 64, 64)



class MasonRight:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "mason right.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))
        
        self.obstacles=[
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
            ]
        self.step_triggers=[
            MasonRightExit1,
            MasonRightExit2
            ]
    
class MasonRightExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 12*64
        self.new_y = 5*64
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(0*64,5*64, 64, 64)

class MasonRightExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 12*64
        self.new_y = 6*64
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(0*64,6*64, 64, 64)




class FightingClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "fighting club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class FireClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "fire club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class GrassClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "grass club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class LightningClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "lightning club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class PsychicClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "psychic club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class RockClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "rock club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class ScienceClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "science club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class WaterClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "water club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class Airport:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "airport.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]


class ChallengeHall:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "challenge hall.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]



class IshiharasHouse:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "ishiharas house.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]


class PokemonDome:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "pokemon dome.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            ]
        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ]

        self.npcs=[
            ]




class TradingPost:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "trading post.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 768),
            pygame.Rect(576, 0, 64, 768),
            pygame.Rect(64, 256, 512, 64),
            pygame.Rect(64, 64, 512, 64),
            pygame.Rect(64, 128, 512, 64),
            pygame.Rect(64, 192, 512, 64),
            pygame.Rect(64, 0, 512, 64),
            pygame.Rect(64, 704, 512, 64),
            pygame.Rect(64, 384, 64, 320),
            pygame.Rect(512, 384, 64, 320),
            pygame.Rect(448, 576, 64, 128),
            pygame.Rect(128, 576, 64, 128),
        ]


        self.step_triggers=[]

        self.interact_object_triggers=[
        map_objects.TradingPostJumboSteve,
        map_objects.TradingPostCharity,
        ]




