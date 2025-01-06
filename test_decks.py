import pytest
import duel_classdefs as cd
import main
import cards
import menu
import decks


def test_loading_deck_from_file():
    duel_manager = cd.DuelManager()
    player1 = cd.Player(duel_manager)    
    cd.move_cards_to_from(decks.generate(decks.seel1x_energy1x),player1.deck)
    assert player1.deck[0].name=="Seel"
    assert player1.deck[1].name=="water"

def test_loading_deck_containing_multiples():
    duel_manager = cd.DuelManager()
    player1 = cd.Player(duel_manager)    
    cd.move_cards_to_from(decks.generate(decks.seel4x_energy10x),player1.deck)
    assert player1.deck[0].name=="Seel"
    assert player1.deck[3].name=="Seel"
    assert player1.deck[4].name=="water"
    assert player1.deck[13].name=="water"
    assert len(player1.deck)==14