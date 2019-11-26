import random
class Monster():
 



  def __init__(self,type,lvl):
    modify = random.randint(lvl-2,lvl +5)
    self.type = type
    self.lvl=lvl+modify
    if self.lvl<1:
      self.lvl=1
    self.atk=20+modify*2 +(random.randint(-10,10))
    self.hp=15+ lvl * 20
    self.xpValue= self.atk
    self.alive = True

  def appear(self):
    print("a monster appears it is level "+ str(self.lvl))
 


    