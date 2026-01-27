#CENA 7: NEGOCIAÇÃO COM A JAN

label scene7:

    scene frame_1384
    with dissolve

    scene frame_1385
    with dissolve
    pause 1.0

    scene frame_1386
    with dissolve
    pause 1.0

    scene frame_1391
    with dissolve

    jan "Thank you, hunter."

    scene frame_1395
    with dissolve
    
    jan "Hello. Come in."

    scene frame_1396
    with dissolve
    
    jan "Okay."

    scene frame_1401
    with dissolve
    
    michael "Who is the boy toy?"

    menu:
        "Get jealous of Hunter":
            $ jan_affinity -= 2
            michael "Were you going to tell me that you hired a model to be your assistant?"
            scene frame_1402
            with dissolve
    
            jan "That's my new assistant."

            scene frame_1410
            with dissolve
    
            jan "I have to call you the second I get a new assistant now?"

            scene frame_1416
            with dissolve
    
            michael "Be nice to get a memo. We are lovers."
        
        "Ignore Hunter and focus on Jan":
            $ jan_affinity += 2

            scene frame_1393
            with dissolve

            michael "Jan, you look powerful today. Like a boss. A girl boss."

            scene frame_1397
            with dissolve

            jan "(Sighs) Let's just start, Michael."


    scene frame_1409
    with dissolve
    
    toby "Hi, jan."

    scene frame_1412
    with dissolve
    
    jan "Hi, Toby."

    scene frame_1415
    with dissolve
    
    jan "(Clearing throat)"

    scene frame_1416
    with dissolve

    michael "(Clearing throat) "

    scene frame_1418
    with dissolve

    jan "First off, Michael, this is a salary negotiation."

    menu:
        "Use the 'Silence Tactic' (Tactic #8)":
            scene frame_1409
            with dissolve    
            
            $ jan_affinity += 1
            "Michael stays silent for 10 seconds, staring intensely at Jan."

            scene frame_1419
            with dissolve

            jan "Michael? Why you ?"

            scene frame_1427
            with dissolve
            michael "I'm negotiating, Jan. It's the power of silence."

            scene frame_1431
            with dissolve

            jan "Good God... okay. Let's just get to the numbers."
        
        "Reclamar do salário do Darryl":

            scene frame_1439
            with dissolve
            $ darryl_respect -= 3
            michael "Darryl makes almost as much as I do! And he wears shorts to work!"

            scene frame_1440
            with dissolve
            jan "Darryl manages the warehouse, Michael. It's a completely different pay scale."



    menu:
        "Say darryl's phrase":
            $ jan_affinity -=1
            scene frame_1439
            with dissolve
            michael "Bippety, boppety."

        "Just say ok":
            scene frame_1443
            with dissolve

            $ jan_affinity +=1
            michael "Ok."

    scene frame_1431
    with dissolve
    pause 1.0

    jan "Right now, we can offer you a six-percent raise."

    scene frame_1434
    with dissolve

    michael "Six percent? After all we've been through?"

    scene frame_1441
    with dissolve

    michael "Oh, god. I got you Jade earrings."

    scene frame_1424
    with dissolve

    jan "Michael. "

    scene frame_1415
    with dissolve

    michael "No."

    scene frame_1424

    jan "Michael"

    scene frame_1425

    michael "No." 

    scene frame_1424

    jan "Michael."

    scene frame_1425

    michael "No!"

    scene frame_1434
    with dissolve

    michael "You're going to play it like this?"

    scene frame_1441
    michael "You give me a good raise or no more sex."

    menu:
        "Double down on the threat (Risky)":
            $ jan_affinity -= 5
            $ darryl_respect = 2
            $ threatened_sex = True
        
        "Apologize immediately":
            $ threatened_sex = False
            $ jan_affinity += 1
            michael "I... I didn't mean that. It was Tactic Number 4. The 'Empty Threat'."
            jan "Don't ever do that again, especially in front of HR."

    if threatened_sex:
        scene frame_1447
        with dissolve
        pause 1.0
        jan "..."
        scene frame_1449
        michael "What are you writing, perv-ball?"

        scene frame_1455
        with dissolve
        
        toby "Just preparing for the deposition."

        scene frame_1456
        with dissolve
        
        toby "This may the first time that a male subordinate has attempted to get a modest, scheduled raise
        by threatening to withhold sex from a female superior."

        scene frame_1465
        with dissolve
        
        toby "It will be a groundbreaking case
        when it inevitably goes to trial."
    
    scene frame_1585
    with dissolve
    
    michael "Why don't you just take that pen and stab me in the heart?"

    scene frame_1586
    with dissolve
    
    michael "This is me, jan. This is me."

    scene frame_1587
    with dissolve
    
    jan "Okay. Michael, please."

    scene frame_1587
    with dissolve
    
    jan "You know, why don't we just take a break?"

    scene frame_1588
    with dissolve

    michael "Okay. This is..."

    scene frame_1589
    with dissolve
    michael "This is going nowhere. No. No. No."

    scene frame_1590
    with dissolve

    michael "You do not try tactic number eight on me."

    scene frame_1591
    with dissolve

    michael "I invented tactic number eight."

    scene frame_1592
    with dissolve

    michael "I'm not going anywhere."

    scene frame_1598
    with dissolve

    jan "Okay, Toby, how about if you..."

    scene frame_1599
    with dissolve

    toby "Sure." 

    scene frame_1603
    with dissolve

    jan "Great."

    scene frame_1605
    with dissolve

    jan "(thinking)...."

    scene frame_1607
    with dissolve

    jan "What's wrong with you?"

    scene frame_1609
    with dissolve

    michael "I don't know. Was a weird day."

    scene frame_1610
    with dissolve

    michael "I accidentally cross-dressed."

    scene frame_1611
    with dissolve

    michael "And then Darryl made me feel bad for not making any money."

    scene frame_1612
    with dissolve

    michael "And then I had to ride up here with stupid Toby."

    scene frame_1613
    with dissolve

    michael "And then your assistant is all young and hot and I..."

    scene frame_1616
    with dissolve

    jan "Okay, Michael."

    scene frame_1628
    with dissolve

    jan "I can offer you a 12-percent raise, but you have got to ask for 15."

    menu:
        "Follow Jan's Plan":
            $ jan_affinity += 5
            $ darryl_respect += 5

            scene frame_1635
            with dissolve
            michael "I demand 15 percent! I won't settle for a penny less!"

            scene frame_1643
            with dissolve

            jan "No, but we can offer you 12."

            scene frame_1654
            with dissolve
            michael "I accept your counter-offer with dignity."
        
        "Try to get more":
            $ jan_affinity -= 3

            scene frame_1648
            with dissolve
            michael "Actually, I want 20 percent! I'm worth it!"

            scene frame_1673
            with dissolve
            pause 1.0
            jan "Michael, I'm literally handing you a lifeline and you're choking it."
        
    scene frame_1675
    with dissolve
    pause 1.0

    if jan_affinity >= 5:
        jump good_ending
    else:
        jump bad_ending
