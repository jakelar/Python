import heroCreation
import monster
import random
import battle
import os
import run
import map
import LoadSave


def main():
  #determines if new or saved game and runs
  newSaved = input("New or Load? ").lower().strip()


  if newSaved == 'new':
      maped = map.maps()
      hero = heroCreation.create().created()
      run.run(hero,maped)

      
      
  elif newSaved == 'load':
      fileName = input("filename?")
      hero = LoadSave.Load(fileName)
      maped = LoadSave.mapLoad(fileName)
      run.run(hero,maped)
      


if __name__ == "__main__":
    main()
