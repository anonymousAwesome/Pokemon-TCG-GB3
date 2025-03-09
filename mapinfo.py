import pygame
import os
import ui


"""
----------------------------------
objects
----------------------------------
"""


class BaseMapObjectClass:
    def __init__(self,screen):
        self.screen=screen



class MasonCenterTree(BaseMapObjectClass):

    def __init__(self,screen,current_dialogue,event_manager):
        super().__init__(screen)
        self.current_dialogue=current_dialogue
        self.rect=pygame.Rect(64, 704, 64, 128)
        self.event_manager=event_manager

    def interact_object(self,event_list):
        self.event_manager.add_event(self.current_dialogue.__init__,[self.screen,"It's a tree.\nI'm not sure what you expected."])
        self.event_manager.add_event(self.current_dialogue.render,[event_list],persistent_condition=self.current_dialogue.check_remaining_text)


'''
class MasonCenterBlackboard(BaseMapObjectClass):

    def __init__(self,screen,passed):
        super().__init__(screen)
        self.passed=passed
        self.args=["It's a chalkboard.\nIt just says \"butts lol\". :/"]
        self.rect=pygame.Rect(448, 0, 64, 64)
        self.definition_type="class object"
   ''' 

"""
----------------------------------
exits
----------------------------------
"""


class BaseExitClass:
    def __init__(self, player):
        self.player = player

    def step_on_exit(self, map_holder, screen,overworld_event_manager,collision_manager,player_character,temp_exit_list):
        self.player.rect.x = self.new_x
        self.player.rect.y = self.new_y
        if hasattr(self, "facing_direction"):
            self.player.facing_direction = self.facing_direction
            self.player.map_exit_change_facing()
        map_holder.__init__(self.replacement_map, screen)
        overworld_event_manager.add_event(collision_manager.__init__,[map_holder.current_map.bg_image,player_character,map_holder.current_map.obstacles])
        overworld_event_manager.add_event(temp_exit_list.__init__,[map_holder,player_character])



class MasonCenterLeftExit1(BaseExitClass):
    def __init__(self, player):
        super().__init__(player)
        self.new_x = 768
        self.new_y = 704
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320, 64, 64)

class MasonCenterLeftExit2(BaseExitClass):
    def __init__(self, player):
        super().__init__(player)
        self.new_x = 768
        self.new_y = 704+64
        self.replacement_map = MasonLeft
        self.rect = pygame.Rect(0, 320+64, 64, 64)


class MasonCenterBottomExit(BaseExitClass):
    def __init__(self,player):
        super().__init__(player)
        self.new_x = 1*64
        self.new_y = 7*64
        self.replacement_map = MasonLeft
        self.rect=pygame.Rect(448, 896, 128, 64)
        self.facing_direction="up"




class MasonLeftExit1(BaseExitClass):
    def __init__(self,player):
        super().__init__(player)
        self.new_x = 64
        self.new_y = 320
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(832, 704, 64, 64)

class MasonLeftExit2(BaseExitClass):
    def __init__(self,player):
        super().__init__(player)
        self.new_x = 64
        self.new_y = 320+64
        self.replacement_map = MasonCenter
        self.rect=pygame.Rect(832, 704+64, 64, 64)




"""
----------------------------------
NPCs
----------------------------------
"""

class ProfMason:
    def __init__(self,screen):
        pass



"""
----------------------------------
map rooms
----------------------------------
"""

class MasonCenter:
    def __init__(self,screen):
        self.screen=screen
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
       
        
        self.interact_object=[
            MasonCenterTree,
            ]
      
        '''
        self.interact_object=[
            MasonCenterTree,
            MasonCenterBlackboard
            ]'''
        
        self.step_exit_triggers=[
            MasonCenterLeftExit1,
            MasonCenterLeftExit2,
            MasonCenterBottomExit
            ]

'''
        self.step_exit_triggers=[
            
            (pygame.Rect(0, 320+64, 64, 64),{"mapname":"mason_left","x":768,"y":704+64}), 
            (pygame.Rect(832, 320, 64, 64),{"mapname":"mason_right","x":64,"y":320}),
            (pygame.Rect(832, 320+64, 64, 64),{"mapname":"mason_right","x":64,"y":320+64}),
            ]
'''


class TestMap:
    def __init__(self,screen):
        self.screen=screen
        self.bg_image=pygame.image.load(os.path.join("assets", "maps", "trading post.png"))
        self.bg_image=pygame.transform.scale(self.bg_image, (self.bg_image.get_width() * 4, self.bg_image.get_height() * 4))

        self.obstacles=[
        ]

        self.step_exit_triggers=[]


class MasonLeft:
    def __init__(self,screen):
        self.screen=screen
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

        self.step_exit_triggers=[
            MasonLeftExit1,
            MasonLeftExit2
            ]
'''
    "step exit triggers":[
        (pygame.Rect(832, 704, 64, 64),{"mapname":"mason_center","x":64,"y":320}),
        (pygame.Rect(832, 768, 64, 64),{"mapname":"mason_center","x":64,"y":320+64}),
        ],'''

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
    "step exit triggers":[
        (pygame.Rect(0, 320, 64, 64),{"mapname":"mason_center","x":768,"y":320}),
        (pygame.Rect(0, 320+64, 64, 64),{"mapname":"mason_center","x":768,"y":320+64}),
        ],
    }

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
    "interact self exit triggers":[
        (pygame.Rect(64, 448, 64, 64),{"mapname":"mason_center","x":448,"y":832,"direction":"up"})
        ],
    "tcg club names":[
        (pygame.Rect(64, 448, 64, 64),"Mason's Lab"),
        (pygame.Rect(192, 448, 64, 64),"Fighting Club"),
        (pygame.Rect(128, 320, 64, 64),"Lightning Club"),
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
