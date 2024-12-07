import pytest
from card_deck_classes import *

import duel
import main

import cards_data


@pytest.fixture
def player1():
    duel_manager=duel.DuelManager(main.phase_handler,prizes=6)
    return(duel.Player(duel_manager))

@pytest.fixture
def player2():
    duel_manager=duel.DuelManager(main.phase_handler,prizes=6)
    return(duel.Player(duel_manager))

@pytest.fixture
def pikachu1(player1):
    pikachu = Pokemon(
        name="Pikachu",
        cardset="base",
        energy_type="electric",
        evolution_level="basic",
        hp=40,
        attack_cost=0,
        attack_dmg=10,
        retreat_cost=0,
        owner=player1,
        weakness="fighting",
    ) 
    return(pikachu)

@pytest.fixture    
def pikachu2(player2):
    pikachu = Pokemon(
        name="Pikachu",
        cardset="base",
        energy_type="electric",
        evolution_level="basic",
        hp=40,
        attack_cost=0,
        attack_dmg=10,
        retreat_cost=0,
        owner=player2,
        weakness="fighting",
    ) 
    return(pikachu)

@pytest.fixture    
def raichu1(player1):
    raichu = Pokemon(
        name="Raichu",
        cardset="base",
        energy_type="electric",
        evolution_level="stage 1",
        hp=60,
        attack_cost=0,
        attack_dmg=20,
        retreat_cost=1,
        owner=player1,
        evolves_from="Pikachu",
        weakness="fighting",
    ) 
    return(raichu)

def test_one_active_pokemon(player1, pikachu1):
    active=CardCollection(player1, pikachu1)
    assert pikachu1 in active

def test_two_active_pokemon(player1, player2, pikachu1,pikachu2):
    active1=CardCollection(player1, pikachu1)
    active2=CardCollection(player2, pikachu2)
    assert pikachu1 in active1
    assert pikachu2 in active2

def test_one_pokemon_attacking_another(pikachu1,pikachu2):
    pikachu1.attack(pikachu2)
    assert pikachu2.hp==30

def test_hp_past_max_doesnt_go_negative(pikachu1,pikachu2):
    pikachu1.attack_dmg=50
    pikachu1.attack(pikachu2)
    assert pikachu2.hp==0

def test_negative_damage(pikachu1,pikachu2):
    pikachu1.attack_dmg=-20
    pikachu1.attack(pikachu2)
    assert pikachu2.hp==40

def test_KO_removes_one_prize_card(pikachu1,pikachu2):
    pikachu1.attack_dmg=50
    pikachu1.attack(pikachu2)
    assert pikachu1.owner.prizes==5

def test_won_coin_flip_then_two_turns_end():
    duel_object=duel.DuelManager(main.PhaseHandler(),prizes=6)
    duel_object.user_won_starting_coin(True)
    assert duel_object.turn=="player"
    duel_object.advance_turn()
    assert duel_object.turn=="computer"
    duel_object.advance_turn()
    assert duel_object.turn=="player"

def test_lost_coin_flip_then_two_turns_end():
    duel_object=duel.DuelManager(main.PhaseHandler(),prizes=6)
    duel_object.user_won_starting_coin(False)
    assert duel_object.turn=="computer"
    duel_object.advance_turn()
    assert duel_object.turn=="player"
    duel_object.advance_turn()
    assert duel_object.turn=="computer"

def test_starting_phase_handler():
    phase_handler = main.PhaseHandler()
    assert phase_handler.get_game_phase()=="starting"

def test_starting_duel_phase():
    phase_handler = main.PhaseHandler()
    new_duel=duel.DuelManager(phase_handler,prizes=6)
    assert phase_handler.get_game_phase()=="duelling"

def test_ending_duel_phase():
    phase_handler = main.PhaseHandler()
    new_duel=duel.DuelManager(phase_handler,prizes=6)
    new_duel.end_duel()
    assert phase_handler.get_game_phase()=="club"

def test_new_game_phases_per_test():
    phase_handler = main.PhaseHandler()
    assert phase_handler.get_game_phase()=="starting"
    
def test_ko_with_1_prize_remaining_ends_duel(player2,pikachu1,pikachu2):
    pikachu2.attack_dmg=50
    pikachu2.owner.prizes=1
    pikachu2.attack(pikachu1)
    assert player2.duel_handler.phase_handler.get_game_phase()=="club"

def test_attach_energy_to_pokemon(player1,pikachu1):
    water_energy=Energy("water", "basic energy", player1)
    pikachu1.attach_energy(water_energy)
    assert water_energy in pikachu1.attached_energy

def test_moving_water_deck_hand_discard(player1):
    deck=Deck(player1)
    hand=Hand(player1)
    discard_pile=DiscardPile(player1)
    water_energy=Energy("water", "basic energy", player1)
    move_cards_to_from(water_energy, deck)
    assert water_energy in deck
    move_cards_to_from(water_energy, hand, deck)
    assert water_energy in hand
    assert water_energy not in deck
    move_cards_to_from(water_energy, discard_pile, hand)
    assert water_energy in discard_pile
    assert water_energy not in hand
    

def test_moving_pikachu_deck_hand_bench_active(pikachu1,player1):
    deck=Deck(player1)
    hand=Hand(player1)
    active=Active(player1)
    bench=Bench(player1)
    move_cards_to_from(pikachu1, deck)
    assert pikachu1 in deck
    move_cards_to_from(pikachu1,hand, deck)
    assert pikachu1 in hand
    assert pikachu1 not in deck
    move_cards_to_from(pikachu1,active, hand)
    assert pikachu1 in active
    assert pikachu1 not in hand
    move_cards_to_from(pikachu1,bench, active)
    assert pikachu1 in bench
    assert pikachu1 not in active

def test_evolve_pikachu(player1, pikachu1, raichu1):
    active=Active(player1)
    move_cards_to_from(pikachu1,active)
    pikachu1.evolve(raichu1,active)
    assert raichu1 in active
    assert pikachu1 not in active
    assert pikachu1 in raichu1.stored_pre_evolution

def test_costless_retreat_pikachu(pikachu1, raichu1):
    active=Active(player1)
    bench=Bench(player1)
    move_cards_to_from(pikachu1,active)
    move_cards_to_from(raichu1,bench)
    assert pikachu1 in active
    assert raichu1 in bench
    move_cards_to_from(pikachu1,bench,active)
    move_cards_to_from(raichu1,active,bench)
    assert pikachu1 in bench
    assert raichu1 in active

def test_add_multiple_cards(pikachu1,raichu1):
    hand=Hand(player1)
    move_cards_to_from([pikachu1,raichu1],hand)
    assert pikachu1 in hand
    assert raichu1 in hand
    
def test_weakness(pikachu1,player1):
    geodude = Pokemon(
        name="Geodude",
        cardset="base",
        energy_type="fighting",
        evolution_level="basic",
        hp=40,
        attack_cost=0,
        attack_dmg=20,
        retreat_cost=0,
        owner=player1,
    )
    geodude.attack(pikachu1)
    assert pikachu1.hp==0

def test_load_cards_from_file(player1):
    dratini=Pokemon(owner=player1, **cards_data.dratini)
    assert dratini.name=="Dratini"

def test_deck_shuffle(monkeypatch):

    duel_manager=duel.DuelManager(main.phase_handler,prizes=6)
    player1=duel.Player(duel_manager)
    pkmn_card_1=Pokemon(owner=player1,**cards_data.dratini)
    pkmn_card_2=Pokemon(owner=player1,**cards_data.seel)
    pkmn_card_3=Pokemon(owner=player1,**cards_data.machop)
    deck = Deck(owner=player1,cards=[pkmn_card_1, pkmn_card_2, pkmn_card_3])
    original_order = list(deck.cards)
    monkeypatch.setattr(random, 'shuffle', lambda x: x.reverse())
    deck.shuffle()

    assert deck.cards != original_order
    assert deck.cards == list(reversed(original_order))


def test_integration_testing_from_start_to_coin_flip():
    '''
    load player1 deck: Seel (60 hp, 10 dmg, weak to lightning) x2, energy x8
    load player2 deck: Voltorb (40 hp, 10 dmg) x2, energy x8
    Both players draw their hand of 2 cards.
    Both players put down both their pokemon.
    Coin flip to see who goes first.
'''
    duel_manager=duel.DuelManager(main.phase_handler,prizes=1)
    player1=duel.Player(duel_manager)
    player2=duel.Player(duel_manager)
    for i in range(2):
        move_cards_to_from(Pokemon(owner=player1,**cards_data.seel),player1.deck)
    for i in range(8):
        move_cards_to_from(Energy("water energy", "base", player1),player1.deck)
    for i in range(2):
        move_cards_to_from(Pokemon(owner=player2,**cards_data.voltorb),player2.deck)
    for i in range(8):
        move_cards_to_from(Energy("lightning energy", "base", player2),player2.deck)
    
    assert len(player1.deck)==10
    assert len(player2.deck)==10
    assert player1.deck.cards[0].name=="Seel"
    assert player2.deck.cards[0].name=="Voltorb"
    move_cards_to_from(player1.deck.cards[0:2],player1.hand, player1.deck)
    move_cards_to_from(player2.deck.cards[0:2],player2.hand, player2.deck)    
    assert len(player1.deck)==8
    assert len(player2.deck)==8
    assert player1.deck.cards[0].name=="water energy"
    assert player2.deck.cards[0].name=="lightning energy"
    assert player1.hand.cards[0].name=="Seel"
    assert player2.hand.cards[0].name=="Voltorb"
    move_cards_to_from(player1.hand[0],player1.active,player1.hand)
    move_cards_to_from(player1.hand[0],player1.bench,player1.hand)
    move_cards_to_from(player2.hand[0],player2.active,player1.hand)
    move_cards_to_from(player2.hand[0],player2.bench,player1.hand)
    assert len(player1.active.cards)==1
    assert len(player2.active.cards)==1
    assert len(player1.bench.cards)==1
    assert len(player2.bench.cards)==1
    assert player1.active.cards[0].name=="Seel"
    assert player2.active.cards[0].name=="Voltorb"
    assert player1.bench.cards[0].name=="Seel"
    assert player2.bench.cards[0].name=="Voltorb"
    fake_coin_flip=True
    duel_manager.user_won_starting_coin(fake_coin_flip)
    assert duel_manager.turn=="player"

def test_changing_turns_before_coinflip_returns_error():
    pass

#test decking out