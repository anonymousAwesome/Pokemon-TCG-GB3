import pygame
import time

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
    def __init__(self, screen, dialogue_text, name_text=None, photo_location=None):
        self.screen=screen
        self.name_text=name_text
        profile_image=pygame.image.load(photo_location).convert()
        self.profile_image = pygame.transform.scale(profile_image, (profile_image.get_width() * 4, profile_image.get_height() * 4))
        self.remaining_text=self.preprocess(dialogue_text)
        self.creation_time = time.time()
        self.font_height=45
        self.font = pygame.font.Font("./assets/pokemon-emerald.otf", self.font_height)
        self.name_font = pygame.font.Font("./assets/pokemon-emerald.otf", 45)


    def elapsed_time(self):
        return time.time() - self.creation_time

    def __bool__(self):
        return len(self.remaining_text)>0

    def render_dialogue(self):
        self.render()

        white = (255, 255, 255)
        blue = (0, 0, 255)
        black=(0,0,0)

        vert_margin=6
        hor_margin=16

        box_width = 600
        box_height = 150
        box_x = (640 - box_width) // 2
        box_y = 576 - box_height - 20



        #profile image
        self.screen.blit(self.profile_image, (box_x+box_width-self.profile_image.get_width()-2, box_y-self.profile_image.get_height()))

        #render name
        name_surface = self.name_font.render(self.name_text, True, white)
        name_x = box_x + 15
        name_y = box_y - 46
        pygame.draw.rect(self.screen, (30,30,225), (name_x - 10, name_y, name_surface.get_width() + 20, 48),border_top_left_radius=7,border_top_right_radius=7) 
        pygame.draw.rect(self.screen, black, (name_x - 12, name_y, name_surface.get_width() + 22, 48),width=2,border_top_left_radius=7,border_top_right_radius=7)
        self.screen.blit(name_surface, (name_x, name_y+2))


    def render(self):
        '''Yes, this function is probably doing too much. Not worth the
        effort to refactor it, though.'''
        white = (255, 255, 255)
        blue = (0, 0, 255)
        black=(0,0,0)

        vert_margin=6
        hor_margin=16

        box_width = 600
        box_height = 150
        box_x = (640 - box_width) // 2
        box_y = 576 - box_height - 20


        #draw dialogue box
        self.bg_box(box_x,box_y,box_width,box_height)

        #process and render dialogue
        words = self.remaining_text
        lines = []
        temp_line = ""
        max_lines = (box_height - 2 * vert_margin) // self.font_height

        while words:
            word = words.pop(0)
            
            if word == "\n":
                if temp_line:
                    lines.append(temp_line)
                    temp_line = ""
                if len(lines) >= max_lines:
                    break
                continue

            if temp_line:
                test_line=temp_line+" "+word

            if not temp_line:
                test_line=word 

            if self.font.size(test_line)[0] <= (box_width - 2 * hor_margin):
                temp_line = test_line
            else:
                lines.append(temp_line)
                temp_line = word
                if len(lines) >= max_lines:
                    words.insert(0, word)  # Put the last unprocessed word back
                    break

        if temp_line and len(lines) < max_lines:
            lines.append(temp_line)

        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, black)
            text_x = box_x + hor_margin
            text_y = box_y + vert_margin + i * self.font_height
            self.screen.blit(text_surface, (text_x, text_y))
            
        return words


    def preprocess(self,dialogue_string):
        # Split by spaces, then by newlines, keeping track of the \n characters
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


    def bg_box(self,box_x,box_y,box_width,box_height):
        pygame.draw.rect(self.screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
        pygame.draw.rect(self.screen, (0,0,200), (box_x, box_y, box_width, box_height), width=6)  # Blue border
        pygame.draw.rect(self.screen, (125,125,255), (box_x+2, box_y+2, box_width-4, box_height-4), width=2)  # light blue middle



#themenu=Menu(["status","diary","deck","mini-com","coins"],3)
#print(themenu.options)
