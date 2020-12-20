import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverOne:

    def __init__(self, cubeOrigin):
        self.cubeOrigin = cubeOrigin
        self.currentCubePositionList = list()
        self.cubeOriginPositionList = list()
        self.checkColor = CheckFaceColors()

    def run(self, currentCube, solveMoveList):
        if ((self.finishedTwoColorPosition(currentCube, "white", "green")) == False):
            self.edgeMoveTwoColor(currentCube, solveMoveList, "white", "green", "front")
        if ((self.finishedTwoColorPosition(currentCube, "white", "blue")) == False):
            self.edgeMoveTwoColor(currentCube, solveMoveList, "white", "blue", "back")
        if ((self.finishedTwoColorPosition(currentCube, "white", "red")) == False):
            self.edgeMoveTwoColor(currentCube, solveMoveList,  "white", "red", "right")
        if ((self.finishedTwoColorPosition(currentCube, "white", "orange")) == False):
            self.edgeMoveTwoColor(currentCube, solveMoveList, "white", "orange", "left")
    
    def finishedTwoColorPosition(self, currentCube, colorOne, colorTwo):
        return checkPositionOfColor(self.cubeOrigin, currentCube, colorOne, colorTwo)
    
    def edgeMoveTwoColor(self, currentCube, solveMoveList, colorOne, colorTwo, face):
        self.currentCubePositionList = self.checkColor.two(currentCube, colorOne, colorTwo)
        self.cubeOriginPositionList = self.checkColor.two(self.cubeOrigin, colorOne, colorTwo)
        
        if (face != self.currentCubePositionList[0][0] and face != self.currentCubePositionList[1][0]):
            self.moveDownTwoColor(currentCube, solveMoveList, colorOne, colorTwo, face)
        
        if (face == self.currentCubePositionList[0][0] or face == self.currentCubePositionList[1][0]):
            self.moveCenter(currentCube, solveMoveList, face, colorOne, colorTwo)
            if (self.currentCubePositionList[0][1] != self.cubeOriginPositionList[0][1]):
                self.changeSide(currentCube, solveMoveList, face)
    
    def moveCenter(self, currentCube, solveMoveList, face, colorOne, colorTwo):
        while (self.currentCubePositionList[1][2] != self.cubeOriginPositionList[1][2]):
            if (face == "front"):
                currentCube.moveBackF()
                solveMoveList.append("F'")
            if (face == "right"):
                currentCube.moveBackR()
                solveMoveList.append("R'")
            if (face == "left"):
                currentCube.moveBackL()
                solveMoveList.append("L'")
            if (face == "back"):
                currentCube.moveBackB()
                solveMoveList.append("B'")
            self.currentCubePositionList = self.checkColor.two(currentCube, colorOne, colorTwo)
    
    def updateFaceColor(self, currentCube, colorOne, colorTwo):
        self.currentCubePositionList = self.checkColor.two(currentCube, colorOne, colorTwo)
        return self.currentCubePositionList[0][0], self.currentCubePositionList[1][0]
    
    def moveDownTwoColor(self, currentCube, solveMoveList, colorOne, colorTwo, face):
        faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
        
        def moveDownCenter(currentCube, solveMoveList, colorOne, colorTwo, face):
            faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
            while (1):
                if (faceOne == face or faceTwo == face):
                    break
                currentCube.moveD()
                solveMoveList.append("D")
                faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
                
        def optimizationStep(count, solveMoveList, move):
            if (count == 3):
                count = 1
                solveMoveList.append(move + "'")
                return count, 1
            else:
                x = 0
                while (x != count):
                    x += 1
                    solveMoveList.append(move)
            return count, 0
        
        count = 0
        if (faceOne == "front" or faceTwo == "front"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                currentCube.moveF()
                faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
            count, flag = optimizationStep(count, solveMoveList, "F")
            moveDownCenter(currentCube, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    currentCube.moveBackF()
                    solveMoveList.append("F'")
                else:
                    currentCube.moveF()
                    solveMoveList.append("F")
        elif (faceOne == "left" or faceTwo == "left"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                currentCube.moveL()
                faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "L")
            moveDownCenter(currentCube, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    currentCube.moveBackL()
                    solveMoveList.append("L'")
                else:
                    currentCube.moveL()
                    solveMoveList.append("L")
        
        elif (faceOne == "right" or faceTwo == "right"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                currentCube.moveR()
                faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "R")
            moveDownCenter(currentCube, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    currentCube.moveBackR()
                    solveMoveList.append("R'")
                else:
                    currentCube.moveR()
                    solveMoveList.append("R")
        
        elif (faceOne == "back" or faceTwo == "back"):
            while (1):
                if (faceOne == "down" or faceTwo == "down"):
                    break
                count += 1
                currentCube.moveB()
                faceOne,faceTwo = self.updateFaceColor(currentCube, colorOne, colorTwo)
            count,flag = optimizationStep(count, solveMoveList, "B")
            moveDownCenter(currentCube, solveMoveList, colorOne, colorTwo, face)
            while (count != 0):
                count -= 1
                if (flag == 0):
                    currentCube.moveBackB()
                    solveMoveList.append("B'")
                else:
                    currentCube.moveB()
                    solveMoveList.append("B")
    
    @staticmethod
    def changeSide(currentCube, solveMoveList, face):
        mixNotation = MixNotation()
        
        if (face == "front"):
            mixNotation.mixMove(["F", "U'", "R", "U"], currentCube)
            appendLists(solveMoveList, ["F", "U'", "R", "U"])
        elif (face == "right"):
            mixNotation.mixMove(["R", "U'", "B", "U"], currentCube)
            appendLists(solveMoveList, ["R", "U'", "B", "U"])
        elif (face == "left"):
            mixNotation.mixMove(["L", "U'", "F", "U"], currentCube)
            appendLists(solveMoveList, ["L", "U'", "F", "U"])
        elif (face == "back"):
            mixNotation.mixMove(["B", "U'", "L", "U"], currentCube)
            appendLists(solveMoveList, ["B", "U'", "L", "U"])