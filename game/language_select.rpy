## Language Selection - Splashscreen
## Aparece apenas na primeira vez que o jogo é aberto

default persistent.language_selected = False

screen language_select():
    add "#1a1a2e"
    
    vbox:
        align (0.5, 0.5)
        spacing 40
        
        text "Get Your Raise" size 64 color "#FFFFFF" xalign 0.5
        text "Select your language" size 32 color "#AAAAAA" xalign 0.5
        
        null height 40
        
        vbox:
            xalign 0.5
            spacing 20
            
            textbutton "English":
                xminimum 300
                xalign 0.5
                action [SetVariable("persistent.language_selected", True), 
                        Language(None), 
                        Return()]
                style "language_button"
            
            textbutton "Português":
                xminimum 300
                xalign 0.5
                action [SetVariable("persistent.language_selected", True), 
                        Language("portuguese"), 
                        Return()]
                style "language_button"
        
        null height 60
        text "You can change this later in Preferences" size 18 color "#666666" xalign 0.5

style language_button:
    xalign 0.5
    padding (40, 15)
    background "#2d2d44"
    hover_background "#4a4a6a"
    
style language_button_text:
    size 28
    color "#FFFFFF"
    xalign 0.5

