import pytest
import duel_classdefs as cd
import main
import menu
import cards

@pytest.fixture
def player1():
    duel_manager = cd.DuelManager(main.phase_handler, prizes=6)
    player1 = cd.Player(duel_manager)
    return player1

@pytest.fixture
def player2():
    duel_manager = cd.DuelManager(main.phase_handler, prizes=6)
    player2 = cd.Player(duel_manager)
    return player2

@pytest.fixture
def setup_duel(player1, player2):
    duel_manager = cd.DuelManager(main.phase_handler, prizes=6)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.active)
    cd.move_cards_to_from(cd.Pokemon(owner=player2,**cards.seel),player2.active)
    return duel_manager, player1, player2

def test_menu_manager_initialization(player1):
    manager = menu.MenuManager("Main Menu", player1)
    assert manager.menu_stack == ["Main Menu"]

def test_add_submenu(player1):
    manager = menu.MenuManager("Main Menu", player1)
    manager.menu_stack.append("Options")
    assert manager.menu_stack == ["Main Menu", "Options"]



def test_initial_menu_options(player1, monkeypatch,capsys):
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu=menu.MenuManager("starting", player1)
    duel_menu.user_choice()
    captured=capsys.readouterr()
    assert captured.out=="""0: Hand
1: Game board
2: Retreat
3: Attack
4: Pokemon power
5: End turn
6: Resign
"""

def test_check_hand_dratini(setup_duel, monkeypatch,capsys):
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.MenuManager("starting", player1)
    hand=cd.CardCollection(player1)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.dratini),player1.hand)
    duel_menu.user_choice()
    duel_menu.user_choice()
    assert duel_menu.choices[0].name=="Dratini"
    assert duel_menu.choices[1]=="Cancel"
    duel_menu.user_choice()
    assert duel_menu.choices=={0:"Check information", 1: "Play it", 2:"Cancel"}
    captured=capsys.readouterr()
    lines=captured.out.strip().split("\n")
    assert lines[-1]=="Name: Dratini"

def test_play_dratini(setup_duel, monkeypatch):
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.MenuManager("starting", player1)
    hand=cd.CardCollection(player1)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.dratini),player1.hand)
    duel_menu.user_choice()
    duel_menu.user_choice()
    def fake_input():
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.user_choice()
    assert player1.bench[0].name=="Dratini"

def test_play_dratini_with_full_bench(setup_duel, monkeypatch):
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.MenuManager("starting", player1)
    hand=cd.CardCollection(player1)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.dratini),player1.hand)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.bench)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.bench)
    assert len(player1.bench)==5
    duel_menu.user_choice()
    duel_menu.user_choice()
    def fake_input():
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.user_choice()
    assert len(player1.bench)==5
    assert player1.hand[0].name=="Dratini"


def test_play_energy_on_dratini(setup_duel, monkeypatch):
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_manager, player1, player2 = setup_duel
    duel_menu=menu.MenuManager("starting", player1)
    hand=cd.CardCollection(player1)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.dratini),player1.active)
    cd.move_cards_to_from(cd.Energy("water", cardset="basic energy", card_type="energy", owner=player1),player1.hand)
    duel_menu.user_choice()
    duel_menu.user_choice()
    def fake_input():
        return 1
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.user_choice()
    def fake_input():
        return 0
    monkeypatch.setattr('builtins.input', fake_input)
    duel_menu.user_choice()
    assert player1.active[0].attached.cards[0].name=="water"


'''    
def test_play_defender_card_on_dratini(setup_duel, monkeypatch):
    pass

def test_defender_effect(setup_duel, monkeypatch):
    pass

def test_bill(setup_duel, monkeypatch):
    pass
    
    '''