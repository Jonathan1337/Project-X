#FINAL RUIM

label bad_ending:

    #bad enging: michael volta para o escritorio explica que não conseguiu o aumento e darryl pede demissão
    scene frame_765
    with dissolve
    
    michael "I have some bad news..."

    scene frame_766
    with dissolve

    michael "I didn't get the raise."

    scene frame_768
    with dissolve

    if darryl_respect >= 5:
        darryl "Fine. We'll try again another time, Mike."
        return 
    
    else:
        scene frame_769
        with dissolve
        pause 1.0 

        darryl "Then I'm out. I quit."

    return

    #end game
