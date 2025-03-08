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



class Menu:
    def __init__(self,options,maxwidth=600):
        self.hor_pos=0
        self.vert_pos=0
        self.location="main menu"

        table = []
        counter = 0
        row = []
        for entry in options:
            row.append(entry)
            counter += 1
            if counter == maxwidth:
                table.append(row)
                row = []
                counter = 0
        if row:
            while len(row) < maxwidth:
                row.append("")
            table.append(row)
        
        self.options=table
        
        self.vert_options_len=len(table)
        self.hor_options_len=maxwidth

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.vert_pos+=1
            if event.key == pygame.K_RETURN:
                self.location=self.options[self.vert_pos][self.hor_pos]

class Dialogue:
    '''
    Note: "dialogue" here refers to both dialogue boxes and non-dialogue
    text boxes that lock the player's input in the same way as a dialogue
    box does.
    I couldn't think of a good term that would refer to both of those but
    wouldn't also include menu text or duel text.'''
    def __init__(self, screen, dialogue_text, name_text=None, photo_location=None):
        self.screen=screen
        self.name_text=name_text
        if photo_location:
            profile_image=pygame.image.load(photo_location).convert()
            self.profile_image = pygame.transform.scale(profile_image, (profile_image.get_width() * 4, profile_image.get_height() * 4))
        else:
            self.profile_image=None
        self.remaining_text=self.preprocess(dialogue_text)
        self.creation_time = time.time()

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
        #draw dialogue box
        bg_box(self.screen,box_x,box_y,box_width,box_height)

        if self.profile_image:
            #profile image
            self.screen.blit(self.profile_image, (box_x+box_width-self.profile_image.get_width()-2, box_y-self.profile_image.get_height()))

        if self.name_text:
            #render name
            name_surface = font.render(self.name_text, True, white)
            name_x = box_x + 15
            name_y = box_y - 46
            pygame.draw.rect(self.screen, (30,30,225), (name_x - 10, name_y, name_surface.get_width() + 20, 48),border_top_left_radius=7,border_top_right_radius=7) 
            pygame.draw.rect(self.screen, black, (name_x - 12, name_y, name_surface.get_width() + 22, 48),width=2,border_top_left_radius=7,border_top_right_radius=7)
            self.screen.blit(name_surface, (name_x, name_y+2))

        #displays the text
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
                if len(lines) >= max_lines:
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


    def render(self,event_list,map_input_lock):

        self.process_current_window() #note to self: probably shouldn't process the window anew each time through the loop. Do something about that.
        self.display_text()

        for event in event_list.events:
            if event.type==pygame.KEYDOWN:
                if event.key==key_mappings.affirm_key or event.key==key_mappings.cancel_key:
                    self.remaining_text=self.words

        if not self.remaining_text:
            map_input_lock.unlock()


def bg_box(screen,box_x,box_y,box_width,box_height):
    pygame.draw.rect(screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
    pygame.draw.rect(screen, (0,0,200), (box_x, box_y, box_width, box_height), width=6)  # Blue border
    pygame.draw.rect(screen, (125,125,255), (box_x+2, box_y+2, box_width-4, box_height-4), width=2)  # light blue middle


def club_name_render(screen, text):
    name_surface = club_font.render(text, True,(0,0,0))
    w=name_surface.get_width()
    h=name_surface.get_height()
    box_x,box_y,box_width,box_height=48,28,w+40,h+20
    pygame.draw.rect(screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
    pygame.draw.rect(screen, (0,0,0), (box_x, box_y, box_width, box_height), width=4)  # Black border
    screen.blit(name_surface, (68, 40))
    

#themenu=Menu(["status","diary","deck","mini-com","coins"],3)
#print(themenu.options)
