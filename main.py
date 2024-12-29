import duel_classdefs as cd
import duel
import decks
import cards
import pygame
import overworld

class PhaseHandler:
    def __init__(self):
        self.game_phase = "starting"

    def set_game_phase(self, new_phase):
        self.game_phase = new_phase
        '''to-do: add code that checks the new phase against a list of
        possible phases.'''

    def get_game_phase(self):
        return self.game_phase

phase_handler = PhaseHandler()

if __name__ == "__main__":

    duel_manager = cd.DuelManager(phase_handler)
    player1 = cd.Player(duel_manager)
    player2 = cd.Player(duel_manager)
    deck1=decks.generate([[cards.water,17],[cards.dratini,4],[cards.hitmonchan,3],[cards.seel,1],[cards.machop,1]],player1)
    deck2=decks.generate([[cards.water,17],[cards.dratini,4],[cards.hitmonchan,3],[cards.seel,1],[cards.machop,1]],player1)
    cd.move_cards_to_from(deck1,player1.deck)
    cd.move_cards_to_from(deck2,player2.deck)
    player1.initial_draw()
    player2.initial_draw()
    player1.prizes.place()
    player1.prizes.place()

    #duel_manager.starting_coin()
    duel_manager.turn="player" #manually let the player go first
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #overworld.render()
        duel.render()
    pygame.quit()