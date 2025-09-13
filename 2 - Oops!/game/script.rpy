# Script for "Oops, a Cannibal Got Your Nose!"

# Colors
define mcColor = "#10c05a"
define cannibalColor = "#da28ad"
define trueCannibalColor = "#fb0064"
define bgCharColor = "#1d53a5"

# Characters used in this game
define narrator = Character(what_italic=True)
define charMC = Character("You", color=mcColor)
define charNotYetCan = Character("Ash", color=cannibalColor)
define charCan = Character("Ash, the Cannibal", color=trueCannibalColor)
define charDad = Character("Dad", color=bgCharColor)
define charMom = Character("Mom", color=bgCharColor)

define charHDg = Character("Hotdog lover", color=bgCharColor)
define charTrn = Character("Train Conductor", color=bgCharColor)
define charDtv = Character("Detective", color=bgCharColor)
define charDck = Character("Duck Man", color=bgCharColor)
define charHnt = Character("Hunter", color=bgCharColor)

#-----------------------------------------------------------------------------------
# Initialize a counter variable for scenarios
init python:
    scenariosSurvived = 0
#-----------------------------------------------------------------------------------
# used to check if a weapon has been acquired
init python:
    weapon = False
#-----------------------------------------------------------------------------------
# used to check if the saw has been acquired
init python:
    saw = False
#-----------------------------------------------------------------------------------
# number of limbs
init python:
    limbs = 5  # Initialize with 5 limbs (head, arm1, arm2, leg1, leg2)
#-----------------------------------------------------------------------------------
# number of sacrifices
init python:
    sacrifices = 0 
#-----------------------------------------------------------------------------------

label start:

    stop music

    # Introduction

    # play a song / sound effect
    play sound "sfx/birds.mp3"
    # Show a background with fade
    scene bedroom with fade
    "You wake up to the sound of birds chirping outside your window."
    play sound "sfx/phone.mp3"
    "Then, your phone starts ringing."

    charNotYetCan "Hey, Ridley! Wanna hang out?" 
    play sound "sfx/birds.mp3"
    charMC "Sure, where to?" 
    charNotYetCan "A camp. Say bye to your parents and make sure to leave your will!" 
    charMC "Wait? What do you--"
    play sound "sfx/hang-up.mp3"


    "Oh. He already hung up..." 
    charMC "He can be that weird, sometimes." 
    play sound "sfx/birds.mp3"

    "While packing stuff for later, you notice your parents standing by the door."

    show mom with dissolve
    show dad at right with dissolve

    charDad "Hey, are you going somewhere?" 
    # Character sprite
    show ridley at left with dissolve
    charMC "Camping." 
    "You answer while shrugging"
    charMom "Okay, just be sure to have your phone with you at all times." 
    charMC "Sure!"
    charDad "Don't forget that we won't be here for the weekend."
    charMC "Yeah. I'll take care of the house, don't worry."

    hide dad with fade
    hide mom with fade

    play sound "sfx/footsteps.mp3"
    scene house with fade
    "After packing and taking a shower, you decide to go downstairs to eat breakfast with your parents"
    "Then, you head out to see Ash."

    scene street with fade
    play sound "sfx/cars.mp3"
    scene police with fade
    show ridley with dissolve 
    "As you approach the restaurant owned by Ash's family, an ambulance can be heard nearby."
    play sound "sfx/police.mp3"
    "Getting even closer, you see some police officers taking care of a crowd."
    play sound "sfx/crowd.mp3"
    "It seems that part of the road had been sealed off due to a recent incident."
    play sound "sfx/footsteps.mp3"
    "Not wanting to trespass, you decide to reach the restaurant by going the other way around." 
    scene street2 with fade
    play music "music/notScary.mp3"
    "As you do so, suddenly, you feel a hand on your shoulder..."
    charNotYetCan "It's chomping time!" 
    "A voice exclaims."
    play music "music/happy.mp3"
    "You quickly turn around to see your silly friend laughing at you."
    show ridley at left with dissolve
    "You realize it was your friend, Ash..."
    charMC "This is why you don’t have many friends." 
    show ash with dissolve
    charNotYetCan "Right, because of that…" 
    "Ash says with a remorseful face."
    charMC "Say, do you know what all that is about?" 
    "You point at all the commotion happening close to your friend's home."
    charNotYetCan "Some idiot pretending to be a vampire or whatever." 
    charNotYetCan "It's cool now."
    charNotYetCan "I think..."
    charMC "You think?!"
    charNotYetCan "Yeah, don't even worry about it."
    charMC "..."
    charNotYetCan "Anyway."
    charNotYetCan "We can’t go eat at our restaurant for some time, though."
    charMC "That’s weird." 
    charMC "Did anything bad happen there?"
    play music "music/oof.mp3" 
    charNotYetCan "I don’t know..." 
    charNotYetCan "But, speaking of eating, let's grab something to eat in that other restaurant."
    charNotYetCan "I could eat a whole cow right about now." 
    play music "music/happy.mp3"
    "You look at your wristwatch and realize why Ash was starving."
    charMC "Sure…" 
    charMC "Let's go, then."
    scene street3 with fade
    hide ash with dissolve
    hide ridley with dissolve

    "You and your friend decide on what to order as you two made your way to the restaurant."
    "Minutes later, Ash remembered something crucial."
    scene restaurant1 with fade
    show ash with dissolve
    charNotYetCan "Oh!"
    show ridley at left with dissolve
    charMC "What?"
    charNotYetCan "I forgot to pack some condiments for dinner!" 
    charNotYetCan "You know I can't live without peppering my food before eating it."
    charNotYetCan "...especially campfire-cooked food."
    "Ash confesses, kneeling on the ground."
    charMC "You always like to overreact."
    charMC "Can't you just bear with it for today?" 
    charNotYetCan "I can but..."
    charNotYetCan "Don't be surprised if I feel like running around in search of deliciously seasoned meat." 
    "You throw an annoyed look at Ash."
    charMC "Well, enough chatting." 
    charMC "Let's just go inside this place." 
    "You reach to the restaurant's door handle and open the door."

    scene restaurant2 with fade
    play sound "sfx/restaurant.mp3"
    "You and Ash ordered food as soon as you found a table for both of you." 
    "You talked for a while about trivial matters until you and your friend had finished your meal." 
    "While wating for the bill, Ash decided to go to the bathroom and stayed there for a while."
    "He reappeared after and even helped in paying the bill."
    "It did leave you confused as to what he was doing in there for so long..."
    charMC "Are you ok, buddy?"
    "You ask Ash when you see an expression on his face that left you curious."
    charNotYetCan "Yeah. Never. Been. Better."
    charMC "If you say so."
    charNotYetCan "Do you have all the stuff for our dinner at the campsite?"
    charMC "Food related? Yes."
    charNotYetCan "What about knifes and pots?"
    charMC "Nope..."
    charNotYetCan "..."
    charMC "..."
    charNotYetCan "Well, maybe we should buy that in our way there."
    charMC "Sounds like a plan."
    play sound "sfx/footsteps.mp3"
    "You, accompanied by Ash, leave the restaurant and head for the nearest warehouse store."

    scene warehouse with fade
    play sound "sfx/warehouse.mp3"
    "With minimal hassle, both arrived at the store to purchase the necessary items." 
    play sound "sfx/radio.mp3"
    "All the while a disturbing bathroom murder was being reported on the radio..."
    charMC "What's this all about?"
    charNotYetCan "Don't know, don't care."
    charNotYetCan "Hey! Look at how sharp that knife is!"
    charMC "..."
    "After a while, you got everything that was needed for later."

    scene street4 with fade
    play sound "sfx/cars2.mp3"
    "The sun began to set."
    "And with everyone else retreating to the safety of their homes due to the threat of a serial killer on the loose."

    scene taxi with fade
    play sound "sfx/horn.mp3"
    "You decided to call a taxi to take you and your friend to the campsite."
    scene campsite with fade
    play sound "sfx/campsite.mp3"
    "An hour later, the taxi arrived at the campsite."
    show ash with dissolve
    "Ash gets out of the taxi and while you were paying for the fare, he began looking around at the place."
    charNotYetCan "That place looks good."
    charNotYetCan "Let's stay there."
    "Ash said, as he pointed to an isolated part of the campsite."
    show ridley at left with dissolve
    charMC "Sure."
    "With not much choice on the matter." 
    "You agree on staying in that place for the evening."
    # This ends the introduction.

    # go to campsite scenario
    jump d1

return

label d1:

    # distraction 2: Beginning of your End

    scene campfire with fade
    play sound "sfx/campsite.mp3"

    "At the campfire, you and your friend cook some food."
    show ash at right with dissolve
    show ridley with dissolve
    "You leave your friend in charge of the meat boiling in the pot."
    "You look away for a second, and then..." 
    play music "music/oof.mp3"
    "You witness Ash devouring all the meat that was in the pot."
    charNotYetCan "Not enough..."
    charNotYetCan " s t i l l" 
    charCan "h u n g r y"
    "Still hungry, he reaches out towards you, attempting to take a bite out of your nose."
    "You try to make a run for it, but unfortunately, he manages to grab onto your leg."

    play music "music/quick.mp3"
    menu:
        "You decide to:" 

        # Choice 1:
        "Reach out for the hotpot.":
            play sound "sfx/boiling.mp3"
            "You throw it at your friend’s face and you see them squirming around."
            hide ash with dissolve
            play sound "sfx/running.mp3"
            "You are free to run away."
            python:
                # increase the number of scenarios survived by 1
                scenariosSurvived += 1 
            python:
                survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

            "[survived_text]"
                
            jump t3

        # Choice 2:
        "Wrestle free from his grasp.":
            "But soon realize that he is stronger than you."
            play sound "sfx/limb-lost.mp3"
            scene limb-lost with fade
            "Your friend gets a body part of yours."
            hide ridley with dissolve

            python:
                # Reduce the limbs by 1
                limbs -= 1  
            
            python:
                remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
            
            "[remaining_limbs_text]"

            "You somehow ran away..."

            jump t3

# this ends d1 
return

label d2:
    # Distraction 3: Hotdog Panic
    
    scene street8 with fade
    play sound "sfx/running.mp3"
    show ridley at left with dissolve
    show ash at right with dissolve
    "Now in the city, you spot your cannibal friend behind you, and you immediately start running away." 
    hide ash with dissolve
    play sound "sfx/bump.mp3"
    "Unfortunately, you end up colliding with someone who was carrying a hotdog."
    show hotdogdude at right with dissolve

    play music "music/quick.mp3"
    menu:
        "You decide to:" 

        # Choice 1:
        "Panically toss the hotdog in the direction where your friend was.":
            "However, before doing so, you notice your friend doing something out of character."
            show ash with dissolve
            charCan "So sorry for this."
            charCan "Please don’t be mean to my clumsy friend."
            charHDg "Don’t worry, I don’t mind it that much."
            charMC "What?"
            "You said as you blankly stared at your friend who was now assisting the person you just bumped into."
            play sound "sfx/limb-lost.mp3"
            scene limb-lost with fade
            "Your friend takes this opportunity to get a body part of yours."

            python:
                # Reduce the limbs by 1
                limbs -= 1
            
            python:
                remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
            
            "[remaining_limbs_text]"

            "You somehow ran away..."

            jump t2

        # Choice 2:
        "Quickly apologize to the person.":
            charMC "Sorry, my bad."
            "After that, you glance back to see your friend devouring the hotdog that had fallen to the ground." 
            play sound "sfx/eat.mp3"
            show ash with dissolve
            "You realize that he also has a grip on your arm."
            play music "music/oof2.mp3"
            "So you decide to trick him."
            charMC "If you want more of those hotdogs, I know just the place where they are. Just let me go and grab them."
            "You said, in hopes of tricking him."
            "Your friend falls for it." 
            hide ash with dissolve
            hide hotdogdude with dissolve
            "He lets go of your arm, and you hastily head for the nearby hotdog stand." 
            play sound "sfx/falling.mp3"
            scene stand with fade
            "You jump on it, attempting to drive it like a racing car, resulting in all the hotdogs spilling out from behind the hotdog stand, causing your friend to chase you." 
            charCan "Come back here!"
            show ash with dissolve
            play sound "sfx/rolling.mp3"
            charCan "All these hotdogs are not as good as your flesh!"
            hide ash with dissolve
            "A few minutes later, you jump out of the hotdog stand."
            play sound "sfx/falling-ground.mp3"
            "As you safely land on top of a shrub of plants, you see your friend still chasing the hotdog stand."
            "You find a saw lying on the floor."
            "You decide to pick it up."
            python:
                saw = True
            "You are free to run away."
            python:
                # increase the number of scenarios survived by 1
                scenariosSurvived += 1 
            python:
                survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

            "[survived_text]"
                
            jump t2

# this ends d2 
return

label d3:
    # Distraction 8: CALVES!

    
    scene street9 with fade
    play sound "sfx/running.mp3"
    show ridley with dissolve
    show ash at left with dissolve

    "Maybe it's over." 
    play sound "sfx/panting-7108.mp3"
    charMC "How big can his stomach be?"
    "You wonder how he can keep running after you with all that food in his body." 
    play music "sfx/crowded-avenue-people-talking-vendors-shouting-musicians-playing-part-1-7099.mp3"
    charMC "Why does he want your meat? There's so many people around…" 
    charMC "Why can’t he pick one of them?" 
    charMC "What’s so tasty about me?"
    
    play music "music/oof2.mp3"
    "Before you know it, he taps you on the shoulder."
    charCan "Look, as much as I’m enjoying my workout, I kinda really need to eat you."
    charMC "..."
    charCan "Hey, I don't wanna sound thankless." 
    charCan "I mean, look at these calves." 
    play sound "sfx/long-kiss-41029.mp3"
    charCan "So sexy..."
    charMC "Are you... making out with your calves?"
    play sound "sfx/ahem-1-47603.mp3"
    charCan "*coughs*" 
    charCan "Anyway, what was I saying?"
    charCan "These days my memory seems to get enthralled by my…beautiful calv-"
    charCan "FOCUS!" 
    charCan "Now." 
    charCan "Remind me what I was telling you?"

    play music "music/quick.mp3"
    menu:
        "Think fast!"

        # Choice 1:
        "Divert the focus to another person":
            if limbs == 5:
                charMC "Oh right! You were telling me about how much you want to eat that man over there."
                charMC "Doesn't he look yummy?"
                charCan "Are you sure?" 
                charCan "Because it would make more sense if I wanted to eat you."
                charCan "Since I’m chasing you and all."
                charMC "Uh. LOOK! CALVES!"
                charCan "YES! CALVES." 
                charCan "Such nice ones you have, Ridley!"
                charCan "Yummers."
                charMC "Wait, no!"
                charMC "Stop!!!"

                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                "Your friend gets a body part of yours."

                python:
                    # Reduce the limbs by 1
                    limbs -= 1
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"

                charCan "Might as well move, old friend. You’ll take some time to digest."
                "You somehow ran away..."   
                # Check if the character has no more limbs before going to the badEnd
                if limbs <= 0:
                    jump badEnd
                else:
                    jump t1

            else:
                charMC "Oh right! You were telling me about how much you want to eat that man over there."
                charMC "Doesn't he look yummy?"
                charCan "Are you sure?" 
                charCan "Because it would make more sense if I wanted to eat you."
                charCan "Since I’m chasing you and all."
                charMC "Uh. LOOK! CALVES!"
                "You notice as your friend spots the man you were referring to."
                charCan "Well, I guess if I’ve already eaten yours." 
                charCan "You won’t get jealous will you?"
                "You shake your head in response."
                charCan "Good. Stay here."
                hide ash with dissolve
                charMC "..."
                "You, in fact, did not stay there." 
                "You hopped away as fast as you could."
                "You run away!"
                python:
                    # increase the sacrifices variable by 1
                    sacrifices += 1  
                
                python:
                    sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)
                
                "[sacrifices_text]"

                # Check if the character has sacrificed more or equal to 3 people to go to true end
                if sacrifices >= 3:
                    jump trueEnd
                else:
                    jump t1


        # Choice 2: 
        "Divert the focus onto something else":
            play music "music/mystery2.mp3"
            charMC "Oh right! I shared the story of how much we loved collecting random bones we found when we were little!"
            charMC "Remember?"
            charCan "Not really..."
            charMC "Of course you don't, you silly head!" 
            play music "sfx/old-friendship-130829.mp3"
            charMC "You used to eat them all." 
            charMC "Ahh, things normal children do."
            charCan "Uhh. If you say so."
            charMC "And you told me you kept one of the bones." 
            charMC "To remind you of the old times."
            charCan "That doesn't sound like me."
            charMC "Shhhh." 
            charMC "Right now you were about to return to the camp to get it for me."
            charMC "I told ya that if you did that for me, I would stop running and let you eat me." 
            charMC "Because we must trust in the power of friendship to keep us together." 
            charMC "And what better way than from inside you!"
            charCan "Do you mean that?"
            charMC "Of course, bestie!"
            charCan "Ok, stay here." 
            charCan "I’ll go get you that bone." 
            charCan "Just gotta remember where I put it."
            hide ash with dissolve
            "Your friend leaves."
            "You successfully trick Ash."
            "You run away."
            python:
                # increase the number of scenarios survived by 1
                scenariosSurvived += 1 
            python:
                survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

            "[survived_text]"

            # Check if the character has survived more or equal to 3 scenarios, go to good end
            if weapon == True and scenariosSurvived >= 3 and limbs != 0 and sacrifices <= 2:
                jump goodEnd
            else:
                jump t1
    jump t1

# this ends d3
return


label d4:
    # Distraction 7

    scene street5 with fade
    play sound "sfx/running.mp3"
    show ridley with dissolve
    show ash at left with dissolve
    play music "sfx/terror-orchestra-6-156155.mp3"
    "After running for your dear life, Ash still manages to stay close to you."
    charMC "Well, maybe If I had all limbs I could outrun you."
    charMC "...sad that it was my favorite limb that was taken off..." 
    play sound "sfx/munching-food-73994.mp3"
    charMC "At the very least, was it tasty?"
    charCan " v e r y" 
    charCan "t a s t y"
    charMC "Oh welp."
    charMC "If one of us is happy..."

    play music "music/quick.mp3"
    menu:
        "Now, how the hell will you get out of this one?"

        # Choice 1:
        "Look behind you!":
            # * points *
            if limbs >= 3:
                scene street6 with fade
                charMC "OH MY GOD, is that Annabelle Hektor?!"
                play sound "sfx/wind.mp3"
                charCan "Where??"
                play sound "sfx/whoosh-6316.mp3"
                "You distracted Ash."
                hide ash with dissolve
                play sound "sfx/running.mp3"
                "You run away."
                python:
                    # increase the number of scenarios survived by 1
                    scenariosSurvived += 1 
                python:
                    survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

                "[survived_text]"
                # Check if the character has survived more or equal to 3 scenarios, go to good end
                if weapon == True and scenariosSurvived >= 3 and limbs != 0 and sacrifices <= 2:
                    jump goodEnd
                else:
                    jump d3
                                
            elif limbs <= 2:
                scene street6 with fade
                "Unfortunately, it is very hard to point at something with no arms."
                charCan "Oh? "
                charMC "It’s..."
                charMC "It’s your twin sister!"
                play sound "sfx/laugh.mp3"
                charCan "Nice try."
                play sound "sfx/eatingsfxwav-14588.mp3"
                charCan "I ate her in the womb."
                play sound "sfx/violindanger-83476 (1).mp3"
                charMC "..."
                hide ash with dissolve
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                "Your friend takes this opportunity to get a body part of yours."

                python:
                    # Reduce the limbs by 1
                    limbs -= 1
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"

                charCan "Might as well move, old friend. You’ll take some time to digest."
                "You somehow ran away..."   
                # Check if the character has no more limbs before going to the badEnd
                if limbs <= 0:
                    jump badEnd
                else:
                    jump d3

        # Choice 2:
        "Kick him where the sun don’t shine":
            if limbs >= 2:
                scene street8 with fade
                "You gather momentum for a massive Ronaldo-style kick."
                "It strikes true!"
                play sound "sfx/bone.mp3"
                "You no longer have to worry about little baby cannibals running around."
                play sound "sfx/ough-47202.mp3"
                charMC "You deserved it!"
                play sound "sfx/monster-roar-6985.mp3"

                "You should probably worry about getting away, though."
                hide ash with dissolve
                play sound "sfx/running.mp3"
                "You run away."
                python:
                    # increase the number of scenarios survived by 1
                    scenariosSurvived += 1 
                python:
                    survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

                "[survived_text]"
                
                # Check if the character has survived more or equal to 3 scenarios, go to good end
                if weapon == True and scenariosSurvived >= 3 and limbs != 0 and sacrifices <= 2:
                    jump goodEnd
                else:
                    jump d3

            elif limbs == 1:
                "You wobble around on your legless torso and manage to hop all the way up!"
                scene street8 with fade
                charCan "I’ve seen mightier penguins."
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                "Your friend takes this opportunity to get a body part of yours."

                python:
                    # Reduce the limbs by 1
                    limbs -= 1
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"

                charCan "Might as well move, old friend. You’ll take some time to digest."
                hide ash with dissolve
                play sound "sfx/running.mp3"
                "You somehow ran away."
                # Check if the character has no more limbs before going to the badEnd
                if limbs <= 0:
                    jump badEnd
                else:
                    jump d3

    jump d3

# this ends d4
return


label t1:
    # Trick 6: Train to...

    scene tunnel with fade
    play sound "sfx/running.mp3"

    "Still running away from your impending doom, you stumble upon a train station!"

    # Check the number of remaining limbs
    if limbs == 5:
        # Situation 1:
        scene booth with fade
        play sound "sfx/crowd.mp3"
        show ridley at left with dissolve
        "Without hesitating, you enter the station and spot some telephone booths."
        "Blessed with the opportunity to finally call your parents for help, you realize, unfortunately, that you have no money on hand."
        play music "music/quick.mp3"
        menu:
            "You decide to:" 

            # Choice 1:
            "Leave the call for later and rush to the nearest train that has just arrived at the station.":
                scene train3 with fade
                play sound "sfx/train.mp3"
                "Upon entering the carriage, however, a person rudely talks with you."
                "Someone gets close to you and asks."
                "Can I see your ticket?!"

                show conductor with dissolve
                "You realize it’s the train conductor who was doing his job of searching for anybody with no train ticket."
                charMC "I’m sorry but a lot has happened so I don’t have the money to get a ticket..."
                charTrn "Not an excuse!"
                charMC "But-"
                "You give up on explaining your bizarre situation to the train conductor so he decides on escorting you off the train."
                "Glancing back, you see your cannibal friend ready to hunt you down."
                show ash at right with dissolve
                charCan "Forgot something?" 
                "Your friend shows you your wallet."
                charCan "You have nowhere else to run off to!"
                play sound "sfx/running.mp3"
                "In a split second, perhaps due to desperation, you push the train conductor, who was standing next to you, with all your might in your friend’s direction."
                "Your friend gets distracted." 
                hide ash with dissolve
                hide conductor with dissolve
                "You run away!"
                python:
                    sacrifices += 1  # increase the sacrifices variable by 1
                
                python:
                    sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)
                
                "[sacrifices_text]"

                # Check if the character has sacrificed more or equal to 3 people to go to true end
                if sacrifices >= 3:
                    jump trueEnd
                else:
                    jump noEnd

            # Choice 2:
            "Head to the nearest vending machine to check if there's some pocket change underneath it.":
                scene machine with fade
                play sound "sfx/train.mp3"
                "Thankfully, you find a lot of coins, enough to even buy a train ticket, so you do so."
                scene train4 with fade
                "Afterwards, you get inside the train and show it to the train conductor."
                play sound "sfx/train.mp3"
                show conductor with dissolve
                charTrn "Thanks."
                charTrn "Have a safe journey."
                charMC "Thanks."
                "You watch the train conductor leave the carriage and you look around to see who was left."
                hide conductor with dissolve
                "You spot only a few other passengers, which makes you feel safe."
                "You start to relax, thinking you've left the worst behind." 
                "..."
                play music "music/oof2.mp3"
                "Suddenly, the train experiences a terrible accident."
                "You wake up to a terrible scene that left you shocked."
                "Trying to get up from the ground, you check your whole body for any injuries." 
                "Thankfully, you were fine but soon realized something frightful."
                charMC "I gotta get out of here." 
                charMC "This train accident may not have been a regular accident after all."
                charCan "Well, well..." 
                charCan "Someone’s been using their brain. I’m proud of you."
                "You look up to see where the voice was coming from." 
                show ash at right with dissolve
                "You realize it was your friend and he was already grabbing you."
                charCan "You really tried running away from me?"

                "Your friend gets a body part of yours."
                hide ridley with dissolve
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade

                python:
                    # Reduce the limbs by 1
                    limbs -= 1 
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"

                "You somehow ran away."

                # Check if the character has no more limbs before going to the badEnd
                if limbs <= 0:
                    jump badEnd
                else:
                    jump noEnd
   
    else:
        # Situation 2:

        play music "music/oof2.mp3"
        scene train2 with fade
        "You move slowly along the train tracks and enter what appears to be an empty train carriage."
        scene train4 with fade
        show ridley at left with dissolve
        "Sitting down to rest for a moment, you're awakened when someone touches your cold shoulder." 
        "Startled, you open your eyes to find a detective's badge."
        show detective with dissolve
        "She explains that she's been investigating a strange string of cases related to cannibalism and points out your missing limbs, asking for what happened."

        play music "music/quick.mp3"
        menu:
            "You decide to:" 

            # Choice 1:
            "Recount everything about your cannibal friend." : 
                "She proceeds to bandage you properly."
                "Surprisingly, she seems understanding—perhaps too understanding— so you decide to test her."
                "You ask."
                charMC "Could you lend me your phone for a minute?"
                charDtv "Sure. Let me just call someone first."
                play sound "sfx/hang-up.mp3"
                "She makes her call and when placing her phone on your hand, the lights on the train go out."
                scene lightout with fade
                play music "music/oof.mp3"
                hide detective with dissolve
                hide ridley with dissolve
                charMC "What’s going on?"
                charDtv "Nothing you should worry about. Just stay here for a while."
                "Trying not to give in to the dark, a few minutes later, you start listening to some footsteps."
                charDtv "Took you long enough."
                "Someone gets closer to you and says."
                "Sorry, some other stuff happened."
                "You recognized that voice from the same person who you were running away from."
                charMC "That voice. How did you get in here?"
                "Your question is left unanswered as you suddenly feel someone grabbing you."
                play sound "sfx/limb-lost.mp3"
                scene limb-lost2 with fade
                "They both get a body part of yours."

                python:
                    # Reduce the limbs by 2
                    limbs -= 2
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"

                "You somehow ran away."

                # Check if the character has no more limbs before going to the badEnd
                if limbs <= 0:
                    jump badEnd
                else:
                    jump noEnd
                

            # Choice 2:
            "Claim that you recently suffered an accident and return to resting." :
                "She wakes you up again as the train starts moving."
                charDtv "So, where are you  going at this time?"
                "You begin feeling suspicious about her."
                charMC "To see my family."
                charDtv "Ok."
                scene lightout with fade
                play music "music/oof.mp3"
                "The detective decides to make a call and minutes later, the train's lights go out."
                hide detective with dissolve
                hide ridley with dissolve
                "Instead of sitting, you decide to press the emergency button to safely exit the train."
                charDtv "Stay still." 
                charDtv "Wouldn’t want you to get injured in any way."
                play sound "sfx/train.mp3"
                "After saying this, she tries to grab you, but you dodge. This leads her out through the open train doors, resulting in her death."
                "You hear fast footsteps approaching from the next train carriage so, in a split second, you decide to leave the train."
                play sound "sfx/train.mp3"
                "The train was still moving but you gathered courage."
                charMC "C’mon! I can make this."
                "You jump out of the moving train, landing safely in a shrub of land."
                show ridley at left with dissolve
                scene train2 with fade
                "Making your way back into the train station, you grab a body part to restore yourself and some items."
                "You find a pistol."
                "You decide to pick it up."
                python:
                    weapon = True

                "Restored a limb."
                python:
                    limbs += 1  # Increase the limbs variable by 1
                
                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)
                
                "[remaining_limbs_text]"
                "You somehow ran away."
                # Check if the character has survived more or equal to 3 scenarios, go to good end
                if weapon == True and scenariosSurvived >= 3 and limbs != 0 and sacrifices <= 2:
                    jump goodEnd
                else:
                    jump noEnd
                
# this ends t1 
return

label t2:
    # Trick 1: Duck Man
    scene pond with fade
    play sound "sfx/pond.mp3"

    show ridley at left with dissolve
    show duck-man with dissolve

    "After a long sprint, you start hearing water."
    "A man is throwing rocks at the ducks in a pond."
    "He can't even hit one, though."
    "There are some trees nearby."

    "Oh, this one will be easy."
    "You think."
    charMC "Excuse me, sir!"
    charDck "Ugh. Can’t you see I’m busy." 
    charMC "It’s just..." 
    charMC "I’m lost!"
    charDck "Fuck off!"

    play music "music/quick.mp3"
    menu:
        "You decide to:"

        # Choice a:
        "Scare him and make him head towards the cannibal.":
            if limbs == 5:
                charMC "I heard there are dangerous... animals around." 
                charMC "I’ve been hearing crunching noises all the way here." 
                charMC "Please show me the way out." 
                charMC "You should leave too."
                charDck "Yeah right." 
                charDck "Just what I needed tonight..." 
                charDck "Another drug addict..." 
                charDck "I know how to deal with the likes of you."
                "He unsheathes a rubber chicken knife that, although ridiculous, looks very deadly."
                play sound "sfx/squeaky-toy-1-6059.mp3"
                charMC "Uh? What...?"
                play music "music/notScary.mp3"
                "He starts chasing you with his rubber chicken knife!"
                charMC "AHHH!"
                "You go back where you came from." 
                play sound "sfx/running.mp3"
                "When spotting your friend, the cannibal, you trip!" 
                "Leading the Duck Man straight into the cannibal's grasp."
                hide duck-man with dissolve
                play sound "sfx/running.mp3"

                "You run away!"
                python:
                    # increase the number of sacrifices by 1
                    sacrifices += 1 
                python:
                    sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)

                "[sacrifices_text]"

            else:
                # Missing any limb
                charMC "I heard there are dangerous...animals around." 
                charMC "I’ve been hearing crunching noises all the way here." 
                charMC "Please show me the way out." 
                charMC "You should leave too."
                charDck "Yeah right." 
                charDck "Just what I needed tonight... "
                charDck "Another drug addict..."
                charDck "I know how to deal with the likes of you."
                "He unsheathes a rubber chicken knife that, although ridiculous, looks very deadly!"
                play sound "sfx/squeaky-toy-1-6059.mp3"
                charMC "Uh? What...?"
                play music "music/notScary.mp3"
                "You attempt to run!" 
                "But, due to your lack of limbs, you can only hop slowly." 
                play sound "sfx/running.mp3"
                "Duck Man ends up getting you..."
                hide duck-man with dissolve
                play sound "sfx/rubber-chicken-96436.mp3"
                "You get stabbed but don't die, since, obviously, a rubber chicken knife can only do so much."
                hide ridley with dissolve
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                "While lying on the floor, the cannibal catches up to you and takes a part of your body."
            python:
                # Reduce the limbs by 1
                limbs -= 1  

            python:
                remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)

            "[remaining_limbs_text]"

            "You somehow run away."

        # Choice b:
        "Be weird.":
            play music "music/mystery.mp3"
            charMC "You see, the gods stopped answering my calls." 
            charMC "I feel so lost... without them."
            charDck "Uh? Did you escape some hospital or something?"
            "You start screaming incoherently as if performing a ritual but with made-up words."
            "Duck Man, now being scared by you says."
            charDck "Hey! Get away from me!" 
            charDck "Shoo!"
            "He starts throwing rocks at you." 
            "Although you pretend not to notice, the stones do hurt your feelings." 
            charMC "I’ve sacrificed so much, so many things, so many people..." 
            charMC "Maybe you will get the gods to listen to me."
            "Duck Man, trapped between you and the pond, faints dramatically." 
            play sound "sfx/sound-effect-scream-thump-groan-159317.mp3"
            hide duck-man with dissolve
            "You prepare the Duck Man to make him more appealing to your dear cannibal friend."
            charMC "Can’t believe that worked!"
            python:
                # increase the number of sacrifices by 1
                sacrifices += 1 
            python:
                sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)

            "[sacrifices_text]"

            "You ran away."

        # Choice c:
        "Talk about the ducks.":
            charMC "Why are you throwing rocks at those ducks?"
            charDck "Look, what do you want?" 
            charDck "Leave! It’s none of your business."
            charMC "C'mon what did they even do?"
            "He appears to get angry at you and starts yelling."
            charDck "These stupid ducks deserve this!" 
            charDck "They killed my grandma!"
            "While the Duck Man’s back is turned towards them, the very wholesome ducks begin gathering right behind him."
            play sound "sfx/quack.mp3"
            charDck "Wha- AAHHHHHHH!"
            play sound "sfx/607226__d4xx__ducks-_1_.mp3"
            play music "music/oof.mp3"
            scene ducks with fade
            "The Duck Man is pulled into the lake and every last bit of his flesh is devoured by the previously wholesome ducks."
            hide duck-man with dissolve
            "You witness as his remains, or what’s left of them anyway, float in the shallow ponds."
            "Suddenly, Ash appears." 
            show ash at right with dissolve
            "You notice that the cannibal has no meat to eat."
            "So he ends up getting you, instead."
            play sound "sfx/wahwahwahwaaaahahahahahaha-94669.mp3"
            hide ridley with dissolve
            play sound "sfx/limb-lost.mp3"
            scene limb-lost with fade
            python:
                # Reduce the limbs by 1
                limbs -= 1  

            python:
                remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)

            "[remaining_limbs_text]"

            "You somehow ran away."

        # Choice d:
        "Drop a tree on him ":
            if limbs == 5 and saw == True:
                charMC "Oh, I was lost in the lyrics of a song." 
                charMC "A song that I was singing in my head."
                charDck "Are you serious? Just leave!"
                charMC "Fine, fine." 
                charMC "Just, stay here."
                charMC "In that exact position you are in right now."
                charDck "Weirdo..."
                play sound "sfx/footsteps.mp3"
                scene tree with fade
                "You pretend to leave the vicinity, but manage to hide behind a large tree."
                "Then, you look around searching for the perfect tree to bonk on the Duck Man’s head."
                "You end up picking one that looks like it will land right on his head."
                play music "music/oof.mp3"
                "You use the saw to cut the tree and make it fall." 
                play sound "sfx/bonk-sound-effect-36055 (1).mp3"
                "Ending the Duck Man’s life as soon as it bonked on him."
                play sound "sfx/man-scream-121085 (2).mp3"
                hide duck-man with dissolve
                "The Duck Man ends up getting a bit... squished." 
                "You just hope the cannibal doesn't mind it that much."
                "Fast footsteps get closer to your vacinity, so you decide to run away."
                python:
                    # increase the number of sacrifices by 1
                    sacrifices += 1 
                python:
                    sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)

                "[sacrifices_text]"

            if limbs == 5 and saw == False:
                charMC "Oh, I was lost in the lyrics of a song." 
                charMC "A song that I was singing in my head."
                charDck "Are you serious? Just leave!"
                charMC "Fine, fine." 
                charMC "Just, stay here."
                charMC "In that exact position you are in right now."
                charDck "Weirdo..."
                play sound "sfx/footsteps.mp3"
                scene tree with fade
                "You pretend to leave the vicinity, but manage to hide behind a large tree."
                "You look around searching for the perfect tree to bonk on the Duck Man’s head."
                "You end up picking one that looks like it will land right on his head."
                "Looking at the tree you wonder:" 
                "What made me think that this was a good idea to begin with?"
                "You attempt to push the tree with your bare hands."
                "Unfortunately you lack the strengh to make it move in the slightest."
                "Suddenly you start hearing loud footsteps approaching."
                show ash at right with dissolve
                "It was your friend, Ash, now right behind you."
                "He gets you."
                "The cannibal has a hard laugh while he bites a chunk out of you."
                hide ridley with dissolve
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                python:
                    # Reduce the limbs by 1
                    limbs -= 1  

                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)

                "[remaining_limbs_text]"

                "You somehow ran away."

            if limbs <= 4:
                charMC "Oh, I was lost in the lyrics of a song." 
                charMC "A song that I was singing in my head."
                charDck "Are you serious? Just leave!"
                charMC "Fine, fine." 
                charMC "Just, stay here."
                charMC "In that exact position you are in right now."
                charDck "Weirdo..."
                play sound "sfx/footsteps.mp3"
                scene tree with fade
                "You pretend to leave the vicinity, but manage to hide behind a large tree."
                "You look around searching for the perfect tree to bonk on the Duck Man’s head."
                "You end up picking one that looks like it will land right on his head."
                "You look at the tree and slowly approach it." 
                "Only then you realize."
                "This tree does not seem to like people with missing limbs!"
                "Sad and depressed, you just sit down and wait for the cannibal to get ya..."
                hide ridley with dissolve
                play sound "sfx/limb-lost.mp3"
                scene limb-lost with fade
                python:
                    # Reduce the limbs by 1
                    limbs -= 1  

                python:
                    remaining_limbs_text = "You have {} limb(s) remaining.".format(limbs)

                "[remaining_limbs_text]"

                "You somehow ran away."
    jump d4

# this ends t2
return
    
label t3:
    # Trick 8: Forest Follies
    scene forest with fade
    play sound "sfx/running.mp3"
    show ridley at left with dissolve

    "After a whole lotta sprinting, you find a hunter stuck in a bear trap."
    show hunter at right with dissolve
    charHnt "Oh, thank goodness..."
    charHnt "Please help me!"
    "Ash must be close behind you!" 
    "There’s no way you’ll outrun him if he finds you."
    charMC "..."
    "But maybe if someone else takes the fall..."

    play music "music/quick.mp3"
    menu:
        "You decide to:" 

        # Choice 1:
        "Pretend to be deaf." :
            "You ignore the man and hide yourself behind a convenient tree."
            scene tree with fade
            charHnt "Hello?"
            "The hunter was still trying to reach you but you decide to still ignore him."
            charHnt "HELLO! CAN YOU HEAR ME??"
            play sound "sfx/footsteps-leaves.mp3"
            charHnt "Tu speak Engleish?!"
            play sound "sfx/bone.mp3"
            charHnt "HELP ME -"
            play music "music/oof2.mp3"
            "The man’s head is totally swallowed up by the cannibal, who bit it clean off."
            "...Yikes."
            "Oh, well. Qué será, será."
            "You should probably bail while you have the time, though..."
            play sound "sfx/monster-roar-6985.mp3"
            hide hunter with dissolve
            play sound "sfx/running.mp3"
            "You run away!"
            # *Sound: Sniffing, then growling.*
            python:
            # increase the number of sacrifices by 1
                sacrifices += 1 
            python:
                sacrifices_text = "You have sacrificed {} person/people.".format(sacrifices)

            "[sacrifices_text]"

            jump d2

        # Choice 2:
        "Close the bear trap further.":
            "You move sneakily closer..."
            scene trap with fade
            charHnt "Bless your heart, young one." 
            charHnt "Truly, you are -"
            play sound "sfx/man-scream-121085 (2).mp3"
            "...and slam the bear trap down on the hunter’s foot."
            charHnt "Oh God!"
            play music "music/determinator.mp3"
            # *Visuals: A foot torn off the body and stuck in the trap.*
            charHnt "Wait..."
            charHnt "Y-You..."
            charHnt "You freed me!"
            charHnt "Thank you, brave one." 
            charHnt "My very own savior!"
            charMC "...sure."
            play music "sfx/birds-singing-in-and-leaves-rustling-with-the-wind-14557.mp3"
            charHnt "I’ll be heading off." 
            charHnt "I think the cannibal I heard of might be coming down for a visit."
            charHnt "So kind of you to spare time to save little old me when you could’ve escaped."
            charMC "It was no problem."
            charHnt "Now go!"
            charHnt "I think I can hold him off with this shotgun right here."
            charMC " Good luck!"
            "You run away."
            scene tree with fade
            play sound "sfx/running.mp3"
            hide hunter with dissolve
            play sound "sfx/footsteps-cannibal.mp3"
            charHnt "Hello, brave one!"
            play sound "sfx/bone.mp3"
            "You hear in the distance a loud crunch noise."
            play sound "sfx/running.mp3"
            charCan "No bullets? Luck really is on my side."
            python:
                # increase the number of scenarios survived by 1
                scenariosSurvived += 1 
            python:
                survived_text = "You have survived {} scenario(s).".format(scenariosSurvived)

            "[survived_text]"
                
            jump d2

# this ends t3
return

label badEnd:
    # Got Your Nose ending 
    # End up with all limbs eaten (by not tricking enough).

    scene street0 with fade
    play sound "sfx/cars2.mp3"
    # ridley sprite without limbs
    show ridley with dissolve 

    "Not having the energy or limbs to escape, you try to call out for anyone to help you run away from your fiendish friend." 
    "..."
    "No one ever appears, and you end up crying on the floor."

    charMC "Well, I guess this is it."
    "You think about all the times you were happy and realize that many of those times were due to your friend."

    play sound "sfx/footsteps.mp3"
    "As you slowly drift away, your friend appears on the scene and says."
    play music "music/mystery2.mp3"
    show ash at right with dissolve
    charCan "You always did have the prettiest nose." 

    play sound "sfx/limb-lost.mp3"
    charCan "Let me fix that."
    "You feel a tingling sensation on your face."
    "Suddenly, you realize you lack the power to even breathe."
    "..."
    play music "music/oof.mp3"
    hide ridley with dissolve
    hide ash with dissolve

    "Oops, a Cannibal Got Your Nose!"
    "The End..."
    "You reached the bad end."

    "Results Screen:"

    python:
        remaining_limbs_text = "You had {} limb(s) remaining.".format(limbs)

    "[remaining_limbs_text]"

    python:
        survived_text = "You survived {} scenario(s).".format(scenariosSurvived)

    "[survived_text]"

    python:
        sacrifices_text = "You sacrificed {} person/people.".format(sacrifices)
    
    "[sacrifices_text]"

    if weapon:  
        "You found a weapon."
    else:
        "You didn't find a weapon."

    # This ends the bad end.
    return

label goodEnd:
    # Canni-boom! ending (cannibal gets so full he ends up exploding)
    # Ridley has to have a weapon and has to survive 3 or more scenarios.

    scene street8 with fade
    play sound "sfx/running.mp3"
    show ridley with dissolve

    "As you continue running away, anger starts to creep into your thoughts."
    "Why do I have to keep running away from someone who could never beat me to the last lamb sandwich in the school's canteen?"

    scene street6 with fade
    charMC "I'm so done with this! Can no one help me?"
    "You yell out, hoping someone will hear."
    play sound "sfx/bloody-floor.mp3"
    "Hehehe."
    "You hear someone laugh from not too far away."
    "As you look around, you realize where you've just run into."
    scene alley with fade
    play sound "sfx/footsteps-cannibal.mp3"
    "You noticed a lot of people on the ground, motionless..."
    "Your friend gets closer."
    "You look at your friend, who is now barely visible."
    show ridley with dissolve
    charMC "All of these people..."
    charMC "Was it really you who did this?"
    charCan "I sure have a big appetite."
    charCan "I thought you already knew that."
    "As you try not to throw up from the stench, you attempt to stand your ground."
    charMC "Do you realize what you've just done?" 
    charMC "These were people like you and me." 
    charMC "They had futures!"
    charCan "Don't you realize how much they mocked me when they went to my parents' restaurant and asked them to serve non-vegan food?" 
    charCan "It sickens me to this day how much they enjoy not caring about the world."
    charMC "This has to stop!"
    charCan "I agree." 
    charCan "Chasing you has been quite time-consuming." 
    charCan "I even missed out on my favorite TV show."

    play music "music/determinator.mp3"
    "Now seeing how far your friend had fallen, you decide to take matters into your own hands."
    # inflated ash
    show ash at right with dissolve
    "Ash, now clearly visible, can hardly move as his stomach has ballooned from overeating."
    "Yet, even with a chance to run away, you are determined to end it here."
    play sound "sfx/explosion.mp3"
    "You wield your weapon, and then, your friend blows up in a grotesque manner."
    "You are so shocked by this that you end up unconscious." 

    scene hospital with fade
    play sound "sfx/birds.mp3"
    "The next day, you open your eyes in a hospital bed, nearby you see your parents asleep on some chairs."
    "You turn on the TV to see that the news is talking about how a serial killer was found dead next to his victims."
    "You breathe a sigh of relief as you realize that you no longer have to run away."
    "Yet..."
    "You feel a bit sad about your friend, Ash."

    "The End."
    "You reached the good end."

    "Results Screen:"

    python:
        remaining_limbs_text = "You had {} limb(s) remaining.".format(limbs)

    "[remaining_limbs_text]"

    python:
        survived_text = "You survived {} scenario(s).".format(scenariosSurvived)

    "[survived_text]"

    python:
        sacrifices_text = "You sacrificed {} person/people.".format(sacrifices)
    
    "[sacrifices_text]"

    if weapon: 
        "You found a weapon."
    else:
        "You didn't find a weapon."
    # This ends the good end.
    return

label trueEnd:
    #  Become a Cannibal ending 
    #  Sacrificed/ Tricked 4 or more people.

    scene street7 with fade
    play sound "sfx/running.mp3"
    "After a long night, you find yourself exhausted and in dire need of nutrition." 

    scene bench with fade
    play music "music/dark.mp3"
    "You sit on a bench that was close to you and wonder out loud"
    show ridley with dissolve
    charMC "When will this ever stop?" 
    charMC "I sacrificed so many good people, only for Ash to still be chasing me!"
    play sound "sfx/laugh.mp3"
    "In the distance, you hear sounds of people having fun."
    charMC "This has to be the worst day of my life, and yet they are having a happy day..."
    play music "music/dark.mp3"
    "Suddenly, you hear footsteps of someone approaching close by."
    show ash at right with dissolve
    charCan "Hey! I heard what you were saying."
    charMC "When did you get here?"

    "You get up from the bench to start running away but he grabs you."
    
    charCan "Listen, I didn’t know I was hurting you all this time."
    play music "music/mystery2.mp3" 
    charCan "I just really wanted to get some of your happiness for myself."
    "You give up on running away and sit next to your friend!"
    charMC "Eating me is not the solution to that!" 
    charMC "Have you considered talking to me before?" 
    charMC "About all of this?" 
    charMC "And that happiness, to me, was being friends with you."
    "You continue."
    charMC "Is human meat all that great for you to decide to cut ties with me?"
    "Your friend makes an expression that you've never seen before and says."
    charCan "You don't know until you try it!"
    "Your friend shows you a human arm, and right then and there, you succumb to your exhaustion and decide to eat it."
    "Turns out you liked it."
    charCan "See? We can still be friends, and you get revenge on this city for not having helped you."

    play music "music/oof.mp3"
    "You realize that you are being manipulated, but as you still want to be friends, you decide to go with the flow."
    "Your friend helps you get up and you two make your way to downtown."
    scene street6 with fade
    "You look around at all the people walking around and get hungrier and hungrier. With the help of your friend, you end up going for a midnight snack."

    "The End!"

    "You reached the true end."

    "Results Screen:"

    python:
        remaining_limbs_text = "You had {} limb(s) remaining.".format(limbs)

    "[remaining_limbs_text]"

    python:
        survived_text = "You survived {} scenario(s).".format(scenariosSurvived)

    "[survived_text]"

    python:
        sacrifices_text = "You sacrificed {} person/people.".format(sacrifices)
    
    "[sacrifices_text]"

    if weapon:  
        "You found a weapon."
    else:
        "You didn't find a weapon."

    # This ends the true end.
    return

label noEnd:
    # when you somehow reach no ending
    scene limb-lost with fade
    play music "music/happy.mp3"

    "Congrats!"
    "You got nowhere fast..."
    "Good luck next time!"

    "Results Screen:"

    python:
        remaining_limbs_text = "You had {} limb(s) remaining.".format(limbs)

    "[remaining_limbs_text]"

    python:
        survived_text = "You survived {} scenario(s).".format(scenariosSurvived)

    "[survived_text]"

    python:
        sacrifices_text = "You sacrificed {} person/people.".format(sacrifices)
    
    "[sacrifices_text]"

    if weapon:  
        "You found a weapon."
    else:
        "You didn't find a weapon."
    
    # This ends the no end.
    return
