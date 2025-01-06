'''
Menu, deckbuilding UI
'''

import duel_classdefs as cd

class MenuStackNavigation:
    def __init__(self, root_menu):
        self.menu_stack = [root_menu]

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
    def __init__(self, root_menu, player):
        self.navigation = MenuStackNavigation(root_menu)
        self.helpers = MainHelperFunctions(player)
        self.choices = {}

    def set_choices(self, choices_dict):
        self.choices = choices_dict

    def user_choice(self):
        if self.navigation.menu_stack==["starting"]:
            self.starting_menu()
        elif self.navigation.menu_stack == ["starting","checking hand"]:
            self.handle_show_hand()
        elif self.navigation.menu_stack == ["starting","checking hand","selected_card"]:
            self.handle_card_action()
        elif self.navigation.menu_stack == ["starting","checking hand","selected_card","play energy"]:
            self.handle_play_energy()

    def starting_menu(self):
        self.set_choices({
            0: "Hand",
            1: "Game board",
            2: "Retreat",
            3: "Attack",
            4: "Pokemon power",
            5: "End turn",
            6: "Resign"
        })
        choice = self.helpers.prompt_choices(self.choices)
        if choice == 0:
            self.navigation.add_to_stack("checking hand")

    def handle_show_hand(self):
        hand_choices = self.helpers.show_hand()
        self.set_choices(hand_choices)
        choice = self.helpers.prompt_choices(self.choices)
        result = self.helpers.process_card_selection(choice, hand_choices)
        if result == "cancel":
            self.navigation.reset_to_main()
        else:
            self.navigation.add_to_stack(result)

    def handle_card_action(self):
        self.set_choices({0: "Check information", 1: "Play it", 2: "Cancel"})
        choice = self.helpers.prompt_choices(self.choices)

        if choice == 0:
            print(f"Name: {self.helpers.selected_card_1.name}")
        elif choice == 1:
            card = self.helpers.selected_card_1
            if card.card_type == "pokemon":
                if len(self.helpers.player.bench) >= 5:
                    print("The bench is full")
                else:
                    cd.move_cards_to_from(card, self.helpers.player.bench, self.helpers.player.hand)
                self.navigation.reset_to_main()
            elif card.card_type == "energy":
                self.navigation.add_to_stack("play energy")
        elif choice == 2:
            self.navigation.reset_to_main()

    def handle_play_energy(self):
        available_targets = self.helpers.play_energy()
        self.set_choices(available_targets)
        choice = self.helpers.prompt_choices(self.choices)
        result = self.helpers.attach_energy(choice, available_targets)
        if result == "cancel" or result == "done":
            self.navigation.reset_to_main()

class MainHelperFunctions:
    def __init__(self, player):
        self.player = player
        self.selected_card_1 = None
        self.selected_card_2 = None

    def prompt_choices(self,choices):
        for key, value in choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input())
                if choice in choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def show_hand(self):
        hand_choices = {i: card for i, card in enumerate(self.player.hand)}
        hand_choices[len(self.player.hand)] = "Cancel"
        return hand_choices

    def process_card_selection(self, choice, hand_choices):
        if hand_choices[choice] == "Cancel":
            return "cancel"
        self.selected_card_1 = hand_choices[choice]
        return "selected_card"

    def play_energy(self):
        available_targets = {0: self.player.active[0]}
        for i, card in enumerate(self.player.bench, start=1):
            available_targets[i] = card
        available_targets[len(available_targets)] = "Cancel"
        return available_targets

    def attach_energy(self, choice, available_targets):
        if available_targets[choice] == "Cancel":
            return "cancel"
        self.selected_card_2 = available_targets[choice]
        cd.move_cards_to_from(self.selected_card_1, self.selected_card_2.attached, self.player.hand)
        return "done"
