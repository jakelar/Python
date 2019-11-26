import hero


class create():
    def created(self):
        raced = False
        classed = False
        raceList = ["human", "elf", "orc"]
        classList = ["ranger", "warrior", "wizard"]
#finds out hero name
        heroName = input("What is your name? ").lower().strip()

#Finds out hero Race
        while not raced:
            print(*raceList, sep=", ")
            race = input("What is your race? ").lower().strip()
            if race in raceList:
                raced = True
                break
#finds out hero class
        while not classed:
            print(*classList, sep=", ")
            heroClass = input("What is your class? ").lower().strip()
            if heroClass in classList:
                classed = True
                break
#creates the object based on class
        if heroClass == "warrior":
            char = hero.Warrior(heroName, race, heroClass)
        elif heroClass == "wizard":
            char = hero.Wizard(heroName, race, heroClass)
        elif heroClass == "ranger":
            char = hero.Ranger(heroName, race, heroClass)
        if race == "orc":
          hero.orc(char)
        if race == "elf":
          hero.elf(char)
        return char
