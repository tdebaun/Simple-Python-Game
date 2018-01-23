# -*- coding: utf-8 -*-
"""
A simple text based game inspired by the Fire Emblem series

@author: Tom DeBaun
"""
from random import randint

#Initialize the weapons list
weaponlist = ["Axe", "Sword", "Lance", "Bow", "Magic"]

#Initialize the end condition
end = False

#Define the fighter class
class fighter:
    def __init__(self, name, wt, atk, skl, spd, dfn, res, rng, hp):
        self.name = name
        self.wt = wt
        self.atk = atk
        self.skl = skl
        self.spd = spd
        self.dfn = dfn
        self.res = res
        self.rng = rng
        self.hp = hp
        self.adv = False
        self.dmg = 0

#Define the show stats function
def showstats(char):
    print("%s, %s Fighter, stats - %d attack, %d skill, %d speed, %d defense, %d resistance, range %d, %d Hp"  %(char.name, char.wt, char.atk, char.skl, char.spd, char.dfn, char.res, char.rng, char.hp))

#Define the fight function
def fight(a, b):
    print("%s's turn" % (a.name))
    if randint(0,10) + (b.spd / 2) < a.skl + randint(0, 5):
        if randint(0, 10) == a.skl:
            b.hp -= (a.dmg * 2)
            print("Critical Hit! %s deals %d damage to %s, %d hp remaining" %(a.name, (a.dmg * 2), b.name, b.hp))
        else:
            b.hp -= a.dmg
            print("%s attacks dealing %d damage, %s has %d hp remaining" %(a.name, a.dmg, b.name, b.hp))
    else:
        print ("%s misses" %(a.name))
    if a.rng == b.rng and randint(0,10) + (a.spd / 2) < b.skl + randint(0, 5):
        if randint(0, 10) == b.skl:
            a.hp -= (b.dmg * 2)
            print("Critical Hit! %s deals %d damage to %s, %d hp remaining" %(b.name, (b.dmg * 2), a.name, a.hp))
        else:
            a.hp -= b.dmg
            print("%s counterattacks dealing %d damage, %s has %d hp remaining" %(b.name, b.dmg, a.name, a.hp))
    elif a.rng == b.rng:
        print ("%s misses" %(b.name))
    if a.spd > b.spd and randint(0,10) + (b.spd / 2) < a.skl + randint(0, 5):
        if randint(0, 10) == a.skl:
            b.hp -= (a.dmg * 2)
            print("Critical Hit! %s deals %d damage to %s, %d hp remaining" %(a.name, (a.dmg * 2), b.name, b.hp))
        else:
            b.hp -= a.dmg
            print("%s attacks again dealing %d damage, %s has %d hp remaining" %(a.name, a.dmg, b.name, b.hp))
    elif a.spd > b.spd:
        print ("%s misses" %(a.name))

#Define a function to check the end condition for use after each fight
def checkend(a, b):
    if a.hp > 0 and b.hp <= 0:
        print ("%s wins" %(a.name))
        return True
    elif b.hp > 0 and a.hp <= 0:
        print ("%s wins" %(b.name))
        return True
    elif a.hp <= 0 and b.hp <= 0:
        print ("both fighters died")
        return True

#Define a function to run fight between two fighters
def combat(a, b):
    turn = 1
    end = False
    print("Combat between ")
    
    showstats(a)
    print ("And")
    showstats(b)
    
    print(" ")
    
    checkadv(a, b)
    
    print(" ")
    
    while end == False:
        print("Round %s" %(str(turn)))
        print(" ")
        
        fight(a, b)
        if checkend(a, b) == True:
            break
        
        print(" ")
        
        fight(b, a)
        if checkend(a, b) == True:
            break
        
        print(" ")
        
        if input("Continue Combat? ") == "no":
            print("A fighter has withdrawn")
            break
        
        turn += 1
        
        
        print(" ")
  
#Define a function to have a pre-generated fighter fight randomly generated
# opponents until they lose      
def arena(a):
    turn = 1
      
    b = fighter("", "", 1, 1, 1, 1, 1, 1, 1)
    arenastats(b)
    defeated = 0
    
    print(" ")
    
    print("Combat between ")
    
    showstats(a) 
    print("And")
    showstats(b)
    
    print(" ")

    checkadv(a, b)
    
    print(" ")
    
    while a.hp > 0 and b.hp > 0:
        
        print("Round %s" %(str(turn)))
        
        print(" ")
        
        fight(a, b)
            
        print(" ")
        
        if b.hp > 0 and a.hp > 0:
            fight(b, a)
        
        print(" ")
           
        if b.hp > 0 and a.hp <= 0:
            print ("%s wins, %s defeated %d enemies before falling in battle" %(b.name, a.name, defeated))
            break
        elif a.hp <= 0 and b.hp <= 0:
            print ("both fighters died, %s defeated %d enemies before falling in battle" %(a.name, defeated))
            break
        
        elif a.hp > 0 and b.hp <= 0:
            print ("%s wins" %(a.name))
            defeated += 1
            cont = input("%s has %d hp remaining, %d enemies defeated, Would you like to continue figthing? " %(a.name, a.hp, defeated))
            if cont == "yes":
                print(" ")
                if 25 <= (a.hp + 5):
                    print("%s was not healed" %(a.name))
                else:
                    healing = randint(3,8)
                    a.hp += healing
                    print("%s was healed for %d hp" %(a.name, healing))
                print(" ")
                arenastats(b)
                turn = 0
                checkadv(a, b)
            else:
                print("%s has withdrawn" %(a.name))
                break
        if input("Continue Combat? ") == "no":
            print("%s has withdrawn" %(a.name))
            break
        
        turn += 1
        
        
        print(" ")

#Define a function to generate stats for an arena opponent
def arenastats(char):
    char.dfn = randint(4, 11)
    char.res = randint(2, 9)
    char.wt = weaponlist[randint(0,4)]
    if char.wt == "Axe" or char.wt == "Sword" or char.wt == "Lance":
        char.rng = 1
    elif char.wt == "Magic" or char.wt == "Bow":
        char.rng = 2
    if char.wt == "Magic":
        char.atk = randint(4, 15)
    else:
        char.atk = randint(8, 19)
    char.name = "%s Fighter" %(char.t)
    char.skl = randint(2, 10)
    char.spd = randint(1, 8)
    char.hp = randint(20, 36)
    showstats(char)

#Define a function to create a stronger character to fight the arena with
#This character can be re-rolled            
def herostats(char):
     char.name = input("Enter a name for this fighter: ")
     statsgood = False
     while statsgood == False:
        char.dfn = randint(5, 13)
        char.res = randint(4, 10)
        wt = weaponlist[randint(0,4)]
        char.wt = wt
        if wt == "Axe" or  wt == "Sword" or wt == "Lance":
            char.rng = 1
        elif wt == "Magic" or wt == "Bow":
            char.rng = 2
        if char.wt == "Magic":
            char.atk = randint(6, 16)
        else:
            char.atk = randint(10, 20)
        char.skl = randint(3, 10)
        char.spd = randint(2, 9)
        char.hp = randint(25, 41)
        showstats(char)
        if input("generate new stats? ") == "no":
            statsgood = True            

#Define a function to create a stronger character that can't be re-rolled            
def randherostats(char):
     char.name = input("Enter a name for this fighter: ")
     char.dfn = randint(5, 13)
     char.res = randint(4, 10)
     wt = weaponlist[randint(0,4)]
     char.wt = wt
     if wt == "Axe" or  wt == "Sword" or wt == "Lance":
         char.rng = 1
     elif wt == "Magic" or wt == "Bow":
         char.rng = 2
     if char.wt == "Magic":
         char.atk = randint(9, 17)
     else:
         char.atk = randint(10, 20)
     char.skl = randint(3, 9)
     char.spd = randint(2, 7)
     char.hp = randint(30, 51)
     showstats(char)
#Define a function to run a small tournament between 4 randomly generated fighters
def tournament():
    a = fighter("", "", 1, 1, 1, 1, 1, 1, 1)
    randherostats(a)
    b = fighter("", "", 1, 1, 1, 1, 1, 1, 1)
    randherostats(b)
    c = fighter("", "", 1, 1, 1, 1, 1, 1, 1)
    randherostats(c)
    d = fighter("", "", 1, 1, 1, 1, 1, 1, 1)
    randherostats(d)
    
    ahp = a.hp
    bhp = b.hp
    chp = c.hp
    dhp = d.hp
    end = False
    
    print(" ")
    
    print("The first fight is between %s and %s" %(a.name, b.name))
    checkadv(a, b)
    
    print(" ")
    
    while end == False:
        fight(a, b)
        if checkend(a, b) == True:
            break
        print(" ")
        fight(b, a)
        if checkend(b, a) == True:
            break
        if input("Continue Combat? ") == "no":
            print("a fighter has withdrawn")
            break
    
    
    print(" ")
    print(" ")
    
    end = False
    print("The second fight is between %s and %s" %(c.name, d.name))
    checkadv(c, d)
    
    print(" ")
    
    while end == False:
        fight(c, d)
        if checkend(c, d) == True:
            break
        print(" ")
        fight(d, c)
        if checkend(c, d) == True:
            break
        if input("Continue Combat? ") == "no":
            print("a fighter has withdrawn")
            break
    
    print(" ")

    print(" ")
    
    if a.hp > 0 and b.hp <= 0: 
        e = a
        e.hp = ahp
    if b.hp > 0 and a.hp <= 0:
        e = b
        e.hp = bhp
    if c.hp > 0 and d.hp <= 0:
        f = c
        f.hp = chp
    if d.hp > 0 and c.hp <= 0:
        f = d
        f.hp = dhp
    if a.hp <= 0 and b.hp <= 0 and f.hp > 0:
        print("%s has no opponent to fight, they win by default" %(f.name))
    if c.hp <= 0 and d.hp <= 0 and e.hp > 0:
        print("%s has no opponent to fight, they win by default" %(e.name))
    if a.hp <= 0 and b.hp <= 0 and c.hp <= 0 and d.hp:
        print("All fighters have fallen")
    if e.hp > 0 and f.hp > 0:
        print("The final round is between %s and %s" %(e.name, f.name))
        showstats(e)
        showstats(f)
        checkadv(e, f)
        print(" ")
        end = False
        while end == False:
            fight(e, f)
            if checkend(e, f) == True:
                break
            print(" ")
            fight(f, e)
            if checkend(e, f) == True:
                break
            if input("Continue Combat? ") == "no":
                print("a fighter has withdrawn")
                break
    
#Define a function to check which fighter has an advantage and calculate damage
def checkadv(a, b):
    if a.wt == "Magic":
        a.dmg = a.atk - b.res
    else:
        a.dmg = a.atk - b.dfn
    
    if b.wt == "Magic":
        b.dmg = b.atk - a.res
    else:
        b.dmg = b.atk - a.dfn
     
    if a.dmg <= 0:
        a.dmg = 1
    if b.dmg <= 0:
        b.dmg = 1
    
    if a.adv == True:
        a.skl -= 1
        a.adv = False
    if b.adv == True:
        b.atk -= 1
        b.adv = False
      
    if a.wt == "Sword" and b.wt == "Axe":
        a.dmg += 3
        a.skl += 1
        a.adv = True
        print("%s has weapon advantage" %(a.name))
    if a.wt == "Axe" and b.wt == "Lance":
        a.dmg += 3
        a.skl += 1
        a.adv = True
        print("%s has weapon advantage" %(a.name))
    if a.wt == "Lance" and b.wt == "Sword":
        a.dmg += 3 
        a.skl += 1
        a.adv = True
        print("%s has weapon advantage" %(a.name))
    if b.wt == "Sword" and a.wt == "Axe":
        b.dmg += 3
        b.skl += 1
        b.adv = True
        print("%s has weapon advantage" %(b.name))
    if b.wt == "Axe" and a.wt == "Lance":
        b.dmg += 3
        b.skl += 1
        b.adv = True
        print("%s has weapon advantage" %(b.name))
    if b.wt == "Lance" and a.wt == "Sword":
        b.dmg += 3
        b.skl += 1
        b.adv = True
        print("%s has weapon advantage" %(b.name))

tournament()
        