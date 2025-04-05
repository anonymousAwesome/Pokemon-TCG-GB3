import characters
import map_helpers
import pygame



vertical_modifier=-192

class OpeningCutsceneMalinda():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,1)
        self.sprite=characters.NPC(288,128+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect


class OpeningCutsceneGrass():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,2)
        self.sprite=characters.NPC(256,0+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneLightning():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,3)
        self.sprite=characters.NPC(320,0+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneFire():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,4)
        self.sprite=characters.NPC(256,-64+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneWater():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,5)
        self.sprite=characters.NPC(320,-64+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneGround():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,6)
        self.sprite=characters.NPC(256,-128+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutscenePoison():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,7)
        self.sprite=characters.NPC(320,-128+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneFlying():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,8)
        self.sprite=characters.NPC(256,-192+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutscenePsychic():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,9)
        self.sprite=characters.NPC(320,-192+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect

class OpeningCutsceneNormal():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,10)
        self.sprite=characters.NPC(256,-832+vertical_modifier, self.loaded_sprites,"down")
        self.rect=self.sprite.rect


#Mason's Lab


    

class DrMason():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_gb3,0)
        self.sprite=characters.NPC(448,192, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,2,0)
        self.text="Welcome! I'm Dr. Mason, with a PhD in Pokemon cardology!"

    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Dr. Mason",profile_image=self.portrait,duel=False)
        

class Sam():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(2*64,7*64, self.loaded_sprites,"right")
        self.rect=self.sprite.rect
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,0,1)
        self.text="""So... I was supposed to teach you how to play the Pokemon Trading Card Game, but, er, apparently the tutorial wasn't worth the effort to code. Sorry.
Maybe you could play one of the prequels first? Last I heard, the first game was available on the Switch."""
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Sam",profile_image=self.portrait,duel=False)
        
class LabTechCenterTopRight():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(11*64,4*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="""In the original game, if you put all your energy into spare decks and then talked to me, I would give you 10 of each basic energy.
That's 60 energy cards, instantly!
This is not to be confused with Aaron, who gave you a booster of 10 energy cards when you beat him. My way was much faster.
On a related note, I'm out of energy cards. Gave them all away. Probably shouldn't have done that."""
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Lab Tech",duel=False)
        
class LabTechCenterBottomRight():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(10*64,10*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="Thanks to recent card science breakthroughs, the same card can now be placed in multiple decks at the same time! I realize this breaks the laws of physics, but it's so convenient!"
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Lab Tech",duel=False)

class LabTechCenterBottomLeft():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(5*64,11*64, self.loaded_sprites,"right")
        self.rect=self.sprite.rect
        text1="One of the other technicians called me an NPC with only two lines."
        text2="What did he mean by that?"
        self.text=[text1,text2]
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Lab Tech",duel=False)

class Aaron():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(3*64,4*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="This room holds the auto deck system, but it broke. Nobody ever used it, though, so it was months before anybody noticed."
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,1,1)
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Aaron",profile_image=self.portrait,duel=False)

class LabTechRightBottom():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(5*64,8*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="Dr. Mason? I thought he already left for his vacation."
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Lab Tech",duel=False)

class LabTechLeftTop():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(1*64,2*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text1="Shhh! Don't tell anyone; I'm taking a break."
        self.text2="The air has a pungent odor..."
    
    def interact_object(self,inner_context):
        '''Note that this one doesn't use the helper function, because I 
        need the first box to have his name and the second one to 
        not have his name.'''
        inner_context.event_manager.add_event(map_helpers.dialogue_facing,[inner_context.player_character,self])
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text1],{"name_text":"Lab Tech"})
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,self.text2])
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
        inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
        inner_context.map_input_lock.lock()

class LabTechLeftBottom():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,4)
        self.sprite=characters.NPC(10*64,7*64, self.loaded_sprites,"left")
        self.rect=self.sprite.rect
        self.text="""We finally got these numbered ping-pong tables installed! Too bad the paddles are still on back-order.
Well, at least I can still practice on the cutting-edge computer simulation in the other room."""

    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Lab Tech",duel=False)


#Fighting Club


class Tyler():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,14)
        self.sprite=characters.NPC(7*64,7*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        text1="""The first rule of the Fighting Club is: you don't talk about the Fighting Club."""
        text2="""I mean, unless you really want to. We don't really enforce that rule."""
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,0,9)
        self.text=[text1,text2]
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Tyler",profile_image=self.portrait)
        
class Norton():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,14)
        self.sprite=characters.NPC(9*64,5*64, self.loaded_sprites,"up")
        self.rect=self.sprite.rect
        text1="""(So he was a hallucination the entire time. What a twist!)"""
        text2="""Oh, hello! I was just playing this video game. Did you want to duel?"""
        self.text=[text1,text2]
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,1,9)
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Norton",profile_image=self.portrait)

class Helena():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,18)
        self.sprite=characters.NPC(3*64,6*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="""We are a generation of duellists, raised by Pokemon cards. And I'm wondering if more Pokemon cards are really the answer."""
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,2,9)
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Helena",profile_image=self.portrait)


class Brad():
    def __init__(self):
        self.loaded_sprites=characters.load_sprites_from_sheet(characters.spritesheet_tcg2,33)
        self.sprite=characters.NPC(5*64,3*64, self.loaded_sprites,"down")
        self.rect=self.sprite.rect
        self.text="""Do you know what a Supporter is? It's just a trainer card. So why do people like you and me know what a Supporter is?"""
        self.portrait=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,3,9)
    
    def interact_object(self,inner_context):
        map_helpers.deliver_lines(self,inner_context,self.text,name_text="Brad",profile_image=self.portrait)
