import logging
import main
import random
import effects

class DuelManager:
    def __init__(self,phase_handler,prizes=6):
        self.prizes=prizes
        self.phase_handler=phase_handler
        self.phase_handler.set_game_phase("duelling")
        self.turn=None

    def user_won_starting_coin(self, coin_results:bool):
        if coin_results is True:
            self.turn="player"
        elif coin_results is False:
            self.turn="computer"
        else:logging.error(f"Unexpected value in DuelManager.__init__() -- expected boolean for user_won_starting_coin, got {user_won_starting_coin}")
      
    def advance_turn(self):
        if not self.turn:
            logging.error(f"Can't advance the turns; haven't run user_won_starting_coin() yet.")
        if self.turn=="player":
            self.turn="computer"
        elif self.turn=="computer":
            self.turn="player"
        else:
            logging.error(f"Unexpected value in DuelManager.advance_turn() -- expected \"player\" or \"computer\", got {self.turn}")

    def end_duel(self):
        self.phase_handler.set_game_phase("club")



class Card:
    def __init__(self, name,cardset,card_type,owner):
        self.name = name
        self.cardset=cardset
        self.card_type=card_type
        self.owner=owner

    def __str__(self):
        return (f"{self.name}, {self.cardset} set")

''' At some point I think I'm likely to need a function that will check 
to see if a card is in any CardCollections.'''

class Trainer(Card):
    def __init__(self, name, cardset, card_type, owner):
        super().__init__(name, cardset, card_type,owner)

class Energy(Card):
    def __init__(self, name, cardset, card_type, owner):
        super().__init__(name, cardset, card_type, owner)

class Pokemon(Card):
    def __init__(self, name, cardset, card_type, owner, energy_type, evolution_level, hp, attacks, retreat_cost, level_id=None, weakness=None, resistance=None,evolves_from=None):
        super().__init__(name,cardset, card_type, owner)
        self.energy_type=energy_type
        self.evolution_level=evolution_level
        self.hp = hp
        self.attacks=attacks
        self.retreat_cost = retreat_cost
        self.evolves_from=evolves_from
        self.add_reduce_dmg_effects=[]
        self.other_effects=[]
        self.level_id=level_id
        self.weakness=weakness
        self.resistance=resistance
        if weakness:
            self.other_effects.append(effects.weakness)
        if resistance:
            self.add_reduce_dmg_effects.append(effects.resistance)
        self.attached=CardCollection(owner)
        self.type="pokemon"

        self.stored_pre_evolution=CardCollection(owner)

        self.temp_dmg=None

    def __str__(self):
        return (f"{self.name}, {self.cardset} set, lv. {self.level_id}")

    def attack(self, opponent, attack_num):
        '''
        Need a better way of ordering the effects. 
        For example, the order should go "weakness, resistance, pluspower".
        '''
        self.temp_dmg=self.attacks[attack_num]["damage"]
        for effect in self.add_reduce_dmg_effects:
            effect(self, opponent)
        for effect in opponent.add_reduce_dmg_effects:
            effect(opponent, self)
        if self.temp_dmg<0:
            self.temp_dmg=0
        for effect in self.other_effects:
            effect(self, opponent)
        for effect in opponent.other_effects:
            effect(opponent, self)
        opponent.hp-=self.temp_dmg
        if opponent.hp<=0:
            opponent.hp=0
            self.owner.lose_prize()

    def attach_card(self,card):
        move_cards_to_from(card, self.attached)
        #may need an extra function to return just the energy cards
    
    def evolve(self, evolution_card,location):
        move_cards_to_from(self,evolution_card.stored_pre_evolution,location)
        move_cards_to_from(evolution_card,location)

class CardCollection:
    def __init__(self, owner, cards=None):
        self.owner=owner
        if cards is None:
            self.cards=[]
        elif isinstance(cards, Card):
            self.cards=[cards]
        elif isinstance(cards, list):
            self.cards=cards
        else:
            logging.error(f"Expected card or list of cards, got {cards}")


    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        #allows iteration: for card in cardcollection
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]


def move_cards_to_from(cardlist, destination_location,prev_location=None):
    if isinstance(cardlist, Card):
        cardlist=[cardlist]
    if isinstance(cardlist, list):
        for card in cardlist:
            destination_location.cards.append(card)
            if prev_location:
                prev_location.cards.remove(card)
    else:
        logging.error(f"Expected card or list of cards, got {cardlist}")


class Player:
    def __init__(self,duel_handler):
        self.duel_handler=duel_handler
        self.prizes=duel_handler.prizes
        self.deck=CardCollection(self)
        self.active=CardCollection(self)
        self.bench=CardCollection(self)
        self.hand=CardCollection(self)
        self.discard_pile=CardCollection(self)
        self.choices={}

    def lose_prize(self,quantity=1):
        #outdated, need to refactor
        self.prizes-=quantity
        if self.prizes<=0:
            self.duel_handler.end_duel()
    
