import pygame
import time
import key_mappings

font_height=45
font = pygame.font.Font("./assets/pokemon-emerald.otf", font_height)
club_font = pygame.font.Font("./assets/pokemon-emerald.otf", 60)


white = (255, 255, 255)
blue = (0, 0, 255)
black=(0,0,0)

vert_margin=6
hor_margin=16

box_width = 600
box_height = 150
box_x = (640 - box_width) // 2
box_y = 576 - box_height - 20


class ChoiceOptions:
    def __init__(self, inner_context):
        self.inner_context = inner_context
        self.still_active = True
        self.option_manager = OptionManager(["choice 1", "choice 2", "choice 3"])
        self.input_processor = InputProcessor()
    
    def check_still_active(self):
        return self.still_active
    
    def render_ui(self):
        pygame.draw.rect(self.inner_context.screen, (255, 0, 255), (20, 20, 100, 100))
        current_choice = self.option_manager.get_current()
        #print(f"Current: {current_choice}")
    
    def process_input(self):
        actions = self.input_processor.process_events(
            self.inner_context.event_list, 
            self.option_manager.current_index
        )
        
        for action in actions:
            if action == "move_up":
                self.option_manager.move_up()
                print(f"index {self.option_manager.current_index}: {self.option_manager.get_current()}")
            elif action == "move_down":
                self.option_manager.move_down()
                print(f"index {self.option_manager.current_index}: {self.option_manager.get_current()}")
            elif action == "select":
                print(f"Selected: {self.option_manager.get_current()}")
            elif action == "cancel":
                self.still_active = False
    
    def display_choices(self):
        self.render_ui()
        self.process_input()


class InputProcessor:
    
    def process_events(self, event_list, current_state):
        """Process events and return actions"""
        actions = []
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == key_mappings.up_key:
                    actions.append("move_up")
                elif event.key == key_mappings.down_key:
                    actions.append("move_down")
                elif event.key == key_mappings.affirm_key:
                    actions.append("select")
                elif event.key == key_mappings.cancel_key:
                    actions.append("cancel")
        return actions

class OptionManager:
    def __init__(self, options):
        self.options = options
        self.current_index = 0
    
    def move_up(self):
        if self.current_index > 0:
            self.current_index -= 1
            return True
        return False
    
    def move_down(self):
        if self.current_index + 1 < len(self.options):
            self.current_index += 1
            return True
        return False
    
    def get_current(self):
        return self.options[self.current_index]
    
    def get_all_options(self):
        return self.options



class Dialogue:
    '''
    Note: "dialogue" here refers to both dialogue boxes and non-dialogue
    text boxes that lock the player's input in the same way as a dialogue
    box does.
    I couldn't think of a good term that would refer to both of those but
    wouldn't also include menu text or duel text.'''
    def __init__(self, screen, dialogue_text, name_text=None, profile_image=None,greyscale=False):
        self.screen=screen
        self.name_text=name_text
        self.profile_image=profile_image
        self.remaining_text=self.preprocess(dialogue_text)
        self.creation_time = time.time()
        self.process_current_window()
        self.greyscale=greyscale

    def check_remaining_text(self):
        return self.remaining_text

    def preprocess(self,dialogue_string):
        # Split by spaces, then by newlines, keeping track of the \n characters
        if dialogue_string:
            parts = dialogue_string.split(" ")
            words = []
            temp = []
            for part in parts:
                if '\n' in part:
                    split_part = part.split('\n')
                    for i, sub_part in enumerate(split_part):
                        if i > 0: 
                            words.append("\n")
                        words.append(sub_part)
                else:
                    words.append(part)
            return words
        else:
            return ""

    def elapsed_time(self):
        return time.time() - self.creation_time

    def __bool__(self):
        return len(self.remaining_text)>0

    def display_text(self):
        bg_box(self.screen,box_x,box_y,box_width,box_height,greyscale=False)

        if self.profile_image:
            if self.name_text:
                self.screen.blit(self.profile_image, (box_x+2, box_y-self.profile_image.get_height()-46))
            else:
                self.screen.blit(self.profile_image, (box_x+2, box_y-self.profile_image.get_height()))

        if self.name_text:
            name_surface = font.render(self.name_text, True, white)
            if self.profile_image:
                name_x = box_x+6
                name_y = box_y - 46
                name_box_width=max(name_surface.get_width()+22,self.profile_image.get_width())
                if self.greyscale:
                    pygame.draw.rect(self.screen, (180,180,180), (name_x-5, name_y, name_box_width+3, 48)) 
                else:
                    pygame.draw.rect(self.screen, (30,30,225), (name_x-5, name_y, name_box_width+3, 48)) 
                pygame.draw.rect(self.screen, black, (name_x - 7, name_y, name_box_width + 5, 48),width=2)
                self.screen.blit(name_surface, (name_x+8, name_y))
               
            else:
                name_x = box_x + 15
                name_y = box_y - 46
                if self.greyscale:
                    pygame.draw.rect(self.screen, (180,180,180), (name_x - 10, name_y, name_surface.get_width() + 20, 48),border_top_left_radius=7,border_top_right_radius=7) 
                else:
                    pygame.draw.rect(self.screen, (30,30,225), (name_x - 10, name_y, name_surface.get_width() + 20, 48),border_top_left_radius=7,border_top_right_radius=7) 
                pygame.draw.rect(self.screen, black, (name_x - 12, name_y, name_surface.get_width() + 22, 48),width=2,border_top_left_radius=7,border_top_right_radius=7)
                self.screen.blit(name_surface, (name_x, name_y+2))


        for i, line in enumerate(self.lines):
            text_surface = font.render(line, True, black)
            text_x = box_x + hor_margin
            text_y = box_y + vert_margin + i * font_height
            self.screen.blit(text_surface, (text_x, text_y))

    def process_current_window(self):
        '''checks to see how much will fit in the current window, adds
        that to... self.lines? I guess? while taking the word off of 
        self.words. self.words isn't used, unless the player presses 
        a button and render() sets self.remaining text equal to self.words'''
        self.words = self.remaining_text[:]
        self.lines = []
        current_line = ""
        max_lines = (box_height - 2 * vert_margin) // font_height

        while self.words:
            word = self.words.pop(0)
            
            if word == "\n":
                if current_line:
                    self.lines.append(current_line)
                    current_line = ""
                if len(self.lines) >= max_lines:
                    break
                continue

            if current_line:
                box_width_check_line=current_line+" "+word

            if not current_line:
                box_width_check_line=word 

            if font.size(box_width_check_line)[0] <= (box_width - 2 * hor_margin):
                current_line = box_width_check_line
            else:
                self.lines.append(current_line)
                current_line = word
                if len(self.lines) >= max_lines:
                    self.words.insert(0, word)  # Put the last unprocessed word back
                    break

        if current_line and len(self.lines) < max_lines:
            self.lines.append(current_line)


    def render(self,event_list):

        self.display_text()

        for event in event_list:
            if event.type==pygame.KEYDOWN:
                if event.key==key_mappings.affirm_key or event.key==key_mappings.cancel_key:
                    self.remaining_text=self.words
                    self.process_current_window()


def bg_box(screen,box_x,box_y,box_width,box_height,greyscale=False):
    pygame.draw.rect(screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
    if greyscale:
        pygame.draw.rect(screen, (70,70,70), (box_x, box_y, box_width, box_height), width=6)  # grey border
        pygame.draw.rect(screen, (150,150,150), (box_x+2, box_y+2, box_width-4, box_height-4), width=2)  # lighter grey middle
    else:
        pygame.draw.rect(screen, (0,0,200), (box_x, box_y, box_width, box_height), width=6)  # Blue border
        pygame.draw.rect(screen, (125,125,255), (box_x+2, box_y+2, box_width-4, box_height-4), width=2)  # light blue middle


def club_name_render(screen, text):
    keys = pygame.key.get_pressed()
    if not keys[key_mappings.up_key] and not keys[key_mappings.down_key] and not keys[key_mappings.right_key] and not keys[key_mappings.left_key]:
        name_surface = club_font.render(text, True,(0,0,0))
        w=name_surface.get_width()
        h=name_surface.get_height()
        box_x,box_y,box_width,box_height=48,28,w+40,h+20
        pygame.draw.rect(screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
        pygame.draw.rect(screen, (0,0,0), (box_x, box_y, box_width, box_height), width=4)  # Black border
        screen.blit(name_surface, (68, 40))
    