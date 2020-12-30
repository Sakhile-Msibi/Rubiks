import sys
import random

from sources.solver.Rubik import Rubik
from sources.printErrorMsg import printErrorMsg

class MixNotation:

    def __init__(self):
        self.maxCount = 500
        self.availableCommands = ["F", "D", "B", "R", "L", "U", "F2", "D2", "B2", "R2", "L2", "U2", "F'", "B'", "R'", "L'", "U'", "D'"]
    
    def randomMoveGenerator(self, countMove):
        if (countMove > self.maxCount):
            printErrorMsg("The maximum number allowed is 500")
        listMove = list()
        size = len(self.availableCommands) - 1
        while countMove > 0:
            countMove -= 1
            n = random.randint(0, size)
            listMove.append(self.availableCommands[n])
        return listMove
    
    def mixMove(self, listMove, cube):
        for element in listMove:
            if (element == "F"):
                cube.moveF()
            elif (element == "B"):
                cube.moveB()
            elif (element == "R"):
                cube.moveR()
            elif (element == "L"):
                cube.moveL()
            elif (element == "U"):
                cube.moveU()
            elif (element == "D"):
                cube.moveD()
            elif (element == "F2"):
                cube.moveDoubleF()
            elif (element == "B2"):
                cube.moveDoubleB()
            elif (element == "R2"):
                cube.moveDoubleR()
            elif (element == "L2"):
                cube.moveDoubleL()
            elif (element == "U2"):
                cube.moveDoubleU()
            elif (element == "D2"):
                cube.moveDoubleD()
            elif (element == "F'"):
                cube.moveBackF()
            elif (element == "B'"):
                cube.moveBackB()
            elif (element == "R'"):
                cube.moveBackR()
            elif (element == "L'"):
                cube.moveBackL()
            elif (element == "U'"):
                cube.moveBackU()
            elif (element == "D'"):
                cube.moveBackD()
        return (cube)