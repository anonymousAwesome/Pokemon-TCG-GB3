import pytest
import duel_classdefs as cd
import main
import menu
import cards

@pytest.fixture
def player1():
    duel_manager = cd.DuelManager(prizes=6)
    player1 = cd.Player(duel_manager)
    return player1

@pytest.fixture
def player2():
    duel_manager = cd.DuelManager(prizes=6)
    player2 = cd.Player(duel_manager)
    return player2

@pytest.fixture
def setup_duel(player1, player2):
    duel_manager = cd.DuelManager(prizes=6)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.active)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player2.active)
    return duel_manager, player1, player2

def test_menu_manager_initialization(player1):
    manager = menu.Main(player1)
    assert manager.navigation.menu_stack == ["starting"]

def test_add_submenu(player1):
    manager = menu.Main(player1)
    manager.navigation.menu_stack.append("Options")
    assert manager.navigation.menu_stack == ["starting", "Options"]



def test_initial_menu_options(player1, monkeypatch,capsys):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu=menu.Main(player1)
    duel_menu.run_menu()
    captured=capsys.readouterr()
    assert captured.out=="""0: Hand
1: Game board
2: Retreat
3: Attack
4: Pokemon power
5: End turn
6: Resign
"""

def test_dratini_option(setup_duel, player1,monkeypatch,capsys):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.Main(player1)
    cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.hand)
    with capsys.disabled():
        duel_menu.run_menu()
    duel_menu.run_menu()
    captured=capsys.readouterr()
    assert captured.out=="""0: Dratini, base set, lv. 10
1: Cancel
"""

def test_look_at_dratini(setup_duel, player1,monkeypatch,capsys):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.Main(player1)
    cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.hand)
    with capsys.disabled():
        duel_menu.run_menu()
        duel_menu.run_menu()
    duel_menu.run_menu()
    captured=capsys.readouterr()
    assert captured.out=="""0: Check information
1: Play it
2: Cancel
Name: Dratini
"""

def test_play_dratini(setup_duel, player1,monkeypatch):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.Main(player1)
    cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.hand)
    duel_menu.run_menu()
    duel_menu.run_menu()
    def fake_input(prompt=None):
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.run_menu()
    assert player1.bench[0].name=="Dratini"

def test_play_dratini_with_full_bench(setup_duel, monkeypatch):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.Main(player1)
    hand=cd.CardCollection()
    cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.hand)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(**cards.seel),player1.bench)
    assert len(player1.bench)==5
    duel_menu.run_menu()
    duel_menu.run_menu()
    def fake_input(prompt=None):
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.run_menu()
    assert len(player1.bench)==5
    assert player1.hand[0].name=="Dratini"


def test_play_energy_on_dratini(setup_duel, monkeypatch):
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.Main(player1)
    cd.move_cards_to_from(cd.Pokemon(**cards.dratini),player1.active)
    cd.move_cards_to_from(cd.Energy("water", cardset="basic energy", card_type="energy"),player1.hand)
    duel_menu.run_menu()
    duel_menu.run_menu()
    def fake_input(prompt=None):
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.run_menu()
    def fake_input(prompt=None):
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.run_menu()
    assert player1.active[0].attached.cards[0].name=="water"

'''    
def test_play_defender_card_on_dratini(setup_duel, monkeypatch):
    pass

def test_defender_effect(setup_duel, monkeypatch):
    pass

def test_bill(setup_duel, monkeypatch):
    pass
    
    '''