'''
Menu, deckbuilding UI
'''

import duel


class MenuManager:
    def __init__(self, root_menu, player):
        self.menu_stack = [root_menu]
        self.choices={}
        self.player=player
        self.selected_card_1=None
        self.selected_card_2=None

    def set_choices(self, choices_dict):
        """Helper method to set menu choices."""
        self.choices = choices_dict

    def reset_to_main(self):
        """Reset to the main starting menu."""
        self.menu_stack = ["starting"]
        self.selected_card_1=None
        self.selected_card_2=None

    def user_choice(self):
        '''Main method to handle user choices.
        In order:
        * get/generate choices
        * list choices, get user input
        * process any game results
        * store any card information
        * update menu stack
        '''

        if self.menu_stack == ["starting"]:
            self.starting_menu()
        elif self.menu_stack == ["starting", "checking hand"]:
            self.show_hand()
        elif self.menu_stack == ["starting", "checking hand", "selected_card"]:
            self.info_or_hand()
        elif self.menu_stack == ["starting", "checking hand", "selected_card", "play energy"]:
            self.play_energy_from_hand()

    def user_prompt(self):
        """Prompt user for input and return the selected choice."""
        for key, value in self.choices.items():
            print(f"{key}: {value}")
        while True:
            try:
                choice = int(input())
                if choice in self.choices:
                    return choice
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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
        choice = self.user_prompt()
        if choice == 0:
            self.menu_stack.append("checking hand")

    def show_hand(self):
        hand_choices = {i: card for i, card in enumerate(self.player.hand)}
        hand_choices[len(self.player.hand)] = "Cancel"
        self.set_choices(hand_choices)

        choice = self.user_prompt()
        if self.choices[choice] == "Cancel":
            self.reset_to_main()
        else:
            self.selected_card_1 = self.choices[choice]
            self.menu_stack.append("selected_card")

    def info_or_hand(self):
        self.set_choices({0: "Check information", 1: "Play it", 2: "Cancel"})
        choice = self.user_prompt()

        if choice == 0:
            print(f"Name: {self.selected_card_1.name}")
        elif choice == 1:
            if self.selected_card_1.card_type == "pokemon":
                if len(self.player.bench) >= 5:
                    print("The bench is full")
                else:
                    duel.move_cards_to_from(self.selected_card_1, self.player.bench, self.player.hand)
                self.reset_to_main()
            elif self.selected_card_1.card_type == "energy":
                self.menu_stack.append("play energy")
        elif choice == 2:
            self.reset_to_main()

    def play_energy_from_hand(self):
        available_targets = {0: self.player.active[0]}
        available_targets.update({i: card for i, card in enumerate(self.player.bench, start=1)})
        available_targets[len(available_targets)] = "Cancel"
        self.set_choices(available_targets)

        choice = self.user_prompt()
        if self.choices[choice] == "Cancel":
            self.reset_to_main()
        else:
            self.selected_card_2 = self.choices[choice]
            duel.move_cards_to_from(self.selected_card_1, self.selected_card_2.attached, self.player.hand)
            self.reset_to_main()
