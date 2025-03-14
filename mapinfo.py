import pygame
import os
import ui
import characters


"""
----------------------------------
objects
----------------------------------
"""


class BaseMapObjectClass:
    def __init__(self,screen,current_dialogue,event_manager,map_input_lock):
        self.screen=screen
        self.current_dialogue=current_dialogue
        self.event_manager=event_manager
        self.map_input_lock=map_input_lock

class MasonCenterTree(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock)
        self.rect=pygame.Rect(64, 704, 64, 128)

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"It's a tree.\nI'm not sure what you expected."])
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
        self.map_input_lock.lock()


class MasonCenterBlackboard(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock)
        self.rect=pygame.Rect(448, 0, 64, 64)

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"It's a chalkboard.\nIt just says \"butts lol\". :/"])
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
        self.map_input_lock.lock()

"""
----------------------------------
exits
----------------------------------
"""


class BaseExitClass:
    def __init__(self):
        pass

    def step_on(self, map_holder, screen,overworld_event_manager,collision_manager,player_character,temp_exit_list,current_npcs):
        player_character.rect.x = self.new_x
        player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            player_character.facing_direction = self.facing_direction
            player_character.map_exit_change_facing()
        map_holder.__init__(self.replacement_map)
        collision_manager.__init__(map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles)
        temp_exit_list.__init__(map_holder,player_character)
        current_npcs.reset(self.replacement_map)

class MasonCenterLeftExit1(BaseExitClass):
    def __init__(self):
        #super().__init__(player)
        self.new_x = 768
        self.new_y = 704
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320, 64, 64)

class MasonCenterLeftExit2(BaseExitClass):
    def __init__(self):
        #super().__init__(player)
        self.new_x = 768
        self.new_y = 704+64
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320+64, 64, 64)


class MasonCenterBottomExit(BaseExitClass):
    def __init__(self):
        #super().__init__(player)
        self.new_x = 1*64
        self.new_y = 7*64
        self.replacement_map = TcgIsland
        self.rect=pygame.Rect(448, 896, 128, 64)
        self.facing_direction="down"

class MasonLeftExit1(BaseExitClass):
    def __init__(self):
        #super().__init__(player)
        self.new_x = 64
        self.new_y = 320
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(832, 704, 64, 64)

class MasonLeftExit2(BaseExitClass):
    def __init__(self):
        #super().__init__(player)
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
    def step_on(self, map_holder, screen,overworld_event_manager,collision_manager,player_character,temp_exit_list,current_npcs):
        ui.club_name_render(screen,self.club_text)
    def interact_self(self, map_holder, screen,overworld_event_manager,collision_manager,player_character,temp_exit_list,current_npcs):
        player_character.rect.x = self.new_x
        player_character.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            player_character.facing_direction = self.facing_direction
            player_character.map_exit_change_facing()
        map_holder.__init__(self.replacement_map)
        collision_manager.__init__(map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles)
        temp_exit_list.__init__(map_holder,player_character)
        current_npcs.reset(self.replacement_map)

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

class DrMason(characters.Character):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,3)
        self.sprite=characters.NPC(448,192, self.loaded_sprites)


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
            MasonCenterBlackboard
            ]
              
        self.step_triggers=[
            MasonCenterLeftExit1,
            MasonCenterLeftExit2,
            MasonCenterBottomExit
            ]

        self.npcs=[
            DrMason
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

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock)
        self.rect=pygame.Rect(256, 256, 64, 64)
        self.photo_location=os.path.join("assets", "duellists", "Charity.png")

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"Welcome to the trading post.\nWould you like to make a trade?"],{"name_text":"Charity","photo_location":self.photo_location})
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
        self.map_input_lock.lock()


class TradingPostJumboSteve(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager,map_input_lock):
        super().__init__(screen,current_dialogue,event_manager,map_input_lock)
        self.rect=pygame.Rect(64, 384, 64, 64)
        self.photo_location=os.path.join("assets", "duellists", "jumbo steve.png")

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"My deck uses only the largest cards! Jumbo promotional cards are where it's at! Game balance? Never heard of it!"],{"name_text":"Jumbo Steve","photo_location":self.photo_location})
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)
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
