class PhaseHandler:
    def __init__(self):
        self.game_phase = "starting"

    def set_game_phase(self, new_phase):
        self.game_phase = new_phase

    def get_game_phase(self):
        return self.game_phase

phase_handler = PhaseHandler()