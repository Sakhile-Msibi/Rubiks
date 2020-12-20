import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.checkPositionOfColor import checkPositionOfColor
from sources.solver.CheckFaceColors import CheckFaceColors

class SolverThree:
	
	def __init__(self, cubeOrigin):
		self.cubeOrigin = cubeOrigin
		self.currentCubePositionList = list()
		self.cubeOriginPositionList = list()
		self.checkColor = CheckFaceColors()
	
	def run(self, currentCube, solveMoveList):
		if ((self.finishedThreeColorPosition(currentCube, ["green", "orange"])) == False):
			self.moving(currentCube, solveMoveList, ["green", "orange"], "front")
		if ((self.finishedThreeColorPosition(currentCube, ["orange", "blue"])) == False):
			self.moving(currentCube, solveMoveList, ["orange", "blue"], "left")
		if ((self.finishedThreeColorPosition(currentCube, ["blue", "red"])) == False):
			self.moving(currentCube, solveMoveList, ["blue", "red"], "back")
		if ((self.finishedThreeColorPosition(currentCube, ["red", "green"])) == False):
			self.moving(currentCube, solveMoveList, ["red", "green"], "right")
	
	def finishedThreeColorPosition(self, currentCube, colorsList):
		return checkPositionOfColor(self.cubeOrigin, currentCube, colorsList[0], colorsList[1])

	def updatePositionList(self, cube, colorsList):
		return (self.checkColor.two(cube, colorsList[0], colorsList[1]))
	
	def moving(self, currentCube, solveMoveList, colorsList, face):
		self.cubeOriginPositionList = self.updatePositionList(self.cubeOrigin, colorsList)
		self.currentCubePositionList = self.updatePositionList(currentCube, colorsList)

		checkSideList = self.checkSide(currentCube, colorsList)
		
		if (checkSideList[0] == True):
			self.moveToTryPosition(currentCube, solveMoveList, colorsList)
		else:
			if (self.currentCubePositionList[0][0] != "down"):
				self.pushDown(currentCube, solveMoveList, colorsList)
				self.currentCubePositionList = self.updatePositionList(currentCube, colorsList)
			if (self.currentCubePositionList[0][0] != "down"):
				print("+++++++++++++++++++++++++++++++++++++++++++++++++")
				print("+++++                ERROR                  +++++")
				print("+++++++++++++++++++++++++++++++++++++++++++++++++")
				sys.exit(-1)
			self.currentCubePositionList = self.updatePositionList(currentCube, colorsList)
			if (self.currentCubePositionList[0][0] == "down"):
				self.moveToCenter(currentCube, solveMoveList, colorsList, face)
				self.currentCubePositionList = self.updatePositionList(currentCube, colorsList)
				self.moveToTryPosition(currentCube, solveMoveList, colorsList)
	
	def moveToCenter(self, currentCube, solveMoveList, colorsList, face):
		checkSideList = self.checkSide(currentCube, colorsList)
		while (checkSideList[0] == False):
			currentCube.moveD()
			solveMoveList.append("D")
			checkSideList = self.checkSide(currentCube, colorsList)

	def pushDown(self, currentCube, solveMoveList, colorsList):
		faceOne, faceTwo, colorOne, colorTwo = self.getSideParams(currentCube, colorsList)
		pattern = self.getPatternPushDown(faceOne, faceTwo)
		if (pattern == "rightPattern"):
			self.moveFormulaRight(currentCube, solveMoveList, faceOne)
		elif (pattern == "leftPattern"):
			self.moveFormulaLeft(currentCube, solveMoveList, faceOne)
	
	def getPatternPushDown(self, faceOne, faceTwo):
		if (faceOne == "left"):
			if (faceTwo == "front"):
				return ("rightPattern")
			elif (faceTwo == "back"):
				return ("leftPattern")
		elif (faceOne == "front" and faceTwo == "right"):
				return ("rightPattern")
		elif (faceOne == "right" and faceTwo == "back"):
			return ("rightPattern")

	def getSideParams(self, currentCube, colorsList):
		self.currentCubePositionList = self.updatePositionList(currentCube, colorsList)
		down = self.currentCubePositionList[0][0]
		colorDown = self.currentCubePositionList[0][1]
		colorFace = self.currentCubePositionList[1][1]
		face = self.currentCubePositionList[1][0]
		return down, face, colorDown, colorFace
	
	def checkSide(self, currentCube, colorsList):
		down, face, colorDown, colorFace = self.getSideParams(currentCube, colorsList)
		if (down != "down"):
			return [False, "null"]
		if (face == "front"):
			if (colorDown == "orange" and colorFace == "green"):
				return [True, "leftPattern"] 
			elif (colorDown == "red" and colorFace == "green"):
				return [True, "rightPattern"] 
		if (face == "back"):
			if (colorDown == "orange" and colorFace == "blue"):
				return [True, "leftPattern"] 
			elif (colorDown == "red" and colorFace == "blue"):
				return [True, "rightPattern"]
		if (face == "right"):
			if (colorDown == "blue" and colorFace == "red"):
				return [True, "rightPattern"]
			elif (colorDown == "green" and colorFace == "red"):
				return [True, "leftPattern"] 
		if (face == "left"):
			if (colorDown == "green" and colorFace == "orange"):
				return [True, "rightPattern"] 
			elif (colorDown == "blue" and colorFace == "orange"):
				return [True, "leftPattern"]
		return [False, "null"]
	
	def moveToTryPosition(self, currentCube, solveMoveList, colorsList):
		down, face, colorDown, colorFace = self.getSideParams(currentCube, colorsList)
		checkSideList = self.checkSide(currentCube, colorsList)
		if (checkSideList[1] == "rightPattern"):
			self.moveFormulaRight(currentCube, solveMoveList, face)
		elif (checkSideList[1] == "leftPattern"):
			self.moveFormulaLeft(currentCube, solveMoveList, face)

	def moveFormulaLeft(self, currentCube, solveMoveList, face):
		mixNotation = MixNotation()

		if (face == "front"):
			mixNotation.mixMove([ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ], currentCube)
			appendLists(solveMoveList, [ "D", "L", "D'", "L'", "D'", "F'", "D", "F" ])
		elif (face == "left"):
			mixNotation.mixMove([ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ], currentCube)
			appendLists(solveMoveList, [ "D", "B", "D'", "B'", "D'", "L'", "D", "L" ])
		elif (face == "back"):
			mixNotation.mixMove([ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ], currentCube)
			appendLists(solveMoveList, [ "D'", "L'", "D", "L", "D", "B", "D'", "B'" ])
		elif (face == "right"):
			mixNotation.mixMove([ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ], currentCube)
			appendLists(solveMoveList, [ "D", "F", "D'", "F'", "D'", "R'", "D", "R" ])
	
	def moveFormulaRight(self, currentCube, solveMoveList, face):
		mixNotation = MixNotation()
        
		if (face == "front"):
			mixNotation.mixMove([ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ], currentCube)
			appendLists(solveMoveList, [ "D'", "R'", "D", "R", "D", "F", "D'", "F'" ])
		elif (face == "left"):
			mixNotation.mixMove([ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ], currentCube)
			appendLists(solveMoveList, [ "D'", "F'", "D", "F", "D", "L", "D'", "L'" ])
		elif (face == "right"):
			mixNotation.mixMove([ "D'", "B'", "D", "B", "D", "R", "D'", "R'"], currentCube)
			appendLists(solveMoveList, [ "D'", "B'", "D", "B", "D", "R", "D'", "R'"])
		elif (face == "back"):
			mixNotation.mixMove([ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ], currentCube)
			appendLists(solveMoveList, [ "D", "R", "D'", "R'", "D'", "B'", "D", "B" ])