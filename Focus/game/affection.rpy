init python: 

    def changeAffectionHans(stat, suitor1_relationship):
            if suitor1_relationship > 0:
                suitor1_relationship += 1 
                renpy.notify("A afeição de [h] aumentou!")
            else: 
                renpy.notify("A afeição de [h] diminuiu!")
            stat += suitor1_relationship
            return stat 
    def changeAffectionArthur(stat, suitor2_relationship): 
            if suitor2_relationship > 0: 
                suitor2_relationship += 1
                renpy.notify("A afeição de [a] aumentou!")
            else: 
                renpy.notify("A afeição de [a] diminuiu!")
            stat += suitor2_relationship
            return stat 
    def changeAffectionLuna(stat, suitor3_relationship):
            if suitor3_relationship > 0: 
                suitor3_relationship += 1
                renpy.notify("A afeição de [lm] aumentou!")
            else: 
                renpy.notify("A afeição de [lm] diminuiu!")
            stat += suitor3_relationship
            return stat 
    
    def changeAffectionOliver(stat, suitor4_relationship):
            if suitor4_relationship > 0: 
                suitor4_relationships += 1
                renpy.notify("A afeição de [og] aumentou!")
            else: 
                renpy.notify("A afeição de [og] diminuiu!")
            stat += suitor4_relationship
            return stat
    
    def changeAffectionVictor(stat, suitor5_relationship):      
            if suitor5_relationship > 0: 
                suitor5_relationship += 1
                renpy.notify("A afeição de [vl] aumentou!")
            else: 
                renpy.notify("A afeição de [vl] diminuiu!")
            stat += suitor5_relationship
            return stat
    def changeAffectionDaph(stat, suitor6_relationship):
        if suitor6_relationship > 0:
            suitor6_relationship += 1
            renpy.notify("A afeição de [dl] aumentou!")
        else: 
            renpy.notify("A afeição de [dl] diminuiu!") 
        stat += suitor6_relationship
        return stat         
    
