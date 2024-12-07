from card_deck_classes import *

'''
copy-paste template:
={
        "name":"",
        "cardset":"base",
        "energy_type":"",
        "evolution_level":"basic",
        "hp":,
        "attack_cost":,
        "attack_dmg":,
        "retreat_cost":,
        "weakness":"",
        "resistance":""
        }

'''

dratini={
        "name":"Dratini",
        "cardset":"base",
        "energy_type":"colorless",
        "evolution_level":"basic",
        "hp":40,
        "attack_cost":1,
        "attack_dmg":10,
        "retreat_cost":1,
        "resistance":"psychic"}

seel={
        "name":"Seel",
        "cardset":"base",
        "energy_type":"water",
        "evolution_level":"basic",
        "hp":60,
        "attack_cost":1,
        "attack_dmg":10,
        "retreat_cost":1,
        "weakness":"lightning",
        }

machop={
        "name":"Machop",
        "cardset":"base",
        "energy_type":"fighting",
        "evolution_level":"basic",
        "hp":50,
        "attack_cost":1,
        "attack_dmg":20,
        "retreat_cost":1,
        "weakness":"psychic",
        }

rattata={
        "name":"Rattata",
        "cardset":"base",
        "energy_type":"colorless",
        "evolution_level":"basic",
        "hp":30,
        "attack_cost":1,
        "attack_dmg":20,
        "retreat_cost":0,
        "weakness":"fighting",
        "resistance":"psychic"
        }

staryu={
        "name":"Staryu",
        "cardset":"base",
        "energy_type":"water",
        "evolution_level":"basic",
        "hp":40,
        "attack_cost":1,
        "attack_dmg":20,
        "retreat_cost":1,
        "weakness":"lightning",
        }
        
voltorb={
        "name":"Voltorb",
        "cardset":"base",
        "energy_type":"lightning",
        "evolution_level":"basic",
        "hp":40,
        "attack_cost":1,
        "attack_dmg":10,
        "retreat_cost":1,
        "weakness":"fighting",
        }

"""
Pokemon whose attacks have no special effects, that nonetheless have
multiple attacks and/or inconsistent energy requirements:
https://pkmncards.com/card/growlithe-base-set-bs-28/
https://pkmncards.com/card/hitmonchan-base-set-bs-7/
https://pkmncards.com/card/diglett-base-set-bs-47/
https://pkmncards.com/card/ponyta-base-set-bs-60/
"""

defender={
        "name":"Defender",
        "cardset":"base",
        }