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
            text _(_("Aviso!")):
                size 70
                
            text _("Este é um projeto sem fins lucrativos, desenvolvido exclusivamente para fins didáticos e demonstração de habilidades técnicas no motor Ren'Py.")
            
            text _("The Office") + " e todos os seus personagens, marcas e imagens são de propriedade da " + _("NBCUniversal") + "."
            
            text _("Este software não é afiliado, endossado ou patrocinado pelos detentores dos direitos originais.")
            

style warning_intro_text:
    size 35
    text_align 0.5
    xalign 0.5

label splashscreen:
    scene black
    show screen warning_intro_scr
    pause 
    hide screen warning_intro_scr
    return

    