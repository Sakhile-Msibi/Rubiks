import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverFive:

    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.checkColor = CheckFaceColors()

    def run(self, currentCube, solveMoveList):
        result = self.moveDown(currentCube, solveMoveList)
        if (result == 4):
            return True
        elif (result == 2):
            self.moveFace(currentCube, solveMoveList)
    
    def moveDown(self, currentCube, solveMoveList):
        count = 0
        while (count < 2):
            if ((self.finishedTwoColorPosition(currentCube, ["yellow", "green"])) == True):
                count += 1
            if ((self.finishedTwoColorPosition(currentCube, ["yellow", "blue"])) == True):
                count += 1
            if ((self.finishedTwoColorPosition(currentCube, ["yellow", "red"])) == True):
                count += 1
            if ((self.finishedTwoColorPosition(currentCube, ["yellow", "orange"])) == True):
                count += 1
            if (count == 4):
                return 4
            if (count < 2):
                count = 0
                currentCube.moveD()
                solveMoveList.append("D")
        return 2
    
    def	finishedTwoColorPosition(self, currentCube, colorsList):
        return checkPositionOfColor(self.cubeOrigin, currentCube, colorsList[0], colorsList[1])
    
    def moveFace(self, currentCube, solveMoveList):
        result = 2
        if ((self.finishedTwoColorPosition(currentCube, ["yellow", "green"])) == True and (self.finishedTwoColorPosition(currentCube, ["yellow", "blue"])) == True):
                result = self.moveOppositeRibs(currentCube, solveMoveList, "right")
        if ((self.finishedTwoColorPosition(currentCube, ["yellow", "red"])) == True and (self.finishedTwoColorPosition(currentCube, ["yellow", "orange"])) == True):
                result = self.moveOppositeRibs(currentCube, solveMoveList, "front")
        if (result == 2):
            self.cornerChange(currentCube, solveMoveList, self.getIncorectCornern(currentCube))
    
    def moveOppositeRibs(self, currentCube, solveMoveList, face):
        mixNotation = MixNotation()
        
        if (face == "front"):
            mixNotation.mixMove(["L", "D", "L'", "D", "L", "D2", "L'"], currentCube)
            appendLists(solveMoveList, ["L", "D", "L'", "D", "L", "D2", "L'"])
        if (face == "right"):
            mixNotation.mixMove(["F", "D", "F'", "D", "F", "D2", "F'"], currentCube)
            appendLists(solveMoveList, ["F", "D", "F'", "D", "F", "D2", "F'"])
        return self.moveDown(currentCube, solveMoveList)
    
    def getIncorectCornern(self, currentCube):
        isFalseBlue = self.finishedTwoColorPosition(currentCube, ["yellow", "blue"])
        isFalseGreen = self.finishedTwoColorPosition(currentCube, ["yellow", "green"])
        isFalseRed = self.finishedTwoColorPosition(currentCube, ["yellow", "red"])
        isFalseOrange = self.finishedTwoColorPosition(currentCube, ["yellow", "orange"])
        
        if (isFalseBlue == True and isFalseOrange == True):
            return ("front")
        elif (isFalseGreen == True and isFalseOrange == True):
            return ("right")
        elif (isFalseGreen == True and isFalseRed == True):
            return ("back")
        elif (isFalseRed  == True and isFalseBlue == True):
            return ("left")
    
    def cornerChange(self, currentCube, solveMoveList, face):
        mixNotation = MixNotation()
        
        if (face == "front"):
            mixNotation.mixMove(["L", "D", "L'", "D", "L", "D2", "L'", "D"], currentCube)
            appendLists(solveMoveList, ["L", "D", "L'", "D", "L", "D2", "L'", "D"])
        elif (face == "back"):
            mixNotation.mixMove(["R", "D", "R'", "D", "R", "D2", "R'", "D"], currentCube)
            appendLists(solveMoveList, ["R", "D", "R'", "D", "R", "D2", "R'", "D"])
        elif (face == "right"):
            mixNotation.mixMove(["F", "D", "F'", "D", "F", "D2", "F'", "D"], currentCube)
            appendLists(solveMoveList, ["F", "D", "F'", "D", "F", "D2", "F'", "D"])
        elif (face == "left"):
            mixNotation.mixMove(["B", "D", "B'", "D", "B", "D2", "B'", "D"], currentCube)
            appendLists(solveMoveList, ["B", "D", "B'", "D", "B", "D2", "B'", "D"])