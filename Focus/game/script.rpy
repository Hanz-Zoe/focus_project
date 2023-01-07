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

$ affection_points = 0
$ affection_points += 1
################################################################################
## Functions. 
################################################################################

#Função que governa a feição dos personagens.# 
init python: 
    def change_stataffection(stat, amount):
        if amount > 0: 
            renpy.notify("[n] aumentou a afeição por você" )
        else: 
            renpy.notify("[n] diminiu a afeição por você")
            stat += amount
            return stat


################################################################################
## Conditions 
################################################################################
$ affection = True 

################################################################################
## Game. 
################################################################################
label start: 


return
#That's all folks! For the time being!
