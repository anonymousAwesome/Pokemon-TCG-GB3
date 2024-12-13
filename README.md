#Pokemon TCG GB3: Rise of the Forbidden Faction

This program is a fangame sequel to the Pokemon TCG games for the Game Boy Color. The player explores the game world, defeats duellists in a card game, and collects cards to improve their deck.

The program uses the Pygame module for gameplay and pygbag to export the game to HTML5 for browser play.

##Planned features:

* Every card from Base to Neo expansions, plus Japanese-only cards that never got an official English release. That's roughly a thousand cards.

* Over 64 trainers, each with their own unique deck.

* Two maps: TCG Island and Neo Continent, each containing their own card clubs and rewarding the player with different cards.

* A villainous organization, the Forbidden Faction, who use powerful forbidden cards.

* Duellists offer optional challenges once you defeat them the first time, adding deck restrictions or altering the rules of the duel, in exchange for an extra booster pack if you win.

##Current status:

(All percentages are approximate.)

Cards: 5/~1000 done  
Duelling system: 5% done  
Duelling layout: 50% done  
NPC sprites and portraits: 6% done (each sprite and each portrait is roughly 1%)  
NPC/player interactions: 0% done  
New location designs: 3/15 done (8 clubs, hidden basement (2 rooms), FF headquarters (2.5 rooms), Neo Continent Grand Master Stadium, Neo Continent overworld, and 0.5 airport)  
Menu, GUI, and displaying text: 5% done  
NPC duel AI: 0% done  
NPC decks: 0% done  
NPC dialogue: 75% done  
Music and sounds: 10% done  
Save/load: 0% done  
Cutscene system: 0% done

This repo also contains the `obstacle generator.py` Python script, a tool to generate rects for tile collision directly on the loaded image. More information about that can be found at the beginning of that file.