import pytest
from card_deck_classes import *

import duel

@pytest.fixture
def player1():
    return(Player(6))

@pytest.fixture
def player2():
    return(Player(6))

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
    
    
'''
def test_prize_card_win():
    
def test_negative_prize_cards():'''