################################################################################
## Variable Declaration.
################################################################################
define n = Character("Narrator", color="#000000")
define h = Character("Hans Morgan", color="#7851a9")
define a = Character("Arthur Muslock", color="#000080")
define lh = Character("Leona Husk", color="#FF0000")
define lm = Character("Luna Moonson", color="#301934")
define hb = Character("Hudson Bayern", color="#808080")
define op = Character("Olaf Pogrom", color="#FFC000")
define og = Character("Oliver Garfield", color="#722F37")
define vl = Character("Victor Laurent", color="#FFA500")
define dl = Character("Daphny Laurent", color="#E0115F") 
define li = Character("[name]", color="#E9DFE0")

#image bg lanchonete = ""
#image bg empresa  = "" ****BAD DESCOMNTA E COLOCA O CAMINHO DAS IMAGENS QUANDO TIVER.****
################################################################################
## Functions. 
################################################################################

 
            

################################################################################
## Conditions 
################################################################################
 

################################################################################
## Game. 
################################################################################
label start: 


return
label Empresa
    hide bg lanchonete
    scene bg empresa:
        zoom 1.5
    with dissolve
call screen Lanchonete
    if _return == "Empresa": 
        jump Empresa
    elif _return == "Lanchonete" :
        jump Lanchonete
        

screen lanchonete: 
    imagemap: 
        ground #"coloque a imagem da lanchonete aqui"
        hover #"colocar o caminho da imagem do botão a ser clicado"
        hotspot() action Return("Empresa")#colocar as coordenadas onde o jogo registrat o clique, e também retorna o valor da próxima sala
        hotspot() action Return("Lanchonete")   



label levelup(target_label="start"):
    if exp >= 500:
        if level == 1: 
            $level = 2 
            "Level up!"
    if exp>=1000 
        if level ==2:
            $level = 3
            "Level up!"
    if exp >= 1500 
        if level ==3:
            $level = 4
            "level up!"
    if exp >= 1500
        if level == 4:
            $level = 5
            "Level up! "
    jump expression target_label
    label end: 
        return
#That's all folks! For the time being!
