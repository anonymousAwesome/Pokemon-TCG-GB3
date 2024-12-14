import pytest
import duel
import main
import cards
import menu
import decks


def test_loading_deck_from_file():
    duel_manager = duel.DuelManager(main.phase_handler)
    player1 = duel.Player(duel_manager)    
    duel.move_cards_to_from(decks.load(decks.seel1x_energy1x,player1),player1.deck)
    assert player1.deck[0].name=="Seel"
    assert player1.deck[1].name=="water"

def test_loading_deck_containing_multiples():
    duel_manager = duel.DuelManager(main.phase_handler)
    player1 = duel.Player(duel_manager)    
    duel.move_cards_to_from(decks.load(decks.seel4x_energy10x,player1),player1.deck)
    assert player1.deck[0].name=="Seel"
    assert player1.deck[3].name=="Seel"
    assert player1.deck[4].name=="water"
    assert player1.deck[13].name=="water"
    assert len(player1.deck)==14