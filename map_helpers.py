import random
import numpy as np

with open("profanity_dict.txt", 'r') as file:
    profanity_words=file.read().splitlines()

vowels="aeiou"

first_consonants=['B', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Z',"Bl", "Cl", "Fl", "Gl", "Pl",
"Sl", "Br", "Cr", "Dr", "Fr", "Gr", "Pr", "Tr", "Sk", "Sm", "Sn",
"Sp", "St", "Sw", "Tw",'Sh', 'Ch','Th']

second_consonants=['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
'p', 'r', 's', 't', 'v', 'w', 'x', 'z',"bb","bl", "cl", "fl", "gg","gl", "pl",
"sl", "br", "cr", "dr", "fr", "gr", "pr", "pt", "tr", "sc", "sk", "sm", "sn",
"sp", "st", "sw", "tw",'sh', 'ch','th','ng', 'nt', 'rs', 'll', 'ns', 'ss',
'nd', 'nk', 'ct', 'tt', 'rt', 'ck', 'rr']

third_consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
'p', 'r', 's', 't', 'v', 'w', 'x', 'z',"bl", "cl", "fl", "gl", "pl",
"sk", "sp", "st", 'sh', 'ch','th','ng', 'nt', 'rs', 'll', 'ns', 'ss',
'nd', 'nk', 'ct', 'tt', 'rt', 'ck', 'rr']


#Note: the lists *are* different from each other.
#Don't combine them.

def word_is_safe(string):
        return not any(word in string for word in profanity_words)

def gen_word():
    while True:
        word=""
        word+=random.choice(first_consonants)
        word+=random.choice(vowels)
        word+=random.choice(second_consonants)
        word+=random.choice(vowels)
        if random.randint(0,1):
            word+=random.choice(vowels)
        if random.randint(0,1):
            word+=random.choice(third_consonants)
        if len(word)==4 and word[3]=="e":
            word+="h"
        if word_is_safe(word):
            return word


def reload_map(inner_context,replacement_map):
    inner_context.map_holder.__init__(replacement_map)
    if inner_context.player_data.currently_greyscale:
        inner_context.map_holder.current_map.bg_image.blit(inner_context.perceptual_greyscale(inner_context.map_holder.current_map.bg_image),(0,0))

    inner_context.temp_exit_list.__init__(inner_context.map_holder,inner_context.player_character)
    inner_context.current_npcs.reset(replacement_map)
    inner_context.collision_manager.__init__(inner_context.map_holder.current_map.bg_image, inner_context.player_character, inner_context.screen, inner_context.current_dialogue, inner_context.event_manager, inner_context.map_input_lock, obstacles=inner_context.map_holder.current_map.obstacles, npcs=inner_context.current_npcs)


def award_rewards(inner_context,reward):
    if inner_context.phase_handler.won_last_duel:
        print(f"{reward=}")
        inner_context.player_data.card_pool.extend(reward)
        inner_context.phase_handler.won_last_duel=False



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


class EmptyEvent():
    def __init__(self,loops_left):
        self.loops_left=loops_left
    def decrement_loops(self):
        self.loops_left-=1
    def check_still_looping(self):
        return self.loops_left


def dialogue_facing(player_character,npc):
    if player_character.facing_direction=="down":
        npc.sprite.manual_direction_change("up")
    if player_character.facing_direction=="up":
        npc.sprite.manual_direction_change("down")
    if player_character.facing_direction=="left":
        npc.sprite.manual_direction_change("right")
    if player_character.facing_direction=="right":
        npc.sprite.manual_direction_change("left")


class FFCutsceneHelpers:

    def __init__(self,inner_context):
        self.inner_context=inner_context

    def group_move(self,inner_context,speed):
        for npc in inner_context.current_npcs.current_npcs:
            npc.sprite.cutscene_walk("down")
            npc.sprite.move_npc(speed)

    def check_bottom(self,y_coord):
        lowest=0
        for npc in self.inner_context.current_npcs.current_npcs:
            if npc.rect.bottom>lowest:
                lowest=npc.rect.bottom
        if lowest>y_coord:
            return False
        else:
            return True


def dialogue_duel(npc_self,inner_context,text,name_text=None,profile_image=None,duel=True,post_duel_text=None,reward=["card1","card2"]):
    #may need to add an argument for pre-duel text, but currently not sure how
    #duels are going to be handled.
    inner_context.event_manager.add_event(dialogue_facing,[inner_context.player_character,npc_self])
    kwargs_dict={}
    if name_text:
        kwargs_dict["name_text"]=name_text
    if profile_image:
        kwargs_dict["profile_image"]=profile_image
    if type(text) is str:
            inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text],kwargs_dict)
            inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    elif type(text) is list:
        for line in text:
            inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,line],kwargs_dict)
            inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    if duel:
        #inner_context.event_manager.add_event(inner_context.phase_handler.set_duel_data,[],{"player_deck":[~~the player's deck~~],"opponent_deck":[~~the opponent's deck~~],"background_image":~~the background image~~})
        inner_context.event_manager.add_event(inner_context.phase_handler.set_game_phase,["duel"])
        inner_context.event_manager.add_event(award_rewards,[inner_context,reward])
        inner_context.event_manager.add_event(print,[inner_context.player_data.card_pool])
    if post_duel_text:
        inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,post_duel_text],kwargs_dict)
        inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
    inner_context.map_input_lock.lock()

