import monster
import random
import LoadSave
import os
import inventory
def battle(hero):



  lvl = hero.level
  mob = monster.Monster(type, lvl)
  mob.appear()

  while mob.alive:
  #prints HP Bar
    hpbar="["
    n=int((hero.hp/hero.maxHP)*10)
    for i in range(1,10):
      if i<=n:
        hpbar+="||"
      else:
        hpbar+='  '
    hpbar+="]"
    #print Battle options
    action = input("------------------------------ \n"+hpbar+"\n     HP:"+str(hero.hp)+"/"+ str(hero.maxHP)+"\n    [Attack] [Inventory] \n    ["+hero.heroSkill+"] [Run] \n------------------------------ \n > ").lower().strip()
    #attack option
    if action == "attack":
        os.system('clear')
        modify = random.randint(hero.level - 2, hero.level + 7)
        damage = hero.atk + modify
        print("You hit monster for " + str(damage) +" Damage.")
        mob.hp -= damage
        #Check to see if monster is dead
        if mob.hp <= 0:
            mob.alive = False

            print("Final fantasy fanfare song")
            levelUp(hero,mob.xpValue)
            break
        #monster attack    
        if mob.alive:
          mobdify = random.randint(-10,10)
          mobattack = mob.atk+mobdify
          print("Monster hits you for " + str(mobattack) +" Damage.")
          hero.hp -= mobattack
          if hero.hp <= 0:
            hero.alive = False
            print("you dead")
            break
    #Run command handling        
    if action == "run":
      coward = random.randint(0,100)
      if coward >=50:
        print("you run like a coward and escape")
        mob.alive = False
      else:
        print("You couldnt get away, not only are you a coward but you are slow.")
        print("Monster hits you for " + str(mob.atk) +" Damage.")
        hero.hp -= mob.atk
        if hero.hp <= 0:
          hero.alive = False
          print("you dead")
          break
    #skill handler
    if action == hero.heroSkill:
      os.system('clear')
      if hero.hp>25:
        modify = random.randint(hero.level - 2, hero.level + 7)
        damage = hero.atk *2 + modify * 2
        hero.hp-= 25
        print("You use your "+ hero.heroSkill+" monster for " + str(damage) +" Damage. \n Costing you 25hp.")
        mob.hp -= damage
      #Check to see if monster is dead
        if mob.hp <= 0:
            mob.alive = False

            print("Final fantasy fanfare song")
            levelUp(hero,mob.xpValue)
            break
        #monster attack    
        if mob.alive and modify < hero.level+5:
          mobdify = random.randint(-10,10)
          mobattack = mob.atk+mobdify
          print("Monster hits you for " + str(mobattack) +" Damage.")
          hero.hp -= mobattack
          if hero.hp <= 0:
            hero.alive = False
            print("you dead")
            break
        if modify > hero.level+5:
          print("You crit the monster stunning him.")
      else:
        print("not enough HP to use this skill.")
    #inventory handler
    if action == "inventory":
      inventory.prints(hero)
      item= input("use item or [cancel]")  
      if item == "cancel":
        os.system('clear')
      else:
        inventory.use(hero,item)

#level up checker which determines if hero needs to increase in level by exp
def levelUp(hero,XP):
  hero.xp += XP
  print("you gained " + str(XP) + "xp." )
  if hero.xp >= hero.xpMax:
    print("you leveled up")
    hero.levelUp()