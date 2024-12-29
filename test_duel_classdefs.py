import pytest
import duel_classdefs as cd
import main
import random
import cards
import menu
import decks


@pytest.fixture
def player1():
    duel_manager=cd.DuelManager(main.phase_handler,prizes=6)
    return(cd.Player(duel_manager))

@pytest.fixture
def player2():
    duel_manager=cd.DuelManager(main.phase_handler,prizes=6)
    return(cd.Player(duel_manager))

@pytest.fixture
def pikachu1(player1):
    pikachu = cd.Pokemon(
        name="Pikachu",
        cardset="base",
        level_id=99,
        energy_type="electric",
        evolution_level="basic",
        hp=40,
        attacks=[{"name":"Zippyzap","cost":"","damage":10}],
        retreat_cost=0,
        owner=player1,
        weakness="fighting",
        card_type="pokemon",
    ) 
    return(pikachu)

@pytest.fixture    
def pikachu2(player2):
    pikachu = cd.Pokemon(
        name="Pikachu",
        cardset="base",
        level_id=99,
        energy_type="electric",
        evolution_level="basic",
        hp=40,
        attacks=[{"name":"Zippyzap","cost":"","damage":10}],
        retreat_cost=0,
        owner=player2,
        weakness="fighting",
        card_type="pokemon",
    ) 
    return(pikachu)

@pytest.fixture    
def raichu1(player1):
    raichu = cd.Pokemon(
        name="Raichu",
        cardset="base",
        level_id=99,
        energy_type="electric",
        evolution_level="stage 1",
        hp=60,
        attacks=[{"name":"Big Zippyzap","cost":"L","damage":20}],
        retreat_cost=1,
        owner=player1,
        evolves_from="Pikachu",
        weakness="fighting",
        card_type="pokemon",
    ) 
    return(raichu)

@pytest.fixture
def setup_duel():
    duel_manager = cd.DuelManager(main.phase_handler)
    player1 = cd.Player(duel_manager)
    player2 = cd.Player(duel_manager)
    deck_objects1=decks.generate([[cards.dratini,1],[cards.hitmonchan,1],[cards.seel,1],[cards.machop,1],[cards.water,7]],player1)
    deck_objects2=decks.generate([[cards.dratini,1],[cards.hitmonchan,1],[cards.seel,1],[cards.machop,1],[cards.water,7]],player2)
    cd.move_cards_to_from(deck_objects1,player1.deck)
    cd.move_cards_to_from(deck_objects2,player2.deck)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.active)
    cd.move_cards_to_from(cd.Pokemon(owner=player2,**cards.seel),player2.active)
    player1.prizes.place()
    player2.prizes.place()
    return duel_manager, player1, player2


def test_one_active_pokemon(player1, pikachu1):
    active=cd.CardCollection(player1, pikachu1)
    assert pikachu1 in active

def test_two_active_pokemon(player1, player2, pikachu1,pikachu2):
    active1=cd.CardCollection(player1, pikachu1)
    active2=cd.CardCollection(player2, pikachu2)
    assert pikachu1 in active1
    assert pikachu2 in active2

def test_one_pokemon_attacking_another(pikachu1,pikachu2):
    pikachu1.attack(pikachu2,0)
    assert pikachu2.hp==30

def test_hp_past_max_doesnt_go_negative(pikachu1,pikachu2):
    pikachu1.attacks[0]["damage"]=50
    pikachu1.attack(pikachu2,0)
    assert pikachu2.hp==0

def test_negative_damage(pikachu1,pikachu2):
    pikachu1.attacks[0]["damage"]=-20
    pikachu1.attack(pikachu2,0)
    assert pikachu2.hp==40

def test_KO_removes_one_prize_card(setup_duel):
    duel_manager,player1,player2=setup_duel
    for i in range(6): #6 prizes
        for i in range(6): #60 health, 10 dmg
            player2.active[0].attack(player1.active[0],attack_num=0)
    assert(player2.duel_handler.phase_handler.get_game_phase())=="club"

def test_won_coin_flip_then_two_turns_end(monkeypatch):
    duel_object=cd.DuelManager(main.PhaseHandler(),prizes=6)
    monkeypatch.setattr(random, 'choice', lambda x: 1)
    duel_object.starting_coin()
    assert duel_object.turn=="player"
    duel_object.advance_turn()
    assert duel_object.turn=="computer"
    duel_object.advance_turn()
    assert duel_object.turn=="player"

def test_lost_coin_flip_then_two_turns_end(monkeypatch):
    duel_object=cd.DuelManager(main.PhaseHandler(),prizes=6)
    monkeypatch.setattr(random, 'choice', lambda x: 0)
    duel_object.starting_coin()
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
    new_duel=cd.DuelManager(phase_handler,prizes=6)
    assert phase_handler.get_game_phase()=="duelling"

def test_ending_duel_phase():
    phase_handler = main.PhaseHandler()
    new_duel=cd.DuelManager(phase_handler,prizes=6)
    new_duel.end_duel()
    assert phase_handler.get_game_phase()=="club"

def test_new_game_phases_per_test():
    phase_handler = main.PhaseHandler()
    assert phase_handler.get_game_phase()=="starting"
    
def test_ko_with_1_prize_remaining_ends_duel(setup_duel):
    duel_manager,player1,player2=setup_duel
    for i in range(6): #6 prizes
        for i in range(6): #60 health, 10 dmg
            player2.active[0].attack(player1.active[0],attack_num=0)
    assert(player2.duel_handler.phase_handler.get_game_phase())=="club"

def test_attach_energy_to_pokemon(player1,pikachu1):
    water_energy=cd.Energy("water", "basic energy", "energy", player1)
    pikachu1.attach_card(water_energy)
    assert water_energy in pikachu1.attached

def test_moving_water_deck_hand_discard(player1):
    deck=cd.CardCollection(player1)
    hand=cd.CardCollection(player1)
    discard_pile=cd.CardCollection(player1)
    water_energy=cd.Energy("water", "basic energy","energy", player1)
    cd.move_cards_to_from(water_energy, deck)
    assert water_energy in deck
    cd.move_cards_to_from(water_energy, hand, deck)
    assert water_energy in hand
    assert water_energy not in deck
    cd.move_cards_to_from(water_energy, discard_pile, hand)
    assert water_energy in discard_pile
    assert water_energy not in hand
    

def test_moving_pikachu_deck_hand_bench_active(pikachu1,player1):
    deck=cd.CardCollection(player1)
    hand=cd.CardCollection(player1)
    active=cd.CardCollection(player1)
    bench=cd.CardCollection(player1)
    cd.move_cards_to_from(pikachu1, deck)
    assert pikachu1 in deck
    cd.move_cards_to_from(pikachu1,hand, deck)
    assert pikachu1 in hand
    assert pikachu1 not in deck
    cd.move_cards_to_from(pikachu1,active, hand)
    assert pikachu1 in active
    assert pikachu1 not in hand
    cd.move_cards_to_from(pikachu1,bench, active)
    assert pikachu1 in bench
    assert pikachu1 not in active

def test_evolve_pikachu(player1, pikachu1, raichu1):
    active=cd.CardCollection(player1)
    cd.move_cards_to_from(pikachu1,active)
    pikachu1.evolve(raichu1,active)
    assert raichu1 in active
    assert pikachu1 not in active
    assert pikachu1 in raichu1.stored_pre_evolution

def test_costless_retreat_pikachu(pikachu1, raichu1):
    active=cd.CardCollection(player1)
    bench=cd.CardCollection(player1)
    cd.move_cards_to_from(pikachu1,active)
    cd.move_cards_to_from(raichu1,bench)
    assert pikachu1 in active
    assert raichu1 in bench
    cd.move_cards_to_from(pikachu1,bench,active)
    cd.move_cards_to_from(raichu1,active,bench)
    assert pikachu1 in bench
    assert raichu1 in active

def test_add_multiple_cards(pikachu1,raichu1):
    hand=cd.CardCollection(player1)
    cd.move_cards_to_from([pikachu1,raichu1],hand)
    assert pikachu1 in hand
    assert raichu1 in hand
    
def test_weakness(pikachu1,player1):
    geodude = cd.Pokemon(
        name="Geodude",
        cardset="base",
        level_id=999,
        energy_type="fighting",
        evolution_level="basic",
        hp=40,
        attacks=[{"name":"Rock Toss","cost":"","damage":20}],
        retreat_cost=0,
        owner=player1,
        card_type="pokemon",
    )
    geodude.attack(pikachu1,0)
    assert pikachu1.hp==0

def test_load_cards_from_file(player1):
    dratini=cd.Pokemon(owner=player1, **cards.dratini)
    assert dratini.name=="Dratini"

def test_deck_shuffle(monkeypatch):

    duel_manager=cd.DuelManager(main.phase_handler,prizes=6)
    player1=cd.Player(duel_manager)
    pkmn_card_1=cd.Pokemon(owner=player1,**cards.dratini)
    pkmn_card_2=cd.Pokemon(owner=player1,**cards.seel)
    pkmn_card_3=cd.Pokemon(owner=player1,**cards.machop)
    deck = cd.CardCollection(owner=player1,cards=[pkmn_card_1, pkmn_card_2, pkmn_card_3])
    original_order = list(deck.cards)
    monkeypatch.setattr(random, 'shuffle', lambda x: x.reverse())
    random.shuffle(deck.cards)

    assert deck.cards != original_order
    assert deck.cards == list(reversed(original_order))


def test_integration_testing_from_start_to_coin_flip(monkeypatch):
    '''
    load player1 deck: Seel (60 hp, 10 dmg, weak to lightning) x2, energy x8
    load player2 deck: Voltorb (40 hp, 10 dmg) x2, energy x8
    Both players draw their hand of 2 cards.
    Both players put down both their pokemon.
    Coin flip to see who goes first.
'''
    duel_manager=cd.DuelManager(main.phase_handler,prizes=1)
    player1=cd.Player(duel_manager)
    player2=cd.Player(duel_manager)
    for i in range(2):
        cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.seel),player1.deck)
    for i in range(8):
        cd.move_cards_to_from(cd.Energy("water energy", "base","energy", player1),player1.deck)
    for i in range(2):
        cd.move_cards_to_from(cd.Pokemon(owner=player2,**cards.voltorb),player2.deck)
    for i in range(8):
        cd.move_cards_to_from(cd.Energy("lightning energy", "base","energy", player2),player2.deck)
    
    assert len(player1.deck)==10
    assert len(player2.deck)==10
    assert player1.deck.cards[0].name=="Seel"
    assert player2.deck.cards[0].name=="Voltorb"
    cd.move_cards_to_from(player1.deck.cards[0:2],player1.hand, player1.deck)
    cd.move_cards_to_from(player2.deck.cards[0:2],player2.hand, player2.deck)    
    assert len(player1.deck)==8
    assert len(player2.deck)==8
    assert player1.deck.cards[0].name=="water energy"
    assert player2.deck.cards[0].name=="lightning energy"
    assert player1.hand.cards[0].name=="Seel"
    assert player2.hand.cards[0].name=="Voltorb"
    cd.move_cards_to_from(player1.hand[0],player1.active,player1.hand)
    cd.move_cards_to_from(player1.hand[0],player1.bench,player1.hand)
    cd.move_cards_to_from(player2.hand[0],player2.active,player1.hand)
    cd.move_cards_to_from(player2.hand[0],player2.bench,player1.hand)
    assert len(player1.active.cards)==1
    assert len(player2.active.cards)==1
    assert len(player1.bench.cards)==1
    assert len(player2.bench.cards)==1
    assert player1.active.cards[0].name=="Seel"
    assert player2.active.cards[0].name=="Voltorb"
    assert player1.bench.cards[0].name=="Seel"
    assert player2.bench.cards[0].name=="Voltorb"
    monkeypatch.setattr(random, 'choice', lambda x: 1)
    duel_manager.starting_coin()
    assert duel_manager.turn=="player"

def test_attacking_with_secondary_attack():
    duel_manager = cd.DuelManager(main.phase_handler, prizes=1)
    player1 = cd.Player(duel_manager)
    player2 = cd.Player(duel_manager)
    cd.move_cards_to_from(cd.Pokemon(owner=player1,**cards.hitmonchan),player1.active)
    cd.move_cards_to_from(cd.Pokemon(owner=player2,**cards.hitmonchan),player2.active)
    player1.active[0].attack(player2.active[0],1)
    assert player2.active[0].hp==30

def test_initial_draw(monkeypatch):
    duel_manager = cd.DuelManager(main.phase_handler, prizes=1)
    player1 = cd.Player(duel_manager)
    monkeypatch.setattr(random, 'shuffle', lambda x: x.reverse())
    player1.deck.cards=decks.generate([[cards.dratini,1],[cards.hitmonchan,1],[cards.seel,1],[cards.machop,1],[cards.water,7]],player1)
    player1.initial_draw()
    assert player1.hand[0].name=="Dratini"
    assert len(player1.deck)==4
    assert len(player1.hand)==7

def test_prizes_setup(setup_duel):
    duel_manager, player1, player2=setup_duel
    assert len(player1.prizes)==6


