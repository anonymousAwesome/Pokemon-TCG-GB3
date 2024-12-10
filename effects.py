def defender(owning_pokemon, other_pokemon):
    other_pokemon.temp_dmg-=10

def weakness(owning_pokemon, other_pokemon):
    if other_pokemon.energy_type==owning_pokemon.weakness:
        other_pokemon.temp_dmg*=2

def resistance(owning_pokemon, other_pokemon):
    if owning_pokemon.resistance==other_pokemon.energy_type:
        other_pokemon.temp_dmg-=30

def plus_power(owning_pokemon,other_pokemon):
    owning_pokemon.temp_dmg+=10