#CENA 6: Recepção no escritório central

label scene_6:
    
    play music "Pam’s-Desk--Ambience.ogg"

    scene frame_1268
    with dissolve
    pause 1.0

    scene frame_1269
    with dissolve
    pause 1.0

    scene frame_1270
    with dissolve
    pause 1.0

    scene frame_1271
    with dissolve
    pause 1.0

    scene frame_1272
    with dissolve
    pause 1.0
   
    scene frame_1282
    with dissolve
    pause 1.0

    hunter "Hey, guys. Jan is ready for you."

    scene frame_1283
    with dissolve
    michael "Okay."

    scene frame_1286
    with dissolve
    darryl "Okay. Bring it home now."

    scene frame_1287
    with dissolve
    darryl "And don't forget the new black-man phrase I taught you."
    #create a interaction in this scene

    scene frame_1288
    with dissolve
    
    menu:
        "Pippety poppety, give me the zoppety.":
            $ darryl_respect += 2
            michael "Pippety poppety, give me the zoppety!"

        "Up, Up and Away!":
            $ darryl_respect -=1


    scene frame_1293
    with dissolve
    darryl "Yes, sir. Remember that." 

    scene frame_1294
    with dissolve
    
    darryl "I'll be right outside if you need me."

    scene frame_1296
    with dissolve

    darryl "All right."

    scene frame_1302
    with dissolve
    darryl "Yeah. Itaught Mike some new phrases."

    scene frame_1303
    with dissolve
    darryl "I want him to get the raise." 
    
    scene frame_1304
    with dissolve

    darryl"I just can't help myself."

    jump scene_7

