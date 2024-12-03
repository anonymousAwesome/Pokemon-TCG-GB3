'''
Contains the definitions for cards and decks
'''



class Card:
    def __init__(self, name,cardset,owner):
        self.name = name
        self.cardset=cardset
        self.owner=owner

''' At some point I think I'm likely to need a function that will check 
to see if a card is in any CardCollections.'''

class Trainer(Card):
    def __init__(self, name, cardset, owner):
        super().__init__(name, cardset, owner)

class Energy(Card):
    def __init__(self, name, cardset, owner):
        super().__init__(name, cardset, owner)

class Pokemon(Card):
    def __init__(self, name, cardset, owner, energy_type, evolution_level, hp, attack_dmg, retreat_cost,evolves_from=None):
        super().__init__(name,cardset, owner)
        self.energy_type=energy_type
        self.evolution_level=evolution_level
        self.hp = hp
        self.attack_dmg = attack_dmg
        self.retreat_cost = retreat_cost
        self.evolves_from=evolves_from

        self.attached_energy=CardCollection(owner)

        self.stored_pre_evolution=CardCollection(owner)

    def attack(self, opponent, attack_dmg):
        if attack_dmg<0:
            attack_dmg=0
        opponent.hp-=attack_dmg
        if opponent.hp<=0:
            opponent.hp=0
            self.owner.lose_prize()

    def attach_energy(self,card):
        move_cards_to_from(card, self.attached_energy)
        #may need refactoring when non-energy attachments become a thing
    
    def evolve(self, evolution_card,location):
        move_cards_to_from(self,evolution_card.stored_pre_evolution,location)
        move_cards_to_from(evolution_card,location)

class CardCollection:
    def __init__(self, owner, cards=None):
        self.owner=owner
        if cards is None:
            self.cards = []
        elif isinstance(cards, Card):
            self.cards = [cards]
        else:
            self.cards = cards

    def __iter__(self):
        return iter(self.cards)

'''
#currently unused
    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

'''

class Deck(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(cards)

    def shuffle(self):
        random.shuffle(self.cards)

class Active(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(cards)

class Benched(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(cards)

class Hand(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(cards)

class DiscardPile(CardCollection):
    def __init__(self, owner, cards=None):
        super().__init__(cards)


def move_cards_to_from(cardlist, destination_location,prev_location=None):
    if isinstance(cardlist, Card):
        cardlist=[cardlist]
    if isinstance(cardlist, list):
        for card in cardlist:
            destination_location.cards.append(card)
            if prev_location:
                prev_location.cards.remove(card)
    if not isinstance(cardlist, list):
        logging.error(f"Expected card or list of cards, got {cardlist}")