screen warning_intro_scr():
    style_prefix "warning_intro"
    frame:
        background Solid("#000000BF")
        xmaximum 800
        xalign 0.5
        yalign 0.5
        
        padding 25, 25
        vbox:
            spacing 10
            xalign 0.5
            text _("Warning!"):
                size 70
                
            text _("This is a non-profit project, developed exclusively for educational purposes and to demonstrate technical skills in the Ren'Py engine.")
            
            text _("The Office and all its characters, trademarks, and images are the property of NBCUniversal.")
            
            text _("This software is not affiliated with, endorsed by, or sponsored by the original rights holders.")
            

style warning_intro_text:
    size 35
    text_align 0.5
    xalign 0.5

label splashscreen:
    ## Seleção de idioma (apenas na primeira vez)
    if not persistent.language_selected:
        scene black
        call screen language_select
    
    ## Warning/Disclaimer
    scene black
    show screen warning_intro_scr
    pause 
    hide screen warning_intro_scr
    return

    