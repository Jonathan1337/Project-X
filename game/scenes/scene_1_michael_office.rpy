#CENA 1: INICIO A PARTIR DA SALA DO MICHAEL

label scene_1:

    stop music fadeout 1.0

    play music "Pam’s-Desk--Ambience.ogg"

    scene frame_1
    with dissolve
    
    "..."

    scene frame_2
    with dissolve

    michael "(Knock on door) Yeah?"

    scene frame_3
    with dissolve

    darryl "You ready for me?"

    scene frame_4
    with dissolve

    menu:
        "Yes, yeah. Absolutely. Have a seat.":
            pass 

        "No, I'm busy":
            scene frame_5
            darryl "I'm coming in anyway."

    scene frame_5
    with dissolve

    "(sitting)"

    scene frame_4
    with dissolve

    michael "You know what, actually, let's go into the conference room."

    scene frame_6
    with dissolve

    "..."

    scene frame_7
    with dissolve

    michael "No, you know what, let's stay here."

    scene frame_9

    darryl "..."

    scene frame_7
    with dissolve

    michael "Let's go."

    scene frame_8
    with dissolve

    michael "Yeah, let's go to the conference room."

    scene frame_11
    with dissolve

    michael "Tactic number six."

    michael "Change the location of the meeting at the last second."

    michael "Totally throws them off."

    jump scene_2

