import random 
import numpy as np

class AdventureGame():
    
    def __init__(self):
        self.treasures = []
        self.monsters = []
        self.swords = []
        self.potions = []
        self.venoms = []
        self.locations = []
        self.visited = []
        self.map = []
        self.score = 0
        self.swordCount = 0
        self.potionCount = 0
        self.text = ""
        self.quit = False
        self.skip = False
        pass

    def mapGenerator(self):
        randomList = random.sample(range(42), 19)
        c = 0
        for i in randomList:
            if c == 0:
                start = (i//7, i%7)
                self.visited += [start]
                c+=1
            elif 0 < c <= 5:
                treasureLocation = (i//7, i%7)
                self.treasures += [treasureLocation]
                self.locations += [treasureLocation]
                c+=1
            elif 5 < c <= 10:
                monsterLocation = (i//7, i%7)
                self.monsters += [monsterLocation]
                self.locations += [monsterLocation]
                c+=1
            elif 10 < c <= 12:
                swordLocation = (i//7, i%7)
                self.swords += [swordLocation]
                self.locations += [swordLocation]
                c+=1
            elif 12 < c <= 15:
                potionLocation = (i//7, i%7)
                self.potions += [potionLocation]
                self.locations += [potionLocation]
                c+=1
            elif 15 < c <= 18:
                venomLocation = (i//7, i%7)
                self.venoms += [venomLocation]
                self.locations += [venomLocation]
                c+=1
        mapList = []
        for j in range(6):
            mapList.append([""] * 7)
        mapList[start[0]][start[1]] = "E"
        self.map = mapList

    def move(self, mv):
        move = mv.upper()
        if move == "L":
            newLocation = (self.visited[-1][0], self.visited[-1][1]-1)
            if newLocation[1] < 0 or newLocation in self.visited:
                print("You cannot make this move.")
                self.skip = True
            else: 
                self.map[self.visited[-1][0]][self.visited[-1][1]] = ""
                self.visited += [newLocation]
                self.map[newLocation[0]][newLocation[1]] = "E"
        elif move == "U":
            newLocation = (self.visited[-1][0]-1, self.visited[-1][1])
            if newLocation[0] < 0 or newLocation in self.visited:
                print("You cannot make this move.")
                self.skip = True
            else:
                self.map[self.visited[-1][0]][self.visited[-1][1]] = ""
                self.visited += [newLocation]
                self.map[newLocation[0]][newLocation[1]] = "E"         
        elif move == "R":
            newLocation = (self.visited[-1][0], self.visited[-1][1]+1)
            if newLocation[0] > 6 or newLocation in self.visited:
                print("You cannot make this move.")
                self.skip = True
            else:
                self.map[self.visited[-1][0]][self.visited[-1][1]] = ""
                self.visited += [newLocation]
                self.map[newLocation[0]][newLocation[1]] = "E"                
        elif move == "D":
            newLocation = (self.visited[-1][0]+1, self.visited[-1][1])
            if newLocation[0] > 5 or newLocation in self.visited:
                print("You cannot make this move.")
                self.skip = True
            else:
                self.map[self.visited[-1][0]][self.visited[-1][1]] = ""
                self.visited += [newLocation]
                self.map[newLocation[0]][newLocation[1]] = "E"

    def checkTreasures(self, location):
        if location in self.treasures:
            self.map[location[0]][location[1]] = "T"
            print("+TREASURE")
            self.score+=2

    def checkMonsters(self, location):
        if location in self.monsters:
            self.map[location[0]][location[1]] = "M"
            if self.swordCount == 0:
                self.quit = True
                self.text = """Oh no! MONSTER.
You die."""
            else:
                self.text = """Oh no! MONSTER.
SWORD is used."""
                self.swordCount-=1
                self.score+=1

    def checkSwords(self, location):
        if location in self.swords:
            self.map[location[0]][location[1]] = "S"
            self.text = "+SWORD"
            self.swordCount+=1
            self.score+=1

    def checkPotions(self, location):
        if location in self.potions:
            self.map[location[0]][location[1]] = "P"
            self.text = "+POTION"
            self.potionCount+=1
            self.score+=1

    def checkVenoms(self, location):
        if location in self.venoms:
            self.map[location[0]][location[1]] = "V"
            if self.potionCount == 0:
                self.quit = True
                self.text = """Oh no! VENOM.
You die."""
            else:
                self.text = """Oh no! VENOM.
POTION is used."""
                self.potionCount-=1
                self.score+=1

    def checkBlank(self, location):
        if location not in self.locations:
            self.text = ""
            self.score+=1

    def printMap(self):
        mapArray = np.array(self.map)
        print("\033[H\033[J", end="")
        print("--------------------------------")
        print("\n")
        print(mapArray)
        print("\n")
        print("--------------------------------")

    def stats(self):
        scoreList = [self.score]
        swordList = [self.swordCount]
        potionList = [self.potionCount]
        stats = "Score: {} Sword: {} Potion: {}".format(scoreList, swordList, potionList)
        return stats

    def runner(self):
        self.mapGenerator()
        while True:
            self.printMap()
            print(self.text)
            print(self.stats())
            if self.quit:
                break
            mv = input("Press L, U, R, D to move: ")
            self.move(mv)
            if not self.skip:
                location = self.visited[-1]
                self.checkTreasures(location)
                self.checkMonsters(location)
                self.checkSwords(location)
                self.checkPotions(location)
                self.checkVenoms(location)
                self.checkBlank(location)
                

AdventureGame().runner()

        


        
                

        
            

            

        








    



        
     


        
        
            
        
        

    

       
            
        
            
        




        



        

        

        
        
        

        

         
