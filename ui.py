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


#themenu=Menu(["status","diary","deck","mini-com","coins"],3)
#print(themenu.options)