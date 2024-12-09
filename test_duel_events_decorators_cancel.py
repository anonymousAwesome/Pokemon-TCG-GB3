import card_deck_classes as cdc
import duel
import main
import cards_data
import pytest
import effects

@pytest.fixture
def setup_duel():
    duel_manager = duel.DuelManager(main.phase_handler, prizes=1)
    player1 = duel.Player(duel_manager)
    player2 = duel.Player(duel_manager)
    cdc.move_cards_to_from(cdc.Pokemon(owner=player1,**cards_data.seel),player1.active)
    cdc.move_cards_to_from(cdc.Pokemon(owner=player2,**cards_data.seel),player2.active)
    return duel_manager, player1, player2

def test_attaching_trainer(setup_duel):
    duel_manager, player1, player2 = setup_duel
    cdc.move_cards_to_from(cdc.Trainer(owner=player1,**cards_data.defender),player1.active.cards[0].attached)
    assert player1.active.cards[0].attached[0].name=="Defender"


'''
def test_using_defender_against_an_attack(setup_duel):
    duel_manager, player1, player2 = setup_duel
    move_cards_to_from(cdc.Trainer(owner=player1,**cards_data.defender),player1.active.cards[0].attached)
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60

#test multiple defenders
'''

def test_placing_and_triggering_defender_effect_on_pokemon(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].effects.append(effects.defender())
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60

def test_placing_and_triggering_weakness_effect_on_pokemon(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].effects.append(effects.weakness("water"))
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==40

def test_placing_and_triggering_resistance_effect_on_pokemon(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].effects.append(effects.resistance("water"))
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60



#test a limited-time effect
#test an effect that triggers when a card is played