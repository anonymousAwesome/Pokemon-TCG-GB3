import mapinfo
import map_helpers
import characters

empty_event=map_helpers.EmptyEvent(0)



def opening_cutscene_events(inner_context):
    text_list=[f"""{inner_context.player_data.player_name} is just crazy about card collecting and duelling! They faced each club leader on TCG Island and defeated the Grand Masters, obtaining the Legendary Pokemon cards. But then, disaster struck! Team Great Rocket stole everybody's cards and took over TCG Island! After duelling their way through the ranks, {inner_context.player_data.player_name} defeated their leader, King Villicci, causing him to have a change of heart and give up his evil ways. Peace returned to TCG Island.""",
    """Until one day...""",
    "Report!",
    "We've dueled them all into submission with a children's card game, as you ordered.",
    "Excellent! Any word on the Pokemon-ex cards?",
    "No, ma'am.",
    "Well, find them! They have to be SOMEWHERE on this stupid island!",
    "So... why are we constantly walking in place?",
    "Boss said it's to fit in with the locals.",
    "That's gonna be exhausting.",
    "Tell me about it. My hammies are already killing me.",
    "...huh.",
    "Are they okay?",
    "Yeah, they're fine. They just couldn't handle the shock of losing. They'll be up again in a few minutes.",
    "Excellent. Just in time for the protagonist to show up.",
    "...",
    "You play too many video games.",
    "What? It could happen! You don't know!",
    f"Ah, good, you're here! {inner_context.player_data.player_name}, I'm afraid we have something of a situation. Hooligans from a criminal organization have taken over the card clubs here on TCG Island!",
    "What do you mean, 'Again?'",
    "They call themselves the Forbidden Faction, and they use powerful forbidden cards in their decks. Since you did such a good job defeating Team Great Rocket the last time this happened, I thought you would be the perfect person to take care of this problem!",
    "Now, which deck did you bring to TCG Island?",
    """> The Ferocious Charizard Deck
> The Mighty Venusaur Deck
> The Unstoppable Blastoise Deck""",
    "...what do you mean, 'you can't find your deck'? Oh, dear. Well... help yourself to anything in the desk drawer. It's not much, but it's better than nothing.",
    "Player obtained the crappy starter deck!",
    "The printers refuse to make any cards while there is terrorist activity on the island, so we're stuck handing out old booster packs that... well, they're not great. If you want access to better cards, you'll need to drive the Forbidden Faction off of TCG Island first.",
    "Now, go! Defeat duelists, get better cards, and show those Forbidden Faction rapscallions what for!"
    ]

    malinda_image=characters.load_portrait_from_sheet_GB3(0,0)
    grass_image=characters.load_portrait_from_sheet_GB3(3,0)
    lightning_image=characters.load_portrait_from_sheet_GB3(2,0)
    mason_image=characters.load_portrait_from_sheet(characters.portrait_sheet_GB2,2,0)

    inner_context.event_manager.add_event(inner_context.player_character.toggle_visibility)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[0]])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[1]])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,mapinfo.CutsceneFfEntrance])
    inner_context.event_manager.add_event(inner_context.disable_prevent_step_trigger)
    inner_context.prevent_step_trigger = True
    inner_context.map_input_lock.lock()

    temp=map_helpers.FFCutsceneHelpers(inner_context)
    inner_context.event_manager.add_event(temp.group_move,[inner_context,3],persistent_condition=temp.check_bottom,condition_kwargs={"y_coord":960})

    inner_context.event_manager.add_event(empty_event.__init__,[60])
    inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)

    inner_context.event_manager.add_event(temp.group_move,[inner_context,8],persistent_condition=temp.check_bottom,condition_kwargs={"y_coord":1600})
    
    inner_context.event_manager.add_event(empty_event.__init__,[60])
    inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)
    
    inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,mapinfo.CutsceneWaterClub])
    
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[2],"Malinda",malinda_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[3],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[4],"Malinda",malinda_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[5],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[6],"Malinda",malinda_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[7],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[8],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[9],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[10],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[11],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[12],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[13],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[14],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[15],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[16],"FF Grass",grass_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[17],"FF Lightning",lightning_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,mapinfo.TcgIsland])

    inner_context.event_manager.add_event(inner_context.player_character.change_location,[64*5,64*7,"down"])

    inner_context.event_manager.add_event(inner_context.player_character.toggle_visibility)    
    
    inner_context.event_manager.add_event(empty_event.__init__,[15])
    inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)
    
    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["left"])
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)

    inner_context.event_manager.add_event(empty_event.__init__,[15])
    inner_context.event_manager.add_event(empty_event.decrement_loops,persistent_condition=empty_event.check_still_looping)
    
    inner_context.event_manager.add_event(map_helpers.reload_map,[inner_context,mapinfo.MasonCenter])
    inner_context.event_manager.add_event(inner_context.player_character.change_location,[64*7,64*13,"up"])
    
    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["up"])
    for i in range(9):
        inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)    

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[18],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[19],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[20],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[21],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[22]])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[23],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)


    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["left"])
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)



    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["up"])
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[24]])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    

    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["down"])
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)

    inner_context.event_manager.add_event(inner_context.player_character.cutscene_walk,["right"])
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
    inner_context.event_manager.add_event(inner_context.player_character.move_character, [4], persistent_condition=inner_context.player_character.still_walking)
  
    #to-do: make Mason turn left.
    
    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[25],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)

    inner_context.event_manager.add_event(inner_context.current_dialogue.__init__,[inner_context.screen,text_list[26],"Doctor Mason",mason_image])
    inner_context.event_manager.add_event(inner_context.current_dialogue.render,[inner_context.event_list],persistent_condition=inner_context.current_dialogue.check_remaining_text)
    
    
    
    inner_context.event_manager.add_event(inner_context.map_input_lock.unlock)
    #inner_context.event_manager.add_event(inner_context.disable_prevent_step_trigger)
    

    inner_context.map_input_lock.lock()


'''
Malinda enters the club from offscreen and stands in front of FF1, one tile below him.

Malinda: "Report!"

FF cultist: "We've dueled them all into submission with a children's card game, as you ordered."

Malinda: "Excellent! Any word on the Pokemon-ex cards?"

FF Grass: No, ma'am.

"Well, find them! They have to be SOMEWHERE on this stupid island!"

Malinda leaves.

FF Lightning walks on-screen from the top, standing one tile up and right of FF Grass.

FF Lightning: So... why are we constantly walking in place?

FF Grass: Boss said it's to fit in with the locals.

FF Lightning: That's gonna be exhausting.

FF Grass: Tell me about it. My hammies are already killing me.

FF Lightning: [Looks left, then right, then forward again. The fallen NPCs should be three tiles left and two tiles right of him.]

FF Lightning: ...huh.

FF Lightning: Are they okay?

FF Grass: Yeah, they're fine. They just couldn't handle the shock of losing. They'll be up again in a few minutes.

FF Lightning: Excellent. Just in time for the protagonist to show up.

FF Grass: ...

FF Grass: You play too many video games.

FF Lightning: What? It could happen! You don't know!

change scene to Tcg Island, and make an airplane land on the airport and disappear, then
the player appears and walks from the airport to Mason's lab.

change scene to Mason's Lab, where the player walks forward until they reach the Professor.

'''