'''
Menu, deckbuilding UI
'''

import duel_classdefs as cd
from abc import ABC, abstractmethod

class MenuStackNavigation:
    def __init__(self):
        self.menu_stack = ["starting"]

    def reset_to_main(self):
        self.menu_stack = ["starting"]

    def current_menu(self):
        #untested, maybe unnecessary.
        return self.menu_stack[-1]

    def back_one_level(self):
        #untested, maybe unnecessary.
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()

    def jump_to_index(self, index):
        #untested, maybe unnecessary.
        if 0 <= index < len(self.menu_stack):
            self.menu_stack = self.menu_stack[:index + 1]

    def add_to_stack(self, menu):
        self.menu_stack.append(menu)

class Main:
    def __init__(self, player):
        self.navigation = MenuStackNavigation()
        self.player = player
        self.menu_handlers = {
            ("starting",): InitialMenu(),
            ("starting", "checking hand"): Hand(player),
            ("starting", "checking hand", "selected_card"): HandCard(player),
            ("starting", "checking hand", "selected_card", "play energy"): HandCardEnergy(player),
        }
        self.selected_card1=None
        self.selected_card2=None

    def run_menu(self):
        current_stack = tuple(self.navigation.menu_stack)
        handler = self.menu_handlers.get(current_stack)
        if handler:
            choices = handler.get_choices()
            choice = handler.prompt_choice(choices)
            handler.execute_choice(self,choice)
        else:
            print(f"No handler for menu stack: {current_stack}")

class MenuBase(ABC):
    @abstractmethod
    def get_choices(self):
        pass

    @abstractmethod
    def prompt_choice(self, choices):
        pass

    @abstractmethod
    def execute_choice(self, mainref,choice):
        pass

class InitialMenu(MenuBase):
    def get_choices(self):
        return {
            0: "Hand",
            1: "Game board",
            2: "Retreat",
            3: "Attack",
            4: "Pokemon power",
            5: "End turn",
            6: "Resign"
        }

    def prompt_choice(self, choices):
        for key, value in choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input("Choose an option: "))
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, mainref,choice):
        if choice == 0:
            mainref.navigation.add_to_stack("checking hand")


class Hand(MenuBase):
    def __init__(self, player):
        self.player = player

    def get_choices(self):
        choices = {}
        for i, card in enumerate(self.player.hand):
            choices[i] = card
        choices[len(self.player.hand)] = "Cancel"
        return choices

    def prompt_choice(self, choices):
        for key, value in choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input("Choose a card: "))
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, mainref,choice):
        if choice == len(self.player.hand):  # "Cancel"
            mainref.navigation.reset_to_main()
        else:
            mainref.selected_card1 = self.player.hand[choice]
            mainref.navigation.add_to_stack("selected_card")


class HandCard(MenuBase):
    def __init__(self, player):
        self.player = player

    def get_choices(self):
        return {0: "Check information", 1: "Play it", 2: "Cancel"}

    def prompt_choice(self, choices):
        for key, value in choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input("Choose an action: "))
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, mainref,choice):
        if choice == 0:  # Check information
            print(f"Name: {mainref.selected_card1.name}")
        elif choice == 1:  # Play it
            card = mainref.selected_card1
            if card.card_type == "pokemon":
                if len(self.player.bench) >= 5:
                    print("The bench is full")
                else:
                    cd.move_cards_to_from(card, self.player.bench, self.player.hand)
                mainref.navigation.reset_to_main()
            elif card.card_type == "energy":
                mainref.navigation.add_to_stack("play energy")
        elif choice == 2:  # Cancel
            mainref.navigation.reset_to_main()


class HandCardEnergy(MenuBase):
    def __init__(self, player):
        self.player = player

    def get_choices(self):
        available_targets = {0: self.player.active[0]}
        for i, card in enumerate(self.player.bench, start=1):
            available_targets[i] = card
        available_targets[len(available_targets)] = "Cancel"
        return available_targets

    def prompt_choice(self, choices):
        for key, value in choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input("Choose a target: "))
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, mainref,choice):
        if choice == len(self.get_choices()) - 1:  # "Cancel"
            mainref.navigation.reset_to_main()
        else:
            available_targets = {0: self.player.active[0]}
            for i, card in enumerate(self.player.bench, start=1):
                available_targets[i] = card
            target = available_targets[choice]
            cd.move_cards_to_from(mainref.selected_card1, target.attached, self.player.hand)
            mainref.navigation.reset_to_main()

'''
import main
import cards
duel_manager = cd.DuelManager(prizes=6)
player1 = cd.Player(duel_manager)
test=Main(player1)
cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.active)
cd.move_cards_to_from(cd.Energy("water", cardset="basic energy", card_type="energy"),player1.hand)
test.run_menu()
test.run_menu()
test.run_menu()
test.run_menu()'''