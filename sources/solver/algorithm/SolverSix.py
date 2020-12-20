import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverSix:

    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.currentCubePositionList = list()
        self.checkColor = CheckFaceColors()

    def run(self, currentCube, solveMoveList):
        result = self.checkCorner(currentCube)
		
        if (result == 4):
            return True
        else:
            result = self.checkTryPosition(currentCube)
            if (result[0] == 4):
                return True
            else:
                if result[0] == 0:
                    self.moveToTryPosition(currentCube, solveMoveList, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
                result = self.checkTryPosition(currentCube)
                colorsList = result[1]
                patternList = self.getPattern(currentCube, colorsList)
                self.moveDownFace(currentCube, solveMoveList, patternList)
    
    def moveDownFace(self, currentCube, solveMoveList, patternList):
        face = patternList[1]
        
        if (face == "frontFace"):
            if (patternList[0] == "right"):
                self.moveToTryPosition(currentCube, solveMoveList, ["D", "L", "D'", "R'", "D", "L'", "D'", "R"])
            else:
                self.moveToTryPosition(currentCube, solveMoveList, ["D'", "R'", "D", "L", "D'", "R", "D", "L'"])
        elif (face == "backFace"):
            if (patternList[0] == "right"):
                self.moveToTryPosition(currentCube, solveMoveList, ["D", "R", "D'", "L'", "D", "R'", "D'", "L"])
            else:
                self.moveToTryPosition(currentCube, solveMoveList, ["D'", "L'", "D", "R", "D'", "L", "D", "R'"])
        elif (face == "rightFace"):
            if (patternList[0] == "right"):
                self.moveToTryPosition(currentCube, solveMoveList, ["D", "F", "D'", "B'", "D", "F'", "D'", "B"])
            else:
                self.moveToTryPosition(currentCube, solveMoveList, ["D'", "B'", "D", "F", "D'", "B", "D", "F'"])
        elif (face == "leftFace"):
            if (patternList[0] == "right"):
                self.moveToTryPosition(currentCube, solveMoveList, ["D", "B", "D'", "F'", "D", "B'", "D'", "F"])
            else:
                self.moveToTryPosition(currentCube, solveMoveList, ["D'", "F'", "D", "B", "D'", "F", "D", "B'"])
    
    def getPattern(self, currentCube, colorsList):
        patternList = list()
        
        if (["yellow", "green", "red"] == colorsList):
            patternList.append(self.getDirection(currentCube))
            if (patternList[0] == "left"):
                patternList.append("frontFace")
            else:
                patternList.append("rightFace")
        elif (["yellow", "blue", "orange"] == colorsList):
            patternList.append(self.getDirection(currentCube))
            if (patternList[0] == "left"):
                patternList.append("backFace")
            else:
                patternList.append("leftFace")
        elif (["yellow", "blue", "red"] == colorsList):
            patternList.append(self.getDirection(currentCube))
            if (patternList[0] == "left"):
                patternList.append("rightFace")
            else:
                patternList.append("backFace")
        elif (["yellow", "green", "orange"] == colorsList):
            patternList.append(self.getDirection(currentCube))
            if (patternList[0] == "left"):
                patternList.append("leftFace")
            else:
                patternList.append("frontFace")
        return patternList
    
    def getDirection(self, currentCube):
        currentCube.moveD()
        res = self.checkTryPosition(currentCube)
        direction = "left"
        
        if (res[0] == 0):
            direction = "right"
            currentCube.moveBackD()
        return (direction)
    
    def checkCorner(self, currentCube):
        count = 0
        
        if ((self.finishedThreeColorPosition(currentCube, ["yellow", "green", "red"])) == True):
            count += 1
        if ((self.finishedThreeColorPosition(currentCube, ["yellow", "blue", "orange"])) == True):
            count += 1
        if ((self.finishedThreeColorPosition(currentCube, ["yellow", "red", "blue"])) == True):
            count += 1
        if ((self.finishedThreeColorPosition(currentCube, ["yellow", "orange", "green"])) == True):
            count += 1
        return (count)
    
    def updatePositionList(self, cube, colors):
        return (self.checkColor.three(cube, colors[0], colors[1], colors[2]))
    
    def checkTryPosition(self, currentCube):
        count = 0
        correctCorner = list()
        self.currentCubePositionList = self.updatePositionList(currentCube, ["yellow", "green", "red"])
        
        if (self.checkSide(currentCube, "front")) == True:
            count += 1
            correctCorner = ["yellow", "green", "red"]
        self.currentCubePositionList = self.updatePositionList(currentCube, ["yellow", "blue", "red"])
        if (self.checkSide(currentCube, "right")) == True:
            count += 1
            correctCorner = ["yellow", "blue", "red"]
        self.currentCubePositionList = self.updatePositionList(currentCube, ["yellow", "blue", "orange"])
        if (self.checkSide(currentCube, "back")) == True: 
            count += 1
            correctCorner = ["yellow", "blue", "orange"]
        self.currentCubePositionList = self.updatePositionList(currentCube, ["yellow", "green", "orange"])
        if (self.checkSide(currentCube, "left")) == True:
            count += 1
            correctCorner = ["yellow", "green", "orange"]
        return (count, correctCorner)
    
    def finishedThreeColorPosition(self, currentCube, colorsList):
        return checkPositionOfColor(self.cubeOrigin, currentCube, colorsList[0], colorsList[1], colorsList[2])
    
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
    
    def moveToTryPosition(self, currentCube, solveMoveList, listMix):
        mixNotation = MixNotation()
        mixNotation.mixMove(listMix, currentCube)
        appendLists(solveMoveList, listMix)