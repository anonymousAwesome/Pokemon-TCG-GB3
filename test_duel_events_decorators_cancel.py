from card_deck_classes import *
import duel
import main
import cards_data
import pytest

@pytest.fixture
def setup_duel():
    duel_manager = duel.DuelManager(main.phase_handler, prizes=1)
    player1 = duel.Player(duel_manager)
    player2 = duel.Player(duel_manager)
    move_cards_to_from(Pokemon(owner=player1,**cards_data.seel),player1.active)
    move_cards_to_from(Pokemon(owner=player2,**cards_data.seel),player2.active)
    return duel_manager, player1, player2

def test_attaching_trainer(setup_duel):
    duel_manager, player1, player2 = setup_duel
    move_cards_to_from(Trainer(owner=player1,**cards_data.defender),player1.active.cards[0].attached)
    assert player1.active.cards[0].attached[0].name=="Defender"


'''
def test_using_defender_against_an_attack(setup_duel):
    duel_manager, player1, player2 = setup_duel
    move_cards_to_from(Trainer(owner=player1,**cards_data.defender),player1.active.cards[0].attached)
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60

#test multiple defenders
'''

def test_placing_defender_effect_on_pokemon(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].effects.append(defender())
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60



#test putting the weakness effect on a pokemon
#test putting the resistance effect on a pokemon