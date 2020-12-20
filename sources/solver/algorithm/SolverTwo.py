import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverTwo:

    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.currentCubePositionList = list()
        self.cubeOriginPositionList = list()
        self.checkColor = CheckFaceColors()

    def run(self, currentCube, solveMoveList):
        if ((self.finishedThreeColorPosition(currentCube, "white", "green", "red")) == False):
            self.moving(currentCube, solveMoveList, "white", "green", "red", "front")
        if ((self.finishedThreeColorPosition(currentCube, "white", "red", "blue")) == False):
            self.moving(currentCube, solveMoveList, "white", "red", "blue", "right")
        if ((self.finishedThreeColorPosition(currentCube, "white", "blue", "orange")) == False):
            self.moving(currentCube, solveMoveList, "white", "blue", "orange", "back")
        if ((self.finishedThreeColorPosition(currentCube, "white", "orange", "green")) == False):
            self.moving(currentCube, solveMoveList, "white", "orange", "green", "left")
    
    def finishedThreeColorPosition(self, currentCube, colorOne, colorTwo, colorThree):
        return checkPositionOfColor(self.cubeOrigin, currentCube, colorOne, colorTwo, colorThree)
    
    def updatePositionList(self, cube, colorOne, colorTwo, colorThree):
        return (self.checkColor.three(cube, colorOne, colorTwo, colorThree))

    def moving(self, currentCube, solveMoveList, colorOne, colorTwo, colorThree, face):
        self.cubeOriginPositionList = self.updatePositionList(self.cubeOrigin, colorOne, colorTwo, colorThree)
        self.currentCubePositionList = self.updatePositionList(currentCube, colorOne, colorTwo, colorThree)
        
        if (self.checkSide(currentCube, face)) == False:
            if (self.currentCubePositionList[0][0] == "upper"):
                self.moveEdgeDown(currentCube, solveMoveList, colorOne, colorTwo, colorThree)
            if 	(self.currentCubePositionList[0][0] == "down"):
                self.moveEdgeDownToTryPosition(currentCube, solveMoveList, colorOne, colorTwo, colorThree, face)
        self.currentCubePositionList = self.updatePositionList(currentCube, colorOne, colorTwo, colorThree)
        if (self.checkSide(currentCube, face)) == True:
            self.moveSide(currentCube, solveMoveList, colorOne, colorTwo, colorThree, face)
    
    def moveEdgeDown(self, currentCube, solveMoveList, colorOne, colorTwo, colorThree):
        self.currentCubePositionList = self.updatePositionList(currentCube, colorOne, colorTwo, colorThree)
        mixNotation = MixNotation()
        if (self.currentCubePositionList[1][0] == "right" and self.currentCubePositionList[2][0] == "front"):
            mixNotation.mixMove(["F", "D'", "F'"], currentCube)
            appendLists(solveMoveList, ["F", "D'", "F'"])
        elif (self.currentCubePositionList[1][0] == "left" and self.currentCubePositionList[2][0] == "front"):
            mixNotation.mixMove(["F'", "D", "F"], currentCube)
            appendLists(solveMoveList, ["F'", "D", "F"])
        elif (self.currentCubePositionList[1][0] == "right" and self.currentCubePositionList[2][0] == "back"):
            mixNotation.mixMove(["B'", "D", "B"], currentCube)
            appendLists(solveMoveList, ["B'", "D", "B"])
        elif (self.currentCubePositionList[1][0] == "left" and self.currentCubePositionList[2][0] == "back"):
            mixNotation.mixMove(["B", "D'", "B'"], currentCube)
            appendLists(solveMoveList, ["B", "D'", "B'"])
        self.currentCubePositionList = self.updatePositionList(currentCube, colorOne, colorTwo, colorThree)
    
    def moveEdgeDownToTryPosition(self, currentCube, solveMoveList, colorOne, colorTwo, colorThree, face):
        while (self.checkSide(currentCube, face)) == False:
            currentCube.moveD()
            solveMoveList.append("D")
            self.currentCubePositionList = self.updatePositionList(currentCube, colorOne, colorTwo, colorThree)
    
    def checkSide(self, currentCube, face):
        if (face == "front"):
            return (self.checkDoubleSide(face, "right"))
        elif (face == "right"):
            return (self.checkDoubleSide(face, "back"))
        elif (face == "back"):
            return (self.checkDoubleSide(face, "left"))
        elif (face == "left"):
            return (self.checkDoubleSide(face, "front"))
        return False
    
    def checkDoubleSide(self, face, subFace):
        count = 0
        i = 0
        while (i < len(self.currentCubePositionList)):
            if (((self.currentCubePositionList[i][0]) == face) or ((self.currentCubePositionList[i][0]) == subFace)):
                count += 1
            i += 1
        return (count == 2)
    
    def moveSide(self, currentCube, solveMoveList, colorOne, colorTwo, colorThree, face):
        mixNotation = MixNotation()
        while ((self.finishedThreeColorPosition(currentCube, colorOne, colorTwo, colorThree)) == False):
            if (face == "front"):
                mixNotation.mixMove(["R'", "D'", "R", "D"], currentCube)
                appendLists(solveMoveList, ["R'", "D'", "R", "D"])
            elif (face == "right"):
                mixNotation.mixMove(["B'", "D'", "B", "D"], currentCube)
                appendLists(solveMoveList, ["B'", "D'", "B", "D"])
            elif (face == "back"):
                mixNotation.mixMove(["L'", "D'", "L", "D"], currentCube)
                appendLists(solveMoveList, ["L'", "D'", "L", "D"])
            elif (face == "left"):
                mixNotation.mixMove(["F'", "D'", "F", "D"], currentCube)
                appendLists(solveMoveList, ["F'", "D'", "F", "D"])