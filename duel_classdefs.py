import logging
import random
import effects
import main

class DuelManager:
    def __init__(self,prizes=6):
        self.prizes=prizes
        main.phase_handler.set_game_phase("duelling")
        self.turn=None

    def starting_coin(self):
        if random.choice([0,1]):
            self.turn="player"
        else:
            self.turn="computer"
        #else:logging.error(f"Unexpected value in DuelManager.__init__() -- expected boolean for user_won_starting_coin, got {user_won_starting_coin}")
      
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
        main.phase_handler.set_game_phase("club")



class Card:
    def __init__(self, name,cardset,card_type):
        self.name = name
        self.cardset=cardset
        self.card_type=card_type

    def __str__(self):
        return (f"{self.name}, {self.cardset} set")

''' At some point I think I'm likely to need a function that will check 
to see if a card is in any CardCollections.'''

class Trainer(Card):
    def __init__(self, name, cardset, card_type):
        super().__init__(name, cardset, card_type)

class Energy(Card):
    def __init__(self, name, cardset, card_type):
        super().__init__(name, cardset, card_type)

class Pokemon(Card):
    def __init__(self, name, cardset, card_type, energy_type, evolution_level, hp, attacks, retreat_cost, level_id=None, weakness=None, resistance=None,evolves_from=None):
        super().__init__(name,cardset, card_type)
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
        self.attached=CardCollection()
        self.type="pokemon"

        self.stored_pre_evolution=CardCollection()

        self.temp_dmg=None

    def __str__(self):
        return (f"{self.name}, {self.cardset} set, lv. {self.level_id}")

    def attack(self, owner, opponent, attack_id):
        '''
        Need a better way of ordering the effects. 
        For example, the order should go "weakness, resistance, pluspower".
        '''
        self.temp_dmg=self.attacks[attack_id]["damage"]
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
            owner.take_prize()

    def attach_card(self,card):
        move_cards_to_from(card, self.attached)
        #may need an extra function to return just the energy cards
    
    def evolve(self, evolution_card,location):
        move_cards_to_from(self,evolution_card.stored_pre_evolution,location)
        move_cards_to_from(evolution_card,location)

class CardCollection:
    def __init__(self, cards=None):
        if cards is None:
            self.cards=[]
        elif isinstance(cards, Card):
            self.cards=[cards]
        elif isinstance(cards, list):
            self.cards=cards
        else:
            logging.error(f"Expected card or list of cards, got {cards}")

    def __str__(self):
        temp_list=[]
        for card in self.cards:
            temp_list.append(card.name)
        return (f"{temp_list}")

    def __contains__(self, item):
        return item in self.cards

    def __iter__(self):
        #allows iteration: for card in cardcollection
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

class Prizes(CardCollection):
    def __init__(self, cards=None):
        super().__init__(cards=None)


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
        self.prizes=Prizes()
        self.deck=CardCollection()
        self.active=CardCollection()
        self.bench=CardCollection()
        self.hand=CardCollection()
        self.discard_pile=CardCollection()
        self.choices={}

    def initial_draw(self):
        no_basics=True
        random.shuffle(self.deck.cards)
        while no_basics:
            for card in self.deck[0:6]:
                if getattr(card, 'evolution_level', False):
                    if card.evolution_level=="basic":
                        no_basics=False
            if no_basics:
                random.shuffle(self.deck.cards)
                print("No basics in your hand. Shuffling.")
        move_cards_to_from(self.deck[0:7],self.hand,self.deck)

    def place_prizes(self):
        move_cards_to_from(self.deck[0:self.duel_handler.prizes],self.prizes,self.deck)        

    def take_prize(self):
        if self.prizes:
            move_cards_to_from(self.prizes[-1],self.hand,self.prizes)
            if len(self.prizes)<=0:
                self.duel_handler.end_duel()
    
