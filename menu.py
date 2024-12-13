'''
Menu, deckbuilding UI
'''


class MenuManager:
    def __init__(self, root_menu, player):
        self.menu_stack = [root_menu]
        self.player=player
    
    def current_menu(self):
        return self.menu_stack[-1]
    
    def add_submenu(self, submenu):
        self.menu_stack.append(submenu)
    
    def back_one_level(self):
        if len(self.menu_stack) > 1:
            exited_menu = self.menu_stack.pop()
    
    def jump_to_index(self, index):
        if 0 <= index < len(self.menu_stack):
            self.menu_stack = self.menu_stack[:index + 1]
    
    def display_path(self):
        print(" > ".join(self.menu_stack))

    def collect_choices(self):
        if self.menu_stack==["starting"]:
            self.choices={0: "Hand", 1: "Game board", 2: "Retreat", 3: "Attack", 4: "Pokemon power", 5: "End turn", 6: "Resign"}
        if self.menu_stack==["starting","checking hand"]:
            self.choices={}
            for i,card in enumerate(self.player.hand):
                self.choices[i]=card.name
            self.choices[i+1]="Cancel"

    def request_decision(self):
        for i in range(len(self.choices)):
            print(f"{i}: {self.choices[i]}")
        user_choice=int(input())
        if user_choice==0:
            self.add_submenu("checking hand")