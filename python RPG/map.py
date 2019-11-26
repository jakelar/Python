import random
def maps():
  
  n = 18
  rand = random.randint(0,100)
  map = [[0] * n for i in range(n)]
  bossCount =0
  shopCount =0
  for i in range(n):
      for j in range(n):
        rand = random.randint(0,100)  
        if rand <=20:
          map[i][j] = 'M'
        if (rand >20 and rand <=75):
          map[i][j] = 'P'
        if rand >75 and rand <=78:
          map[i][j]= 'C'
        if rand >78 and rand <80:
          map[i][j]= 'T'
        if rand >=80 and rand<=95:
          if shopCount<=10 :
            map[i][j]='S'
            shopCount +=1
          else:
            map[i][j]='P'
        if rand >95:
          if bossCount <=3:
            map[i][j]='B'
          else:
            map[i][j]='M'
  ranXKey= random.randint(0,17)
  ranYKey=random.randint(0,17)
  ranXDoor=random.randint(0,17)
  ranYDoor=random.randint(0,17)
  map[ranXKey][ranYKey]='K'
  map[ranXDoor][ranYDoor]='D'


      
  map[9][3]='P'        
  return map
  