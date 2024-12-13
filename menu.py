'''
Menu, deckbuilding UI
'''

import duel


class MenuManager:
    def __init__(self, root_menu, player):
        self.menu_stack = [root_menu]
        self.player=player
        self.selected_card_1=None
        self.selected_card_2=None

    def user_prompt(self):
        for i in range(len(self.choices)):
            print(f"{i}: {self.choices[i]}")
        return int(input())

    def user_choice(self):
        '''
        get/generate choices
        list choices, get user input
        process any game results
        store any card information
        update menu stack
        '''
        
        if self.menu_stack==["starting"]:
            self.choices={
            0: "Hand",
            1: "Game board",
            2: "Retreat",
            3: "Attack",
            4: "Pokemon power",
            5: "End turn",
            6: "Resign"
            }
            choice=self.user_prompt()
            if choice==0:
                self.menu_stack.append("checking hand")

        elif self.menu_stack==["starting","checking hand"]:
            self.choices={}
            #possible duplication below
            for i,card in enumerate(self.player.hand):
                self.choices[i]=card
            self.choices[i+1]="Cancel"

            choice=self.user_prompt()
            
            if self.choices[choice]=="Cancel":
                self.menu_stack=self.menu_stack[0]

            else:
                self.selected_card_1=self.choices[choice]
                self.menu_stack.append(self.selected_card_1)


        elif self.menu_stack==["starting", "checking hand",self.selected_card_1]:
            self.choices={0: "Check information", 1:"Play it", 2:"Cancel"}
            choice=self.user_prompt()
            if choice==0:
                print(f"Name: {self.selected_card_1.name}")
            elif choice==1:
                if self.selected_card_1.type=="pokemon":
                    if len(self.player.bench)>=5:
                        print("The bench is full")
                    else:
                        duel.move_cards_to_from(self.selected_card_1,self.player.bench,self.player.hand)
                    self.selected_card_1=None
                    self.menu_stack=self.menu_stack[0]
                elif self.selected_card_1.type=="energy":
                    self.choices={}
                    #possible duplication below
                    self.choices[0]=self.player.active[0]
                    for i,card in enumerate(self.player.bench,start=1):
                        self.choices[i]=card
                    self.choices[len(self.choices)]="Cancel"
                    self.menu_stack.append("selecting target")
            #possible duplication below
            elif self.choices[choice]=="Cancel":
                self.selected_card_1=None
                self.menu_stack=self.menu_stack[0]
        elif self.menu_stack==["starting", "checking hand",self.selected_card_1, "selecting target"]:
            if self.selected_card_1.type=="energy":
                self.choices={}
                self.choices[0]=self.player.active[0]
                for i,card in enumerate(self.player.bench,start=1):
                    self.choices[i]=card
                self.choices[len(self.choices)]="Cancel"

                choice=self.user_prompt()
                
                if self.choices[choice]=="Cancel":
                    self.selected_card_1=None
                    self.selected_card_2=None
                    self.menu_stack=self.menu_stack[0]
                else:
                    self.selected_card_2=self.choices[choice]
                    duel.move_cards_to_from(self.selected_card_1,self.selected_card_2.attached,self.player.hand)
                    self.selected_card_1=None
                    self.selected_card_2=None
                    self.menu_stack=self.menu_stack[0]
