#hero class 
class Hero:
  def __init__(self,name,race,heroClass):
    self.name = name 
    self.race = race
    self.heroClass = heroClass
    self.level = 1
    self.hp = 0
    self.atk = 0
    self.alive = True
    self.mana = 0 
    self.maxMana = 0
    self.xp = 0
    self.xpMax=25
    self.locationi=9
    self.locationj=3
    self.inventory = ["potion","potion"]
    self.gold = 100

#Hero state Class function
  def annClass(self):
    print("I am a " + self.heroClass)
#Hero state attack function
  def ataak(self):
    print("my attack is "+str(self.atk))
#Hero state Name function
  def announce(self):
    print("Hello i am "+ self.name)
# Warrior Child class extends the Hero class (Inheritance)
class Warrior (Hero):
  def __init__(self,name,race,heroClass):
    super().__init__(name,race,heroClass)
    self.maxHP = 100 
    self.hp = 100
    self.mana = 50
    self.maxMana =50
    self.atk = 15
    self.level = 1
    self.heroSkill ='strike'
    
   # if race =="orc":  
   #   self.atk +=4
   #   self.maxMana -= 20
   #   self.maxHP +=40

  #def orcLevel(hero):
   # hero.atk+=1
   # hero.mana -=5
   # hero.hp+=10 

  def levelUp(hero):
    hero.xpMax+=2*hero.xpMax
    hero.maxHP+=30
    print("Your HP increasted by 30 to "+str(hero.maxHP))
    hero.hp = hero.maxHP
    hero.atk+=3
    print("Your attack increasted by 3 to "+str(hero.atk))
    hero.level +=1  
    #if hero.race == "orc":
    #  hero.atk+=1
    #  hero.maxMana-=5
    #  hero.maxHP+=40

  def ataak(self):
    print("my axe is "+str(self.atk) + " POWER.")

  # Wizard Child class extends the Hero class (Inheritance)  
class Wizard (Hero):
  def __init__(self,name,race,heroClass):
    super().__init__(name,race,heroClass) 
    self.maxHP = 70
    self.hp = 70
    self.atk =25
    self.level = 1
    self.heroSkill ='FireBall'
    
    
  def levelUp(hero):
    hero.xpMax+=2*hero.xpMax
    hero.maxHP+=10
    print("Your HP increasted by 10 to "+str(hero.maxHP))
    hero.hp = hero.maxHP
    hero.atk+=7
    print("Your attack increasted by 7 to "+str(hero.atk))
    hero.level +=1  
  
  def ataak(self):
    print("my Fireball hits for "+str(self.atk))
# Ranger Child class extends the Hero class (Inheritance)
class Ranger (Hero):
  def __init__(self,name,race,heroClass):
    super().__init__(name,race,heroClass)
    self.maxHP = 90 

    self.hp = 90
    self.atk =18
    self.level = 1
    self.heroSkill ='flurry'
    

  def levelUp(hero):
    hero.xpMax+=2*hero.xpMax
    hero.maxHP+=15
    print("Your HP increasted by 15 to "+str(hero.maxHP))
    hero.hp = hero.maxHP
    hero.atk+=4
    print("Your attack increasted by 4 to "+str(hero.atk))
    hero.level +=1
    if hero.race=="elf":  
      elfLevel(hero)
    if hero.race == "orc":
      orcLevel(hero)
  
  
  def ataak(self):
    print("Pew pew pew for "+str(self.atk))

def orc(hero):
  hero.atk +=4
  hero.maxMana -= 20
  hero.maxHP +=40
def orcLevel(hero):
  hero.atk+=1
  hero.maxMana -=5
  hero.maxHP+=10

def elf(hero):
  hero.maxMana +=20
  hero.maxHP-=10
def elfLevel(hero):
  hero.maxMana +=5
  hero.maxHP-=5