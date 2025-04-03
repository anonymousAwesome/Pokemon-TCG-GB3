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