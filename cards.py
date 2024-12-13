'''
copy-paste template:
={
        "name":"",
        "cardset":"base",
        "level_id":,
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

'''
C = COLORLESS,
R = FIRE,
F = FIGHTING,
G = GRASS,
W = WATER,
P = PSYCHIC,
L = LIGHTNING,
M = METAL,
D = DARKNESS,
'''


dratini={
        "name":"Dratini",
        "cardset":"base",
        "level_id": 10,
        "energy_type":"c",
        "evolution_level":"basic",
        "hp":40,
        "attacks":[{"name":"Pound","cost":"c","damage":10}],
        "retreat_cost":1,
        "resistance":"p"}

seel={
        "name":"Seel",
        "cardset":"base",
        "level_id": 12,
        "energy_type":"w",
        "evolution_level":"basic",
        "hp":60,
        "attacks":[{"name":"Headbutt","cost":"w","damage":10}],
        "retreat_cost":1,
        "weakness":"l",
        }

machop={
        "name":"Machop",
        "cardset":"base",
        "level_id": 20,
        "energy_type":"f",
        "evolution_level":"basic",
        "hp":50,
        "attacks":[{"name":"Low Kick","cost":"f","damage":10}],
        "retreat_cost":1,
        "weakness":"p",
        }

voltorb={
        "name":"Voltorb",
        "cardset":"base",
        "level_id": 10,
        "energy_type":"l",
        "evolution_level":"basic",
        "hp":40,
        "attacks":[{"name":"Tackle","cost":"c","damage":10}],
        "retreat_cost":1,
        "weakness":"f",
        }
hitmonchan={
        "name":"Hitmonchan",
        "cardset":"base",
        "level_id": 33,
        "energy_type":"f",
        "evolution_level":"basic",
        "hp":70,
        "attacks":[{"name":"Jab","cost":"f","damage":20},{"name":"Special Punch","cost":"ffc","damage":40}],
        "retreat_cost":1,
        "weakness":"p",
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