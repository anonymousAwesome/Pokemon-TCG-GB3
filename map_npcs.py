import characters
import map_helpers

class BaseNpcClass():
    def __init__(self):
        pass

class DrMason(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,0)
        self.sprite=characters.NPC(448,192, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,2,0)
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"Welcome! I'm Dr. Mason, with a PhD in Pokemon cardology!"],{"name_text":"Dr. Mason", "profile_image":self.portrait})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class Sam(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(2*64,7*64, self.loaded_sprites,"right")
        self.rect=self.sprite.rect
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,0,1)
        self.text="""So... I was supposed to teach you how to play the Pokemon Trading Card Game, but, er, apparently the tutorial wasn't worth the effort to code. Sorry.
Maybe you could play one of prequels first? Last I heard, the first game was available on the Switch."""
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Sam","profile_image":self.portrait})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()    

class LabTechCenterTopRight(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(11*64,4*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="""In the original game, if you put all your energy into a spare deck and then talked to me, I would give you 10 of each basic energy.
Imagine that: 60 energy cards, instantly!
On a related note, I'm out of energy cards. Gave them all away. Probably shouldn't have done that."""
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()
        
class LabTechCenterBottomRight(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(10*64,10*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="Thanks to recent card science breakthroughs, the same card can now be placed in multiple decks at the same time! I realize this breaks the laws of physics, but it's so convenient!"
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class LabTechCenterBottomLeft(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(5*64,11*64, self.loaded_sprites,"right")
        self.rect=self.sprite.rect
        self.text1="One of the other technicians called me an NPC with only two lines."
        self.text2="What did he mean by that?"
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text1],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text2],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class LabTechRightTop(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(3*64,4*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="This room holds the auto deck system, but it broke. Nobody ever used it, though, so it was months before anybody noticed."
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class LabTechRightBottom(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(5*64,8*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="Dr. Mason? I thought he already left for his vacation."
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class LabTechLeftTop(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(1*64,2*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text1="Shhh! Don't tell anyone; I'm taking a break."
        self.text2="The air has a pungent odor..."
    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text1],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text2])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()


class LabTechLeftBottom(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(10*64,7*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="""We finally got these numbered ping-pong tables installed! Too bad the paddles are still on back-order.
Well, at least I can still practice on the cutting-edge computer simulation in the other room."""

    
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

