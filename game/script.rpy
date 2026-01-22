
define michael = Character("Michael Scott")

define darryl = Character("Darryl Philbin")

define pam = Character("Pam Beesly")

define kevin = Character("Kevin Malone")

define philys = Character("Philys Lapin")

define jim = Character("Jim Halpert")

define karen = Character("Karen Filippelli")

define creed = Character("Creed Bratton")

define jan = Character("Jan Levinson")

define toby = Character("Toby Flenderson")

define stanley = Character("Stanley Hudson")

define hunter = Character("Hunter Raymond")

default jan_affinity = 0
default darryl_respect =3

label splashscreen:
    scene black
    with dissolve
    
    centered "{b}AVISO LEGAL E DE DIREITOS AUTORAIS{/b}\n\n
    Este é um projeto sem fins lucrativos, desenvolvido exclusivamente para fins didáticos e demonstração de habilidades técnicas no motor Ren'Py.\n\n
    {i}The Office{/i} e todos os seus personagens, marcas e imagens são de propriedade da {b}NBCUniversal{/b}. Este software não é afiliado, endossado ou patrocinado pelos detentores dos direitos originais.\n\n
    Este trabalho é um tributo feito por um fâ, com total respeito à obra original."

    pause 3.0 
    
    scene black
    with dissolve
    
    return 



label start:

    stop music fadeout 1.0

    play music "Pam’s-Desk--Ambience.ogg"

    scene frame_1
    with dissolve
    
    michael "..."

    scene frame_2
    with dissolve

    michael "Yeah???"

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

    darryl "(sitting)"

    scene frame_4
    with dissolve

    michael "You know what, actually, let's go into the conference room."

    scene frame_6
    with dissolve
    
    darryl "Ok"

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

    michael "Yeah, let's go to
    the conference room."

    scene frame_11
    with dissolve

    michael "Tactic number six."

    michael "Change the location of the
    meeting at the last second."

    michael "Totally throws them off."

    scene frame_509
    with dissolve

    michael "I am declining to speak first."

    scene frame_522
    with dissolve

    michael "Number 14,
    declining to speak first."

    scene frame_525
    with dissolve

    michael "Makes them feel
    uncomfortable, puts you in control."

    scene frame_509
    with dissolve

    michael "..."

    scene frame_555
    with dissolve

    darryl "Okay, I'll start.
    It's pretty simple, really."

    scene frame_556
    with dissolve

    darryl "I think I deserve a raise."

    scene frame_557
    with dissolve

    darryl "I'm scheduled to
    get one in six months,"

    scene frame_558
    with dissolve

    darryl "but I'd like that
    to be moved up to now."

    scene frame_559
    with dissolve
    pause 1.0

    scene frame_560
    with dissolve
    pause 1.0

    michael "A good worker and a good man."

    scene frame_561
    with dissolve

    michael "I just..."

    scene frame_562
    with dissolve

    michael "You know, times are tight,"

    scene frame_568
    with dissolve

    michael "and I just don't
    think corporate's"

    scene frame_569
    with dissolve

    michael "Going to go for this right now."

    scene frame_588
    with dissolve

    darryl "Are you wearing lady clothes?"

    scene frame_591
    with dissolve

    camera:
        linear 2.0 zoom 2.0 xalign 0.2 yalign 0

    michael "What????"

    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
        #zoom padrão

    scene frame_592
    with dissolve

    darryl "Are you wearing lady clothes?
    Those look like lady pants."

    scene frame_596
    with dissolve

    michael "No. This is a power suit."

    scene frame_603
    with dissolve

    darryl "That there is a woman's suit."

    scene frame_607
    with dissolve

    michael "I do not buy women's clothes."

    scene frame_603
    with dissolve

    darryl "I'm going to call Roy, man."

    scene frame_609
    with dissolve

    michael "Okay. All right."

    scene frame_603
    with dissolve

    darryl "This is going to
    make him feel better."

    scene frame_603
    with dissolve

    darryl "This is too good."

    scene frame_609
    with dissolve

    michael "You know what,
    Pam, would you please"

    scene frame_610
    with dissolve
    #pick some another print of this scene

    michael "Tell darryl that this
    is not a woman's suit?"

    scene frame_613
    with dissolve

    pam "Oh, my god.
    That's a woman's suit."

    scene frame_614
    with dissolve

    kevin "You're wearing a woman's suit?"

    scene frame_619
    with dissolve

    michael "I do...
    I wear men's suits. Okay?"

    scene frame_621
    with dissolve

    michael "I got this out of a bin."

    scene frame_622
    with dissolve

    michael "There were these
    huge bins of clothes,"

    scene frame_623
    with dissolve

    michael "and everybody was riffling
    through them like crazy."

    scene frame_624
    with dissolve

    michael "and i grabbed one"

    scene frame_625
    with dissolve

    michael "And it fit."

    scene frame_626
    with dissolve

    michael "So I don't think that this is
    totally just a woman's suit."

    scene frame_627
    with dissolve

    michael "At the very least,
    it's bisexual."

    scene frame_637
    with dissolve

    kevin "Who makes it?"

    scene frame_641
    with dissolve

    michael "...Mmmysterious"

    scene frame_645
    with dissolve

    michael "It is mysterious, because the
    buttons are on the wrong side."

    scene frame_646
    with dissolve

    michael "That's the mystery."

    scene frame_646
    with dissolve

    philys "Look, it's got shoulder pads.
    And did you see that lining?"

    scene frame_649
    with dissolve

    philys "Okay. Did you see that?"

    scene frame_651
    with dissolve

    michael "Would you stop it, please?"

    scene frame_653
    with dissolve

    jim "So none of that tipped you off?"
    #pick some another print of this scene

    scene frame_655
    with dissolve

    michael "It's European, okay?
    It's a European cut."

    scene frame_658
    with dissolve

    pam "Michael, the pants
    don't have any pockets."

    scene frame_659
    with dissolve

    michael "No, they don't, see?"

    scene frame_660
    with dissolve

    michael "Italians don't wear pockets."

    scene frame_661
    with dissolve

    pam "(laughing...)"

    scene frame_664
    with dissolve

    pam "It's been a really
    rough couple of days."

    scene frame_670
    with dissolve

    pam "This helps a little."

    scene frame_671
    with dissolve

    karen "Hey, maybe you want to
    come over and raid my closet?"

    scene frame_673
    with dissolve

    michael "No, I don't want to do that
    because I'm twice your size anyway."

    scene frame_674
    with dissolve

    camera:
        linear 2.0 zoom 2.5 xalign 0.2 yalign 0

    darryl "Yeah, he look
    like Hillary Clinton."

    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
        #zoom padrão

    #move camera on this scene do focus on darryl

    scene frame_676
    with dissolve

    michael "..."

    scene frame_679
    with dissolve

    michael "Let's just do this in 15."

    scene frame_681
    with dissolve

    darryl "Okay, can you stand
    right there for one second?"

    scene frame_682
    with dissolve

    darryl "I got to send some e-mails."

    scene frame_684
    with dissolve

    michael "Negotiations are
    all about controlling things,"

    scene frame_687
    with dissolve

    michael "about being
    in the driver's seat."

    scene frame_689
    with dissolve

    michael "And you make one
    tiny mistake, you're dead."

    scene frame_695
    with dissolve

    michael "I made one tiny mistake."

    scene frame_700
    with dissolve

    michael "I wore women's clothes."

    scene frame_764
    with dissolve

    michael "Let's get down to business."

    scene frame_765
    with dissolve

    michael "Why don't you tell me why"

    scene frame_766
    with dissolve

    michael "you think you deserve a raise."

    scene frame_768
    with dissolve

    darryl "Well, it's simple, Mike."

    scene frame_769
    with dissolve

    darryl "I mean, we merged"

    scene frame_770
    with dissolve

    darryl "these two branches, right?"

    scene frame_771
    with dissolve

    darryl "So now we're shipping twice"

    scene frame_772
    with dissolve

    darryl "as many orders as we used to."

    scene frame_773
    with dissolve

    darryl "And with Roy gone,"

    scene frame_774
    with dissolve

    darryl "we've got a smaller crew."

    scene frame_775
    with dissolve

    darryl "And I'm picking up"

    scene frame_776
    with dissolve

    darryl "All of his slack,"

    scene frame_777
    with dissolve

    darryl "So I think I should be"

    scene frame_778
    with dissolve

    darryl "Sompensated fairly by getting a raise."

    scene frame_782
    with dissolve

    michael "Well, those are"

    scene frame_787
    with dissolve

    michael "Very good points.(whispering)"

    scene frame_790
    with dissolve

    darryl "What? I can't hear you."

    scene frame_791
    with dissolve

    michael "Those are very good points.(whispering)"

    scene frame_797
    with dissolve

    darryl "I can't...
    What, Mike? Are you..."

    scene frame_855
    with dissolve

    michael "You make a very
    compelling argument."

    scene frame_856
    with dissolve

    michael "I'm going to give
    you a piece of paper."

    scene frame_857
    with dissolve

    michael "I want you to write down
    how much you want."

    scene frame_861
    with dissolve

    michael "Then I want you to slide it
    # back across the desk to me."

    scene frame_864
    with dissolve

    darryl "Why can't I just tell you?"

    scene frame_868
    with dissolve

    michael "Because that is the way
    these things are done in films."

    scene frame_872
    with dissolve

    play sound "Pen-On-Paper.ogg"

    darryl "(scribbling on paper)"

    scene frame_876
    with dissolve
    
    michael "Now slide it. Yes."

    scene frame_877
    with dissolve

    darryl "There you go."

    scene frame_881
    with dissolve

    michael "(reading a paper)"

    scene frame_882
    with dissolve

    michael "Oh, come on. Be serious."

    scene frame_886
    with dissolve

    darryl "I am serious, Mike.
    That's a 10-percent raise."

    scene frame_887
    with dissolve

    darryl "That's what I want."

    scene frame_889
    with dissolve
    
    michael "I can't give you that."

    scene frame_893
    with dissolve

    michael "I don't make this much."

    scene frame_895
    with dissolve

    darryl "Come on, be for real, Mike."

    scene frame_896
    with dissolve

    michael "I don't. I'll prove it to you."

    scene frame_898
    with dissolve

    michael "There is a pay stub."

    scene frame_901
    with dissolve

    darryl "(laughing)"

    scene frame_903
    with dissolve

    darryl "Are you serious?
    You're earning this?"

    scene frame_905
    with dissolve

    michael "Plus perks."

    scene frame_907
    with dissolve

    michael "Yes."

    scene frame_908
    with dissolve

    darryl "Mike, this is barely
    more than I make."

    scene frame_911
    with dissolve

    darryl "You've been here
    ten years, dawg."

    scene frame_910
    with dissolve

    darryl "(laughing)"

    scene frame_915
    with dissolve

    michael "**Fourteen years.**"

    scene frame_918
    with dissolve

    darryl "(Aiming his celphone to take a picture of pay stub)"

    scene frame_922
    with dissolve

    michael "No, please, please don't."

    scene frame_920
    with dissolve

    darryl "I'm sorry, Mike. Some mofos
    got to hear about this one."

    scene frame_924
    with dissolve

    michael "Okay. Let's take 15 again."

    scene frame_925
    with dissolve

    michael "A boss' salary
    isn't just about money."

    scene frame_930
    with dissolve

    michael "It is about perks. It..."

    scene frame_932
    with dissolve

    michael "For example, every year. I get a $100 gas card."

    scene frame_935
    with dissolve

    michael "Can't put a price tag on that."

    scene frame_990
    with dissolve

    kevin "Michael?"

    scene frame_992
    with dissolve
    
    kevin "Here's the $15 I owe you."

    scene frame_994
    with dissolve
    
    michael "Yeah. Thank you."

    scene frame_995
    with dissolve
    
    kevin "I heard you might need it, so..."

    scene frame_1002
    with dissolve
    
    creed "Here's the $40 you gave me."

    scene frame_1003
    with dissolve

    michael "I didn't give you $40."

    scene frame_1005
    with dissolve
    
    creed "In a way, you did."

    scene frame_1007
    with dissolve

    camera:
        linear 2.0 zoom 1.5 xalign 0.2 yalign 0
        

    michael "..."

    camera:
        zoom 1.0 xalign 0.5 yalign 0.5
        #zoom padrão

    scene frame_1010
    with dissolve

    stanley "Yeah. I heard how much Michael makes."

    scene frame_1014
    with dissolve
    
    stanley "I still think he's way overpaid."

    scene frame_1016
    with dissolve

    darryl "(laughing)"

    scene frame_1017
    with dissolve

    darryl "Fourteen years."

    scene frame_1016
    with dissolve

    darryl "Fourteen."

    scene frame_1022
    with dissolve

    darryl "I know."

    scene frame_1023
    with dissolve

    darryl "Okay, all right, I got to go. Late."

    scene frame_1025
    with dissolve

    michael "..."

    scene frame_1027
    with dissolve

    michael "Okay. Okay. Here's the straight dope."

    scene frame_1031
    with dissolve

    michael "No tricks, no Wikipedia."

    scene frame_1032
    with dissolve

    darryl "What?"

    scene frame_1034
    with dissolve

    michael "I talked to corporate and they told me that"

    scene frame_1038
    with dissolve

    michael "I can only give you a five-percent raise."

    scene frame_1041
    with dissolve

    darryl "That's 'cause of you, Mike.
    They're not going to give the working man more than the boss."

    scene frame_1045
    with dissolve

    michael "Well, what am I supposed to do?"

    scene frame_1046
    with dissolve

    darryl "Get your own raise."

    scene frame_1047
    with dissolve

    darryl "You've got to get out there and earn, son."

    scene frame_1048
    with dissolve

    michael "I'm not going to go out and ask for a raise right now."

    scene frame_1049
    with dissolve

    michael "That is ridiculous."

    scene frame_1052
    with dissolve

    darryl "Well, when they merged the two branches together,
    they put you in charge."

    scene frame_1055
    with dissolve

    darryl "Okay? And we're shipping more now than we ever have."

    scene frame_1058
    with dissolve

    michael "That's true." 

    scene frame_1060
    with dissolve
    
    darryl "Yeah, that's true."

    scene frame_1061
    with dissolve

    darryl"You got to call your girl and get paid."

    scene frame_1064
    with dissolve

    darryl"Show her who wears the pants in the relationship."

    scene frame_1068
    with dissolve

    michael "You know what, I should."

    scene frame_1069
    with dissolve

    darryl "Yeah, you should."

    scene frame_1072
    with dissolve

    michael "I've been a loyal employee for a long time."

    scene frame_1074
    with dissolve

    darryl "Fourteen years long."

    scene frame_1076
    with dissolve

    michael "You know what, I deserve a bump."

    scene frame_1077
    with dissolve

    darryl "Make it happen, captain."

    scene frame_1080
    with dissolve

    michael "I am making it happen, sergeant."

    #text fault

    scene frame_1113
    with dissolve

    jan "Well, why don't we talk next month after the quarter ends?"

    #darryl shaking his head in desaproving signal

    scene frame_1121
    with dissolve

    michael "No, jan."

    scene frame_1126
    with dissolve

    michael "I've never asked for a raise in 14 years.
    This is long overdue. "

    scene frame_1155
    with dissolve
    
    michael"I want to do it today."

    scene frame_1155
    with dissolve

    jan "Today?"

    scene frame_1156
    with dissolve
     
    jan "All right, well, if you want to do it today, we should do it in person,
    and can you get here by 5:00?"

    scene frame_1155
    with dissolve

    michael "Yeah. Yeah, I'll leave right away."

    scene frame_1156
    with dissolve

    jan "Great!
    And listen, because of our, you know, situation,
    we're going to need to have a third party present."

    scene frame_1157
    with dissolve

    michael "Yes. I'm bringing Darryl."

    scene frame_1158
    with dissolve

    jan "Darryl from the warehouse? Mmm-hmm."

    scene frame_1159
    with dissolve

    jan "No, Michael, we... We need an hr rep,
    so I think you should just bring Toby."

    scene frame_1160
    with dissolve

    michael "Hey, I'd rather kill myself."

    scene frame_1161
    with dissolve

    jan "Michael, he's your branch's hr rep...
    And we need someone else in the room...Because of our relationship. Michael!"

    scene frame_1162
    with dissolve

    michael "No, Toby is terrible.Toby is the worst human being I've ever known."

    scene frame_1163
    with dissolve
   
    jan "Either Toby comes with you or we don't do it."

    scene frame_1168
    with dissolve

    michael "Fine."
    jump jan_negociation

    return

label jan_negociation:

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
    darryl "Yes, sir. Remember that. I'll be right outside if you need me.
    All right?!"

    scene frame_1302
    with dissolve
    darryl "Yeah. Itaught Mike some new phrases."

    scene frame_1303
    with dissolve
    darryl "I want him to get the raise." 
    
    scene frame_1304
    with dissolve

    darryl"I just can't help myself."

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

    return

label good_ending:

    play music "John-Jermaine-Jazz.ogg"

    michael "Negotiation is an art."

    scene frame_1692
    with dissolve

    michael "Back and forth. Give and take."

    scene frame_1693
    with dissolve

    michael "And today, both Darryl and I took something."

    scene frame_1694
    with dissolve

    michael "Higher salaries."

    scene frame_1695
    with dissolve

    michael "Win, win, win."

    scene frame_1696
    with dissolve

    michael "But, you know, life is about more than just salary."

    scene frame_1697
    with dissolve

    michael "It's about perks."

    scene frame_1698
    with dissolve

    michael "Like having sex with jan..."

    scene frame_1700
    with dissolve

    jan "Michael."

    return

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

    #end game

    return


screen credits():
    tag menu 
    add "black" 
    
    vbox:
        align (0.5, 0.4)
        spacing 20
        
        text "{b}CREDITS{/b}" size 60 xalign 0.5 color "#fff"
        
        null height 20
        
        text "Developed by: Jonathan S. França" xalign 0.5
        
        null height 10
        
        text "{b}Technologies used:{/b}" xalign 0.5
        text "Engine: Ren'Py" xalign 0.5 # 
        text "Language: Python" xalign 0.5 # 
        
        null height 10
        
        text "Inspired by: The Office (NBCUniversal)" xalign 0.5
        text "Purpose: Technical Portfolio & Skill Demonstration" xalign 0.5
        
    textbutton _("Return"):
        align (0.5, 0.8)
        action Return()
        text_size 40
        text_hover_color "#00ff00" 