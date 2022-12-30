
################################################################################
## Variable Declaration.
################################################################################
define n = Character("Narrator", color="#000000")
define h = Character("Hans Morgan", color="#7851a9")
define a = Character("Arthur Muslock", color"#000080")
define lh = Character("Leona Husk", color="#FF0000")
define lm = Character("Luna Moonson", color="#301934")
define hb = Character("Hudson Bayern", color="#808080")
define op = Caracter("Olaf Pogrom", color="#FFC000")
define og = Character("Oliver Garfield", color="#722F37")
define vl = Character("Victor Laurent", color="#FFA500")
define dl = Character("Daphny Laurent", color="#E0115F") 
define li = Character("Player", color="#E9DFE0")
################################################################################
### Misc. 
################################################################################

################################################################################
## Main Menu and Initialization, the game will start here. 
################################################################################
label start: 
    n "Welcome, to Focus!" 

    menu: 
        "Start Game"
            jump game

    label game: 
        
        scene bg room 
        show elieen happy 

        n "It was still cold when Lilith woke up, her feet freezing outside her blanket. She yawned scanning the room."
        li "Damn, I had a nightmare. Again"

return 
