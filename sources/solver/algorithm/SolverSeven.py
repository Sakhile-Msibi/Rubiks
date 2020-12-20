import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverSeven:

    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.currentCubePositionList = list()
        self.checkColor = CheckFaceColors()
        self.cornerThree = ["yellow", "blue", "red"]
        self.cornerFour = ["yellow", "red", "green"]
        self.cornerOne = ["yellow", "green", "orange"]
        self.cornerTwo = ["yellow", "blue", "orange"]
    
    def run(self, currentCube, solveMoveList):
        currentCube.cubeFaceHash()
        
        if (self.cubeOrigin.hash == currentCube.hash):
            return True
        self.moveSide(currentCube, solveMoveList, self.cornerOne)
        self.moveDown(currentCube, solveMoveList)	
        self.moveSide(currentCube, solveMoveList, self.cornerTwo)
        self.moveDown(currentCube, solveMoveList)
        self.moveSide(currentCube, solveMoveList, self.cornerThree)
        self.moveDown(currentCube, solveMoveList)
        self.moveSide(currentCube, solveMoveList, self.cornerFour)
        self.moveDown(currentCube, solveMoveList)
    
    def moveDown(self, currentCube, solveMoveList):
        currentCube.moveD ()
        solveMoveList.append("D")
    
    def moveSide(self, currentCube, solveMoveList, colorsList):
        mixNotation = MixNotation()
        
        while (self.finishedThreeColorPosition(currentCube, colorsList)) == False:
            mixNotation.mixMove(["L'", "U'", "L", "U"], currentCube)
            appendLists(solveMoveList, ["L'", "U'", "L", "U"])
    
    def finishedThreeColorPosition(self, currentCube, colorsList):
        listPos = self.checkColor.three(currentCube, colorsList[0], colorsList[1], colorsList[2])
        listPosOrigin = self.checkColor.three(self.cubeOrigin, colorsList[0], colorsList[1], colorsList[2])
        if (listPos[0][0] == "down" and listPos[0][1] == "yellow"):
            return True
        return False