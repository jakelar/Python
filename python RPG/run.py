import heroCreation
import monster
import random
import battle
import os
import map
import inventory
import LoadSave


def run(hero, maped):
    while hero.alive:
#display movement options
        movement = input(
            "------------------------------ \n          [North] \n      [West]    [East] \n          [South]\n [Map]  [Inventory] [Status]\n------------------------------ \n "
        ).lower().strip()
#hiden save option
        if movement == "save":
            saveFile = hero.name
            LoadSave.Save(saveFile, hero, maped)
#north movement
        if movement == 'north':
            if hero.locationi == 0:
                os.system('clear')
                print("You cannot go that way.")
            else:
                hero.locationi -= 1
                os.system('clear')
#south movement
        if movement == 'south':
            if hero.locationi == 17:
                os.system('clear')
                print("You cannot go that way.")
            else:
                hero.locationi += 1
                os.system('clear')
#west movement
        if movement == 'west':
            if hero.locationj == 0:
                os.system('clear')
                print("You cannot go that way.")
            else:
                hero.locationj -= 1
                os.system('clear')
#East Movement
        if movement == 'east':
            if hero.locationj == 17:
                os.system('clear')
                print("You cannot go that way.")
            else:
                hero.locationj += 1
                os.system('clear')
#Map option prints map to console
        if movement == 'map':
            os.system('clear')
            import numpy as np
            print(np.matrix(maped))
#Status displays current stats
        if movement == 'status':
            os.system('clear')
            print("Level: " + str(hero.level) + "\nXP: " + str(hero.xp) + "/" +
                  str(hero.xpMax) + "\nHP:" + str(hero.hp) + "/" +
                  str(hero.maxHP) + "\nATK:" + str(hero.atk))
#Brings up inventory
        if movement == 'inventory':
            inventory.prints(hero)
            item = input("use item or [cancel]\n")
            if item == "cancel":
                os.system('clear')
            else:
                inventory.use(hero, item)

#handler for different map tiles

#Boss Tile
        if maped[hero.locationi][hero.locationj] == 'B':
            ready = input(
                " you see a Boss monster in the distance\n are you ready to fight?"
            )
            if ready == 'yes':
                #boss battle
                print("boss battles not yet")
            if ready == 'no':
                print("He'll be waiting")
#Trap tile
        if maped[hero.locationi][hero.locationj] == 'T':
            hero.hp -= 15
            print("You fell into a trap and lost 15 Hit points.")
#Plains tile
        if maped[hero.locationi][hero.locationj] == "P":
            print("You are in a Field.")
            rand = random.randint(0, 100)
            if rand > 75:
                battle.battle(hero)
            if hero.hp <= 0:
                hero.alive = False
                print("you dead")
                break
#Chest Tile
        if maped[hero.locationi][hero.locationj] == 'C':
            print("you found 100 gold and a potion")
            hero.gold += 100
            inventory.add(hero, "potion")
            print("You are in a Field.")
            rand = random.randint(0, 100)
            if rand > 75:
                battle.battle(hero)
            maped[hero.locationi][hero.locationj] = 'P'
#Mountains tile
        if maped[hero.locationi][hero.locationj] == 'M':
            print("You are in the mountains.")
            rand = random.randint(0, 100)
            if rand > 75:
                battle.battle(hero)
#Shop Tile
        if maped[hero.locationi][hero.locationj] == 'S':
            print("You are at a shop")
            purchase = input(
                "do you want to buy a potion 100g or rest 50g\n [potion] [rest]"
            )
            if purchase == "potion":
                if hero.gold >= 100:
                    hero.gold -= 100
                    inventory.add(hero, "potion")
                else:
                    print("not enough gold peasant! Begone!")
                    rand = random.randint(0, 100)
                    if rand > 75:
                        battle.battle(hero)
            if purchase == "rest":
                hero.hp = hero.maxHP
#Key Tile
        if maped[hero.locationi][hero.locationj] == 'K':
            print("You found a magic Key")
            inventory.add(hero, "Magic Key")
            maped[hero.locationi][hero.locationj]='P'
#Door Tile
        if maped[hero.locationi][hero.locationj] == 'D':
            print("You Found a Magic Door")
            if "Magic Key" in hero.inventory:
                print("A WINNER IS YOU")
                break
            else:
                print("I need a Key.")
