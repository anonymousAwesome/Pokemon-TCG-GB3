import characters

class BaseNpcClass():
    def __init__(self):
        pass

class DrMason(BaseNpcClass):
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,18)
        self.sprite=characters.NPC(448,192, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
    

    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(inner_context.player_character.toggle_visibility)

    '''
    def interact_object(self,inner_context):
        inner_context.event_manager.add_event(dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,"Welcome! I'm Dr. Mason, with a PhD in Pokemon cardology!"])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()
    '''