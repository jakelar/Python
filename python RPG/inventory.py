import hero

def use(hero,item):
  if item in hero.inventory:
    
    if item =="potion":
      if hero.maxHP-hero.hp <= 50:
        hero.hp = hero.maxHP
      else:
        hero.hp += 50
      print("you recovered 50 HP")
    remove(hero,item)
  else:
    print ("item not in inventory")
  

def prints(hero):
  print(hero.inventory)

def add(hero,item):
  hero.inventory.append(item)

def remove(hero,item):
  hero.inventory.remove(item)
  

