import duel
import main
import cards
import pytest
import effects

@pytest.fixture
def setup_duel():
    duel_manager = duel.DuelManager(main.phase_handler, prizes=1)
    player1 = duel.Player(duel_manager)
    player2 = duel.Player(duel_manager)
    duel.move_cards_to_from(duel.Pokemon(owner=player1,**cards.seel),player1.active)
    duel.move_cards_to_from(duel.Pokemon(owner=player2,**cards.seel),player2.active)
    return duel_manager, player1, player2

def test_attaching_trainer(setup_duel):
    duel_manager, player1, player2 = setup_duel
    duel.move_cards_to_from(duel.Trainer(owner=player1,**cards.defender),player1.active.cards[0].attached)
    assert player1.active.cards[0].attached[0].name=="Defender"

def test_defender_effect(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].add_reduce_dmg_effects.append(effects.defender)
    player2.active.cards[0].attack(player1.active.cards[0],0)
    assert player1.active.cards[0].hp==60

def test_weakness_effect(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].weakness="w"
    if effects.weakness not in player1.active[0].other_effects:
        player1.active[0].other_effects.append(effects.weakness)
    '''hack code to bypass an obscure glitch that I didn't fix in the
    code, where the pokemon has a weakness, then a weakness gets manually
    assigned, so it procs twice because the effect is in the list twice.
    The correct solution is to make "add effect(s)" a function that also
    checks for unique effects, but I'll wait until I get a more robust
    event manager set up first.'''
    player2.active.cards[0].attack(player1.active.cards[0],0)
    assert player1.active.cards[0].hp==40

def test_resistance_effect(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].resistance="w"
    player1.active[0].add_reduce_dmg_effects.append(effects.resistance)
    player2.active.cards[0].attack(player1.active.cards[0],0)
    assert player1.active.cards[0].hp==60

def test_pluspower_effect(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].add_reduce_dmg_effects.append(effects.plus_power)
    player1.active.cards[0].attack(player2.active.cards[0],0)
    assert player2.active.cards[0].hp==40

def test_multiple_pluspower_effects(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].add_reduce_dmg_effects.append(effects.plus_power)
    player1.active[0].add_reduce_dmg_effects.append(effects.plus_power)
    player1.active[0].add_reduce_dmg_effects.append(effects.plus_power)
    player1.active.cards[0].attack(player2.active.cards[0],0)
    assert player2.active.cards[0].hp==20

'''def test_all_add_reduce_damage_effects(setup_duel):
    duel_manager, player1, player2 = setup_duel
    player1.active[0].effects.append(effects.plus_power)
    player1.active[0].effects.append(effects.plus_power)
    player1.active.cards[0].attack(player2.active.cards[0],0)
    assert player2.active.cards[0].hp==30
'''

#try stacking different effects
#confirm that the effects process in the correct order

#test a limited-time effect
#test playing a card that places an effect on a card

#test playing a defender card then being attacked
#test playing a pluspower then attacking

'''
def test_using_defender_card_against_an_attack(setup_duel):
    duel_manager, player1, player2 = setup_duel
    move_cards_to_from(duel.Trainer(owner=player1,**cards.defender),player1.active.cards[0].attached)
    player2.active.cards[0].attack(player1.active.cards[0])
    assert player1.active.cards[0].hp==60
'''
