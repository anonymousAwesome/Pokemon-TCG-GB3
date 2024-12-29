import cards
import duel_classdefs as cd

def generate(deck,owner):
    '''
    takes a list of 2-item lists, each containing a card dictionary and
    a quantity, and returns a list of card objects'''
    tempdeck=[]

    for pair_list in deck:
        card=pair_list[0]
        for i in range(pair_list[1]):
            if card["card_type"]=="pokemon":
                tempdeck.append(cd.Pokemon(owner=owner,**card))
            elif card["card_type"]=="trainer":
                tempdeck.append(cd.Trainer(owner=owner,**card))
            elif card["card_type"]=="energy":
                tempdeck.append(cd.Energy(owner=owner,**card))
    return(tempdeck)
    

seel1x_energy1x=[[cards.seel,1], [cards.water,1]]

seel4x_energy10x=[[cards.seel,4], [cards.water,10]]
