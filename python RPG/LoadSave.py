import hero
import json
##json map as second File

#load save information from File
def Load(fileName):
  try:
    with open(fileName, 'rt'):
      f = open(fileName, "rt")
      heroName = f.readline().strip().lower()
      race = f.readline().strip().lower()
      heroClass  = f.readline().strip().lower()
      level = f.readline().strip()
      if heroClass == "warrior":
        char = hero.Warrior(heroName,race,heroClass)
        print(level)
        for i in range(int(level)-1):
          char.levelUp()
        print(char.level)
        return char
      elif heroClass == "wizard":
        char = hero.Wizard(heroName,race,heroClass)
        for i in range(int(level)-1):
          char.levelUp()
        return char
      elif heroClass == "ranger":
        char = hero.Ranger(heroName,race,heroClass)
        for i in range(int(level)-1):
          char.levelUp()
        return char

  except FileNotFoundError:
    print("not found")# Keep preset values

#load Map File 
def mapLoad(fileName):
  mapFile=fileName+'map'
  try:
    with open(mapFile, 'r') as filehandle:
      basicList = json.load(filehandle)
      return basicList
  except FileNotFoundError:
    print("notfound")

#write hero and map information to file
def Save(fileName,hero,maped):
  try:
    with open(fileName, 'wt'):
      f = open(fileName, "w")
      f.write(hero.name + '\n' + hero.race + '\n' + hero.heroClass + '\n' + str(hero.level)+'\n')  
      mapFile= fileName+'map'
      d=open(mapFile,'wt') 
      json.dump(maped, d)

  except FileNotFoundError:
    print("not found")# Keep preset values

