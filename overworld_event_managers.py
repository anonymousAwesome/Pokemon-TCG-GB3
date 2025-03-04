from collections import deque

class OverworldEventManager:
    def __init__(self):
        self.event_queue = deque()  # Queue for ordered events

    def add_event(self, event_func, *args, **kwargs):
        """Adds an event (function) to the queue."""
        self.event_queue.append((event_func, args, kwargs))

    def run_next_event(self):
        """Runs the next event if available."""
        if self.event_queue:
            event_func, args, kwargs = self.event_queue.popleft()
            event_func(*args, **kwargs)  # Execute the event function

    def run_all_events(self):
        """Runs all events sequentially until queue is empty."""
        while self.event_queue:
            self.run_next_event()


class OverworldEvents:
    def __init__(self):
        self.event_manager = OverworldEventManager()

    def interact_with_map_object(self,map_holder):
        pass

'''
    def start_npc_interaction(self, npc):
        print(f"{npc} approaches you.")
        self.event_manager.add_event(self.trigger_dialogue, npc)

    def trigger_dialogue(self, npc):
        print(f"{npc}: 'Do you want to duel me?'")
        self.event_manager.add_event(self.player_choice_prompt, npc)

    def player_choice_prompt(self, npc):
        choice = input("Accept duel? (yes/no): ").strip().lower()
        if choice == "yes":
            self.event_manager.add_event(self.start_duel, npc)
        else:
            self.event_manager.add_event(self.decline_duel, npc)

    def decline_duel(self, npc):
        print(f"{npc}: 'Maybe next time!'")

    def start_duel(self, npc):
        print(f"You engage in a duel with {npc}!")
        result = self.resolve_duel(npc)
        if result == "win":
            self.event_manager.add_event(self.win_duel, npc)
        else:
            self.event_manager.add_event(self.lose_duel, npc)

    def resolve_duel(self, npc):
        # Placeholder duel logic (random win/loss)
        import random
        return "win" if random.choice([True, False]) else "lose"

    def win_duel(self, npc):
        print(f"You defeated {npc}!")
        self.event_manager.add_event(self.give_booster_pack)

    def lose_duel(self, npc):
        print(f"{npc} defeated you! Better luck next time.")

    def give_booster_pack(self):
        print("You receive a booster pack!")
'''

events = OverworldEvents()
#events.start_npc_interaction("Duelist Dan")
events.event_manager.run_all_events()
