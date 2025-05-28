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
    
    def step_on(self, inner_context):
        inner_context.player_character.rect.x = self.new_x
        inner_context.player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            inner_context.player_character.facing_direction = self.facing_direction
            inner_context.player_character.map_exit_change_facing()
        map_helpers.reload_map(inner_context,self.replacement_map)



class BaseOverworldClubClass:
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
        self.obstacles=[]
        self.step_triggers=[
            OpeningCutsceneTrigger,
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


class OpeningCutsceneTrigger:
    def __init__(self):
        self.rect=pygame.Rect(-2, -2, 1, 1) #disabled
        
        #self.rect=pygame.Rect(0, 0, 64, 64)

    def step_on(self, inner_context):

        text1=f"""{inner_context.player_data.player_name} is just crazy about card collecting and duelling! They faced each club leader on TCG Island and defeated the Grand Masters, obtaining the Legendary Pokemon cards. But then, disaster struck! Team Great Rocket stole everybody's cards and took over TCG Island! After duelling their way through the ranks, {inner_context.player_data.player_name} defeated their leader, King Villicci, causing him to have a change of heart and give up his evil ways. Peace returned to TCG Island."""
        
        text2="""Until one day..."""

        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text1])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text2])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,CutsceneFfEntrance])
        inner_context.event_manager.add_event(inner_context.disable_prevent_step_trigger)
        inner_context.prevent_step_trigger = True
        inner_context.map_input_lock.lock()

class CutsceneFfEntrance:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "FF entrance.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
        ]

        self.npcs=[
        map_npcs.OpeningCutsceneMalinda,
        map_npcs.OpeningCutsceneGrass,
        map_npcs.OpeningCutsceneLightning,
        map_npcs.OpeningCutsceneFire,
        map_npcs.OpeningCutsceneWater,
        map_npcs.OpeningCutsceneGround,
        map_npcs.OpeningCutscenePoison,
        map_npcs.OpeningCutsceneFlying,
        map_npcs.OpeningCutscenePsychic,
        map_npcs.OpeningCutsceneNormal
        ]

        self.step_triggers=[
        FfEntranceCutsceneTrigger
        ]


class FfEntranceCutsceneTrigger:
    def __init__(self):
        self.rect=pygame.Rect(0, 0, 64, 64)

    def step_on(self, inner_context):
        temp=map_helpers.FFCutsceneHelpers(inner_context)
        inner_context.event_manager.add_event(temp.group_move,[inner_context,3],persistent_condition=temp.check_bottom,condition_kwargs={"y_coord":960})

        inner_context.event_manager.add_event(empty_event.__init__,[60])
        inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)

        inner_context.event_manager.add_event(temp.group_move,[inner_context,8],persistent_condition=temp.check_bottom,condition_kwargs={"y_coord":1600})
        
        inner_context.event_manager.add_event(empty_event.__init__,[60])
        inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)
        
        inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,CutsceneWaterClub])
        
        inner_context.prevent_step_trigger = True
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        #inner_context.event_manager.add_event(inner_context.disable_prevent_step_trigger)
        inner_context.map_input_lock.lock()
        
class CutsceneWaterClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "water club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
        ]


        self.npcs=[
        ]

        self.step_triggers=[
        ]





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
        self.new_x=320
        self.new_y=640
        self.replacement_map=FightingClub
        self.facing_direction="up"
        self.club_text="Fighting Club"

class FireClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(448, 64, 64, 64)
        self.new_x=384
        self.new_y=896
        self.replacement_map=FireClub
        self.facing_direction="up"
        self.club_text="Fire Club"
    
class GrassClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):
        self.rect=pygame.Rect(512, 256, 64, 64)
        self.new_x=384
        self.new_y=832
        self.replacement_map=GrassClub
        self.facing_direction="up"
        self.club_text="Grass Club"
    
class LightningClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(128, 320, 64, 64)
        self.new_x=384
        self.new_y=896
        self.replacement_map=LightningClub
        self.facing_direction="up"
        self.club_text="Lightning Club"
    
class PsychicClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(384, 192, 64, 64)
        self.new_x=384
        self.new_y=768
        self.replacement_map=PsychicClub
        self.facing_direction="up"
        self.club_text="Psychic Club"
    
class RockClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(64, 256, 64, 64)
        self.new_x=384
        self.new_y=832
        self.replacement_map=RockClub
        self.facing_direction="up"
        self.club_text="Rock Club"
    
class ScienceClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(512, 128, 64, 64)
        self.new_x=384
        self.new_y=896
        self.replacement_map=ScienceClub
        self.facing_direction="up"
        self.club_text="Science Club"
    
class WaterClubOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(448, 384, 64, 64)
        self.new_x=384
        self.new_y=896
        self.replacement_map=WaterClub
        self.facing_direction="up"
        self.club_text="Water Club"
    
class AirportOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(320, 448, 64, 64)
        self.new_x=320
        self.new_y=704
        self.replacement_map=AirportTcg
        self.facing_direction="up"
        self.club_text="Airport"
    
class ChallengeHallOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(256, 128, 64, 64)
        self.new_x=384
        self.new_y=832
        self.replacement_map=ChallengeHall
        self.facing_direction="up"
        self.club_text="Challenge Hall"
    
class IshiharasHouseOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(64, 128, 64, 64)
        self.new_x=256
        self.new_y=704
        self.replacement_map=IshiharasHouse
        self.facing_direction="up"
        self.club_text="Ishihara's House"
    
class PokemonDomeOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):    
        self.rect=pygame.Rect(256, 256, 64, 64)
        self.new_x=448
        self.new_y=448
        self.replacement_map=PokemonDomeEntrance
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
            map_npcs.LabTechCenterTopRight,
            map_npcs.Sam,
            map_npcs.LabTechCenterBottomRight,
            map_npcs.LabTechCenterBottomLeft,
            ]


class MasonCenterLeftExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 704-64
        self.new_y = 640
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320, 64, 64)

class MasonCenterLeftExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 704-64
        self.new_y = 640+64
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
            pygame.Rect(0, 0, 64, 960),
            pygame.Rect(64, 0, 704, 64),
            pygame.Rect(64, 896, 704, 64),
            pygame.Rect(64, 832, 704, 64),
            pygame.Rect(704, 64, 64, 576),
            pygame.Rect(192, 512, 384, 64),
            pygame.Rect(192, 576, 384, 64),
            pygame.Rect(192, 256, 384, 64),
            pygame.Rect(192, 192, 384, 64),
            pygame.Rect(704, 768, 64, 64),
            ]

        self.npcs=[
        map_npcs.LabTechLeftTop,
        map_npcs.LabTechLeftBottom,
        ]

        self.step_triggers=[
            MasonLeftExit1,
            MasonLeftExit2
            ]

class MasonLeftExit1(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 320
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(704, 640, 64, 64)

class MasonLeftExit2(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 320+64
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(704, 640+64, 64, 64)



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
        
        self.npcs=[
            map_npcs.LabTechRightBottom,
            map_npcs.Aaron,
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
            pygame.Rect(0, 0, 768, 64),
            pygame.Rect(0, 64, 64, 704),
            pygame.Rect(704, 64, 64, 704),
            pygame.Rect(64, 640, 256, 64),
            pygame.Rect(64, 704, 256, 64),
            pygame.Rect(448, 640, 256, 64),
            pygame.Rect(448, 704, 256, 64),
            pygame.Rect(64, 64, 192, 64),
            pygame.Rect(512, 64, 192, 64),
            pygame.Rect(640, 320, 64, 192),
            pygame.Rect(64, 320, 64, 128),
            pygame.Rect(64, 128, 64, 128),
            pygame.Rect(640, 128, 64, 128),
            ]

        
        self.interact_object_triggers=[
            map_objects.FightingClubSign
            ]
              
        self.step_triggers=[
            FightingClubExit,
            ]

        self.npcs=[
            map_npcs.Tyler,
            map_npcs.Norton,
            map_npcs.Helena,
            map_npcs.Brad,
            ]


class FightingClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 3*64
        self.new_y = 7*64
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(320, 640+64, 128, 64)



class FireClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "fire club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 1024),
            pygame.Rect(832, 0, 64, 1024),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(64, 960, 320, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(512, 960, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(576, 448, 64, 320),
            pygame.Rect(256, 448, 64, 320),
            pygame.Rect(576, 64, 64, 256),
            pygame.Rect(256, 64, 64, 256),
            pygame.Rect(320, 64, 64, 192),
            pygame.Rect(512, 64, 64, 192),
            pygame.Rect(640, 128, 64, 128),
            pygame.Rect(192, 128, 64, 128),
            ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            FireClubExit
            ]

        self.npcs=[
            ]

class FireClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 448
        self.new_y = 64
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 960, 128, 64)




class GrassClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "grass club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 960),
            pygame.Rect(832, 0, 64, 960),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(256, 448, 384, 64),
            pygame.Rect(256, 320, 384, 64),
            pygame.Rect(256, 384, 384, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(64, 832, 320, 64),
            pygame.Rect(512, 832, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(64, 64, 256, 64),
            pygame.Rect(576, 64, 256, 64),
            pygame.Rect(128, 192, 256, 64),
            pygame.Rect(512, 192, 256, 64),
            pygame.Rect(512, 640, 256, 64),
            pygame.Rect(128, 640, 256, 64),
            pygame.Rect(128, 256, 64, 128),
            pygame.Rect(704, 256, 64, 128),
            pygame.Rect(704, 512, 64, 128),
            pygame.Rect(128, 512, 64, 128),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            GrassClubExit
            ]

        self.npcs=[
            ]


class GrassClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 512
        self.new_y = 256
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 896, 128, 64)



class LightningClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "lightning club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 1024),
            pygame.Rect(832, 0, 64, 1024),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(256, 64, 384, 64),
            pygame.Rect(64, 960, 320, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(512, 960, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(256, 448, 64, 320),
            pygame.Rect(576, 448, 64, 320),
            pygame.Rect(704, 128, 64, 64),
            pygame.Rect(128, 128, 64, 64),
        ]


        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            LightningClubExit
            ]

        self.npcs=[
            ]

class LightningClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 128
        self.new_y = 320
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 960, 128, 64)



class PsychicClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "psychic club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 896, 64),
            pygame.Rect(0, 64, 64, 832),
            pygame.Rect(832, 64, 64, 832),
            pygame.Rect(64, 768, 320, 64),
            pygame.Rect(64, 832, 320, 64),
            pygame.Rect(512, 832, 320, 64),
            pygame.Rect(512, 768, 320, 64),
            pygame.Rect(512, 512, 64, 128),
            pygame.Rect(704, 448, 64, 128),
            pygame.Rect(704, 192, 64, 128),
            pygame.Rect(512, 128, 64, 128),
            pygame.Rect(320, 128, 64, 128),
            pygame.Rect(128, 192, 64, 128),
            pygame.Rect(128, 448, 64, 128),
            pygame.Rect(320, 512, 64, 128),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            PsychicClubExit
            ]

        self.npcs=[
            ]

class PsychicClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 384
        self.new_y = 192
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 832, 128, 64)



class RockClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "rock club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 960),
            pygame.Rect(832, 0, 64, 960),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(64, 832, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(512, 832, 320, 64),
            pygame.Rect(640, 448, 128, 64),
            pygame.Rect(576, 128, 128, 64),
            pygame.Rect(128, 640, 128, 64),
            pygame.Rect(256, 64, 64, 128),
            pygame.Rect(640, 704, 64, 64),
            pygame.Rect(640, 384, 64, 64),
            pygame.Rect(576, 64, 64, 64),
            pygame.Rect(128, 320, 64, 64),
            pygame.Rect(192, 576, 64, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            RockClubExit
            ]

        self.npcs=[
            ]


class RockClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 256
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 896, 128, 64)



class ScienceClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "science club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 1024),
            pygame.Rect(832, 0, 64, 1024),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(256, 64, 576, 64),
            pygame.Rect(448, 640, 384, 64),
            pygame.Rect(448, 576, 384, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(64, 960, 320, 64),
            pygame.Rect(512, 960, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(512, 128, 64, 320),
            pygame.Rect(64, 256, 64, 256),
            pygame.Rect(128, 256, 64, 256),
            pygame.Rect(128, 576, 192, 64),
            pygame.Rect(128, 640, 192, 64),
            pygame.Rect(384, 384, 128, 64),
            pygame.Rect(64, 64, 128, 64),
            pygame.Rect(192, 384, 64, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ScienceClubExit
            ]

        self.npcs=[
            ]

class ScienceClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 512
        self.new_y = 128
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 960, 128, 64)



class WaterClub:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "water club.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 1024),
            pygame.Rect(832, 0, 64, 1024),
            pygame.Rect(64, 0, 768, 64),
            pygame.Rect(64, 256, 512, 64),
            pygame.Rect(64, 192, 512, 64),
            pygame.Rect(64, 128, 512, 64),
            pygame.Rect(64, 64, 512, 64),
            pygame.Rect(64, 448, 448, 64),
            pygame.Rect(64, 384, 448, 64),
            pygame.Rect(64, 320, 448, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(64, 960, 320, 64),
            pygame.Rect(512, 960, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(64, 704, 64, 192),
            pygame.Rect(128, 704, 64, 192),
            pygame.Rect(768, 256, 64, 192),
            pygame.Rect(704, 256, 64, 192),
            pygame.Rect(768, 704, 64, 128),
            pygame.Rect(640, 64, 64, 64),
            pygame.Rect(768, 576, 64, 64),
            pygame.Rect(768, 128, 64, 64),
            pygame.Rect(192, 576, 64, 64),
            pygame.Rect(320, 640, 64, 64),
        ]


            
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            WaterClubExit
            ]

        self.npcs=[
            map_npcs.Sara,
            map_npcs.Joshua,
            map_npcs.Amy,
            map_npcs.Amanda,
            ]

class WaterClubExit(BaseExitClass):
    def __init__(self):
        self.new_x = 448
        self.new_y = 384
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 960, 128, 64)



class AirportTcg:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "airport tcg side.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 832),
            pygame.Rect(64, 0, 704, 64),
            pygame.Rect(320, 256, 448, 64),
            pygame.Rect(448, 704, 320, 64),
            pygame.Rect(448, 768, 320, 64),
            pygame.Rect(64, 768, 256, 64),
            pygame.Rect(64, 704, 256, 64),
            pygame.Rect(576, 320, 192, 64),
            pygame.Rect(576, 512, 192, 64),
            pygame.Rect(704, 64, 64, 192),
            pygame.Rect(320, 64, 64, 192),
            pygame.Rect(704, 576, 64, 128),
            pygame.Rect(192, 64, 64, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            AirportTcgBottomExit,
            AirportTcgRightExit
            ]

        self.npcs=[
            ]

class AirportTcgBottomExit(BaseExitClass):
    def __init__(self):
        self.new_x = 320
        self.new_y = 448
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(320, 768, 128, 64)

class AirportTcgRightExit(BaseExitClass):
    def __init__(self):
        self.new_x = 0
        self.new_y = 0
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(704, 384, 64, 128)



class ChallengeHall:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "challenge hall.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 960),
            pygame.Rect(832, 0, 64, 960),
            pygame.Rect(64, 0, 704, 64),
            pygame.Rect(256, 64, 384, 64),
            pygame.Rect(64, 896, 320, 64),
            pygame.Rect(64, 832, 320, 64),
            pygame.Rect(512, 832, 320, 64),
            pygame.Rect(512, 896, 320, 64),
            pygame.Rect(128, 64, 64, 320),
            pygame.Rect(704, 64, 64, 320),
            pygame.Rect(384, 192, 64, 192),
            pygame.Rect(448, 192, 64, 192),
            pygame.Rect(384, 512, 128, 64),
            pygame.Rect(192, 384, 64, 64),
            pygame.Rect(320, 448, 64, 64),
            pygame.Rect(512, 448, 64, 64),
            pygame.Rect(640, 384, 64, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            ChallengeHallBottomExit,
            ChallengeHallTopExit
            ]

        self.npcs=[
            ]

class ChallengeHallBottomExit(BaseExitClass):
    def __init__(self):
        self.new_x = 256
        self.new_y = 128
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(384, 896, 128, 64)


class ChallengeHallTopExit(BaseExitClass):
    def __init__(self):
        self.new_x = 256
        self.new_y = 128
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(768, 0, 64, 64)



class IshiharasHouse:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "ishiharas house.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 64, 832),
            pygame.Rect(576, 0, 64, 832),
            pygame.Rect(64, 64, 512, 64),
            pygame.Rect(64, 0, 512, 64),
            pygame.Rect(512, 320, 64, 256),
            pygame.Rect(64, 768, 192, 64),
            pygame.Rect(64, 704, 192, 64),
            pygame.Rect(64, 512, 192, 64),
            pygame.Rect(64, 448, 192, 64),
            pygame.Rect(384, 768, 192, 64),
            pygame.Rect(384, 704, 192, 64),
            pygame.Rect(384, 448, 128, 64),
            pygame.Rect(384, 512, 128, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            IshiharasHouseExit
            ]

        self.npcs=[
            ]

class IshiharasHouseExit(BaseExitClass):
    def __init__(self):
        self.new_x = 64
        self.new_y = 128
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(256, 768, 128, 64)


class PokemonDomeEntrance:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "pokemon dome entrance.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 704, 64),
            pygame.Rect(960, 0, 64, 576),
            pygame.Rect(0, 64, 64, 512),
            pygame.Rect(64, 448, 384, 64),
            pygame.Rect(64, 512, 384, 64),
            pygame.Rect(576, 448, 384, 64),
            pygame.Rect(576, 512, 384, 64),
            pygame.Rect(64, 256, 192, 64),
            pygame.Rect(64, 64, 192, 64),
            pygame.Rect(832, 0, 128, 64),
        ]

        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            PokemonDomeEntranceBottomExit,
            PokemonDomeEntranceTopLeftExit,
            PokemonDomeEntranceTopRightExit
            ]

        self.npcs=[
            ]


class PokemonDomeEntranceBottomExit(BaseExitClass):
    def __init__(self):
        self.new_x = 256
        self.new_y = 256
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(448, 512, 128, 64)

class PokemonDomeEntranceTopLeftExit(BaseExitClass):
    def __init__(self):
        self.new_x = 448
        self.new_y = 896
        self.replacement_map = PokemonDomeInterior
        self.rect=pygame.Rect(704, 0, 64, 64)


class PokemonDomeEntranceTopRightExit(BaseExitClass):
    def __init__(self):
        self.new_x = 448+64
        self.new_y = 896
        self.replacement_map = PokemonDomeInterior
        self.rect=pygame.Rect(704+64, 0, 64, 64)



class PokemonDomeInterior:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "pokemon dome interior.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
            pygame.Rect(0, 0, 1024, 64),
            pygame.Rect(960, 64, 64, 960),
            pygame.Rect(0, 64, 64, 960),
            pygame.Rect(896, 192, 64, 448),
            pygame.Rect(64, 192, 64, 448),
            pygame.Rect(64, 960, 384, 64),
            pygame.Rect(64, 896, 384, 64),
            pygame.Rect(576, 960, 384, 64),
            pygame.Rect(576, 896, 384, 64),
            pygame.Rect(576, 192, 320, 64),
            pygame.Rect(128, 192, 320, 64),
            pygame.Rect(640, 640, 192, 64),
            pygame.Rect(192, 640, 192, 64),
            pygame.Rect(256, 320, 64, 192),
            pygame.Rect(320, 320, 64, 192),
            pygame.Rect(640, 320, 64, 192),
            pygame.Rect(704, 320, 64, 192),
            pygame.Rect(832, 576, 64, 64),
            pygame.Rect(576, 704, 64, 64),
            pygame.Rect(384, 704, 64, 64),
            pygame.Rect(128, 576, 64, 64),
        ]


        
        self.interact_object_triggers=[
            ]
              
        self.step_triggers=[
            PokemonDomeInteriorExitLeft,
            PokemonDomeInteriorExitRight
            ]

        self.npcs=[
            ]


class PokemonDomeInteriorExitLeft(BaseExitClass):
    def __init__(self):
        self.new_x = 704
        self.new_y = 64
        self.replacement_map = PokemonDomeEntrance
        self.rect=pygame.Rect(448, 960, 64, 64)

class PokemonDomeInteriorExitRight(BaseExitClass):
    def __init__(self):
        self.new_x = 704+64
        self.new_y = 64
        self.replacement_map = PokemonDomeEntrance
        self.rect=pygame.Rect(448+64, 960, 64, 64)



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


