import pytest
from card_deck_classes import *

import duel
import main

@pytest.fixture
def player1():
    return(duel.Player(duel.Duel(main.phase_handler,True),6))

@pytest.fixture
def player2():
    return(duel.Player(duel.Duel(main.phase_handler,True),6))

@pytest.fixture
def pikachu1(player1):
    player=player1
    return(Card(name="Pikachu",hp=40,owner=player))

@pytest.fixture    
def pikachu2(player2):
    player=player2
    return(Card(name="Pikachu",hp=40,owner=player))

def test_one_active_pokemon(pikachu1):
    active=CardCollection(pikachu1)
    assert pikachu1 in active

def test_two_active_pokemon(pikachu1,pikachu2):
    active1=CardCollection(pikachu1)
    active2=CardCollection(pikachu2)
    assert pikachu1 in active1
    assert pikachu2 in active2

def test_one_pokemon_attacking_another(pikachu1,pikachu2):
    pikachu1.attack(pikachu2,10)
    assert pikachu2.hp==30

def test_hp_past_max_doesnt_go_negative(pikachu1,pikachu2):
    pikachu1.attack(pikachu2,50)
    assert pikachu2.hp==0
    
def test_negative_damage(pikachu1,pikachu2):
    pikachu1.attack(pikachu2,-20)
    assert pikachu2.hp==40

def test_KO_removes_one_prize_card(pikachu1,pikachu2):
    pikachu1.attack(pikachu2,50)
    assert pikachu1.owner.prizes==5

def test_won_coin_flip_then_two_turns_end():
    duel_object=duel.Duel(main.PhaseHandler(),True)
    assert duel_object.turn=="player"
    duel_object.advance_turn()
    assert duel_object.turn=="computer"
    duel_object.advance_turn()
    assert duel_object.turn=="player"

def test_lost_coin_flip_then_two_turns_end():
    duel_object=duel.Duel(main.PhaseHandler(),False)
    assert duel_object.turn=="computer"
    duel_object.advance_turn()
    assert duel_object.turn=="player"
    duel_object.advance_turn()
    assert duel_object.turn=="computer"

def test_starting_phase():
    phase_handler = main.PhaseHandler()
    assert phase_handler.get_game_phase()=="starting"

def test_starting_duel_phase():
    phase_handler = main.PhaseHandler()
    new_duel=duel.Duel(phase_handler,True)
    assert phase_handler.get_game_phase()=="duelling"

def test_ending_duel_phase():
    phase_handler = main.PhaseHandler()
    new_duel=duel.Duel(phase_handler,True)
    new_duel.end_duel()
    assert phase_handler.get_game_phase()=="club"

def test_new_game_phases_per_test():
    phase_handler = main.PhaseHandler()
    assert phase_handler.get_game_phase()=="starting"
    
def test_ko_with_1_prize_remaining_ends_duel():
    phase_handler = main.PhaseHandler()
    player1=duel.Player(duel.Duel(phase_handler,True),6)
    player2=duel.Player(duel.Duel(phase_handler,True),1)
    pikachu1=Card(name="Pikachu",hp=40,owner=player1)
    pikachu2=Card(name="Pikachu",hp=40,owner=player2)
    pikachu2.attack(pikachu1,50)
    assert phase_handler.get_game_phase()=="club"
