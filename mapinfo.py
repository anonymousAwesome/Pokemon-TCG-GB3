import pygame
import os
import ui
import characters
import random_name
import numpy as np

def reload_map(inner_context,replacement_map):
    inner_context.map_holder.__init__(replacement_map)
    inner_context.temp_exit_list.__init__(inner_context.map_holder,inner_context.player_character)
    inner_context.current_npcs.reset(replacement_map)
    inner_context.collision_manager.__init__(inner_context.map_holder.current_map.bg_image, inner_context.player_character, inner_context.screen, inner_context.current_dialogue, inner_context.event_manager, inner_context.map_input_lock, obstacles=inner_context.map_holder.current_map.obstacles, npcs=inner_context.current_npcs)



class GlitchEffect:
    def __init__(self):
        self.time_remaining=0

    def process_glitch(self,screen):
        screen_copy = screen.copy()
        array = pygame.surfarray.array3d(screen_copy)
        transposed = np.transpose(array, (1, 0, 2))[:array.shape[0], :array.shape[1]]
        result = np.clip(array[:transposed.shape[0], :transposed.shape[1]] - transposed, 0, 255).astype(np.uint8)
        glitch_surface = pygame.surfarray.make_surface(result)
        screen.blit(glitch_surface, (0, 0))    
        

    def pulse_glitch(self, screen):
        if self.time_remaining>=80 or 30>=self.time_remaining>=0:
            self.process_glitch(screen)
        self.time_remaining -= 1

    def steady_glitch(self,screen):
        self.process_glitch(screen)
        self.time_remaining -= 1

    def start_glitch(self,duration=150):
        self.time_remaining=duration
        
    def check_time_remaining(self):
        return self.time_remaining

glitch_effect=GlitchEffect()

class EmptyEvent():
    def __init__(self,loops_left):
        self.loops_left=loops_left
    def decrement_loops(self):
        self.loops_left-=1
    def check_still_looping(self):
        return self.loops_left
    
empty_event=EmptyEvent(0)


def dialogue_facing(player_character,npc):
    if player_character.facing_direction=="down":
        npc.sprite.manual_direction_change("up")
    if player_character.facing_direction=="up":
        npc.sprite.manual_direction_change("down")
    if player_character.facing_direction=="left":
        npc.sprite.manual_direction_change("right")
    if player_character.facing_direction=="right":
        npc.sprite.manual_direction_change("left")

"""
----------------------------------
objects
----------------------------------
"""

class BaseMapObjectClass:
    def __init__(self):
        self.def_rect()

class MasonCenterTree(BaseMapObjectClass):

    def def_rect(self):
        self.rect=pygame.Rect(64, 704, 64, 128)

    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"It's a tree.\nI'm not sure what you expected."])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class MasonCenterPC(BaseMapObjectClass):

    def def_rect(self):
        self.rect=pygame.Rect(64, 64, 64, 64)

    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(inner_context.phase_handler.set_game_phase,["paddlewar"])


class MasonCenterBlackboard(BaseMapObjectClass):

    def def_rect(self):
        self.rect=pygame.Rect(448, 0, 64, 64)

    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"It's a chalkboard.\nIt just says \"butts lol\". :/"])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

"""
----------------------------------
exits
----------------------------------
"""


class BaseExitClass:
    def __init__(self):
        pass

    def step_on(self, inner_context):
        inner_context.player_character.rect.x = self.new_x
        inner_context.player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            inner_context.player_character.facing_direction = self.facing_direction
            inner_context.player_character.map_exit_change_facing()
        reload_map(inner_context,self.replacement_map)

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
        self.facing_direction="down"
    

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




"""
----------------------------------
Overworld Club entrances
----------------------------------
"""

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
        reload_map(inner_context,self.replacement_map)

class MasonsLabOverworldEntrance(BaseOverworldClubClass):
    def __init__(self):
        #super().__init__()
        self.rect=pygame.Rect(64, 448, 64, 64)
        self.new_x=448
        self.new_y=832
        self.replacement_map=MasonCenter
        self.facing_direction="up"
        self.club_text="Mason Lab"

"""
----------------------------------
NPCs
----------------------------------
"""

class BaseNpcClass():
    def __init__(self):
        pass

class DrMason(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,3)
        self.sprite=characters.NPC(448,192, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

    def interact_object(self,inner_context):

        inner_context.event_manager.add_event(glitch_effect.start_glitch,[300])
        inner_context.event_manager.add_event(glitch_effect.steady_glitch,[inner_context.screen],persistent_condition=glitch_effect.check_time_remaining)


    '''
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"Welcome! I'm Dr. Mason, with a PhD in Pokemon cardology!"])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()
'''
"""
----------------------------------
map rooms
----------------------------------
"""

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
            MasonCenterTree,
            MasonCenterBlackboard,
            MasonCenterPC,
            ]
              
        self.step_triggers=[
            MasonCenterLeftExit1,
            MasonCenterLeftExit2,
            MasonCenterBottomExit,
            ]

        self.npcs=[
            DrMason,
            ]

'''
        self.step_triggers=[
            
            (pygame.Rect(0, 320+64, 64, 64),{"mapname":"mason_left","x":768,"y":704+64}), 
            (pygame.Rect(832, 320, 64, 64),{"mapname":"mason_right","x":64,"y":320}),
            (pygame.Rect(832, 320+64, 64, 64),{"mapname":"mason_right","x":64,"y":320+64}),
            ]
'''


class TestMap:
    def __init__(self):
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "trading post.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
        ]

        self.step_triggers=[]




class TradingPostCharity(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock,player_character):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock,player_character)
        self.rect=pygame.Rect(256, 256, 64, 64)
        self.photo_location=os.path.join("assets", "duellists", "Charity.png")

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"Welcome to the trading post.\nWould you like to make a trade?"],{"name_text":"Charity","photo_location":self.photo_location})
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
        self.event_manager.add_event(self.map_input_lock.unlock)
        self.map_input_lock.lock()


class TradingPostJumboSteve(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock,player_character):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock,player_character)
        self.rect=pygame.Rect(64, 384, 64, 64)
        self.photo_location=os.path.join("assets", "duellists", "jumbo steve.png")

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"My deck uses only the largest cards! Jumbo promotional cards are where it's at! Game balance? Never heard of it!"],{"name_text":"Jumbo Steve","photo_location":self.photo_location})
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
        self.event_manager.add_event(self.map_input_lock.unlock)
        self.map_input_lock.lock()




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
        TradingPostJumboSteve,
        TradingPostCharity,
        ]





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
        MasonsLabOverworldEntrance
        ]

        self.interact_self_triggers=[
        MasonsLabOverworldEntrance
        ]

        self.npcs=[]

        '''        
        self.step_triggers=[
            (pygame.Rect(64, 448, 64, 64),"Mason's Lab"),
            (pygame.Rect(192, 448, 64, 64),"Fighting Club"),
            (pygame.Rect(128, 320, 64, 64),"Lightning Club"),
            ],'''
'''


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
        (pygame.Rect(0, 320, 64, 64),{"mapname":"mason_center","x":768,"y":320}),
        (pygame.Rect(0, 320+64, 64, 64),{"mapname":"mason_center","x":768,"y":320+64}),
        ],
    }

airport_neo_side={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "airport neo side.png")),
    "obstacles":[],
    }

airport_tcg_side={
    "bg_image": pygame.image.load(os.path.join("assets", "maps", "airport tcg side.png")),
    "obstacles":[],
    }

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
    }

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
    }
    
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
    }

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
    }


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
    }


'''
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
