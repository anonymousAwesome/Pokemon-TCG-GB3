import pygame

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


def dialogue(screen, name_text, photo_location, dialogue_text,font_location):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    black=(0,0,0)

    vert_margin=6
    hor_margin=16

    profile_image=pygame.image.load(photo_location).convert()
    profile_image = pygame.transform.scale(profile_image, (profile_image.get_width() * 4, profile_image.get_height() * 4))

    font = pygame.font.Font(font_location, 48)
    name_font = pygame.font.Font(font_location, 48)

    box_width = 600
    box_height = 150
    box_x = (640 - box_width) // 2
    box_y = 576 - box_height - 20

    #profile image
    screen.blit(profile_image, (box_x+box_width-profile_image.get_width()-2, box_y-profile_image.get_height()))

    # Draw dialogue box
    bg_box(screen,box_x,box_y,box_width,box_height)

    # Render name
    name_surface = name_font.render(name_text, True, white)
    name_x = box_x + 15
    name_y = box_y - 46
    pygame.draw.rect(screen, (30,30,225), (name_x - 10, name_y, name_surface.get_width() + 20, name_surface.get_height()),border_top_left_radius=7,border_top_right_radius=7) 
    pygame.draw.rect(screen, black, (name_x - 12, name_y, name_surface.get_width() + 22, name_surface.get_height()),width=2,border_top_left_radius=7,border_top_right_radius=7)
    screen.blit(name_surface, (name_x, name_y))


    # Render dialogue text
    lines = dialogue_text.split("\n")
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, black)
        text_x = box_x + hor_margin
        text_y = box_y + vert_margin + i * 45
        screen.blit(text_surface, (text_x, text_y))


    #text_surface = font.render(dialogue_text, True, black)
    #screen.blit(text_surface, (box_x+hor_margin, box_y+vert_margin))


def bg_box(screen,box_x,box_y,box_width,box_height):
    pygame.draw.rect(screen, (255, 255, 255), (box_x + 4, box_y + 4, box_width - 8, box_height - 8))  # White background
    pygame.draw.rect(screen, (0,0,200), (box_x, box_y, box_width, box_height), width=6)  # Blue border
    pygame.draw.rect(screen, (125,125,255), (box_x+2, box_y+2, box_width-4, box_height-4), width=2)  # light blue middle



#themenu=Menu(["status","diary","deck","mini-com","coins"],3)
#print(themenu.options)

'''
"I thought what I'd do was, I'd pretend I was one of those deaf-mutes. That way I wouldn't have to have any goddam stupid useless conversations with anybody. If anybody wanted to tell me something, they'd have to write it on a piece of paper and shove it over to me. They'd get bored as hell doing that after a while, and then I'd be through with having conversations for the rest of my life. Everybody'd think I was just a poor deaf-mute bastard and they'd leave me alone."
'''