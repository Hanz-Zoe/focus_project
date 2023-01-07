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

init: 
    $ suitor1_relationship = 0 
    $ suitor2_relationship = 0 
    $ suitor3_relationship = 0 
    $ suitor4_relationship = 0 
    $ suitor5_relationship = 0 
    $ suitor6_relationship = 0 
################################################################################
## Functions. 
################################################################################
label hans_afeicao: 
    $ def changeStateAffection(stat, amount):
        if amount > 0: 
            suitor1_relationship += 1
            renpy.notify("a afeição de [h] aumentou!")
        else: 
            renpy.notify("a afeição de [h] diminuiu")
            stat += amount 
            return stat
    return 
label artur_afeicao: 
    $ def changeStateAffection(stat, amount):
        if amount > 0: 
            suitor2_relationship += 1
            renpy.notify("a afeição de [a] aumentou!")
        else: 
            renpy.notify("a afeição de [a] diminuiu")
            stat += amount 
            return stat
    return 
label luna_afeicao: 
    $ def changeStateAffection(stat, amount):
        if amount > 0: 
            suitor3_relationship += 1
            renpy.notify("a afeição de [lm] aumentou!")
        else: 
            renpy.notify("a afeição de [lm] diminuiu")
            stat += amount 
            return stat
    return 
label oliver_garfield: 
    $ def changeStateAffection(stat, amount):
        if amount > 0: 
            suitor4_relationship += 1
            renpy.notify("a afeição de [og] aumentou!")
        else: 
            renpy.notify("a afeição de [og] diminuiu")
            stat += amount 
            return stat
    return 
label victor_laurent: 
    $ def changeStateAffection(stat, amount):
        if amount > 0: 
            suitor5_relationship += 1
            renpy.notify("a afeição de [vl] aumentou!")
        else: 
            renpy.notify("a afeição de [vl] diminuiu")
            stat += amount 
            return stat
    return 
label daphny_laurent: 
    $ def changeStateAffection(stat,amount): 
        if amount > 0:
            suitor6_relationship += 1 
            renpy.notify("a afeição de [dl] aumentou!")
        else: 
            renpy.notify("a afeição de [dl] diminuiu")
            stat += amount
            return stat 
    return 
            

################################################################################
## Conditions 
################################################################################
 

################################################################################
## Game. 
################################################################################
label start: 


return
#That's all folks! For the time being!
