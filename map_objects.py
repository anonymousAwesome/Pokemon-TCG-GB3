import pygame

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
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"It's a chalkboard.\nIt just says \"butts lol\". :/"],{"greyscale":inner_context.player_data.currently_greyscale})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()
        
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
