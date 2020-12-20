import sys

from sources.solver.Rubik import Rubik
from sources.appendLists import appendLists
from sources.solver.mix.MixNotation import MixNotation
from sources.backState import backState

class SolverFour:
    
    def run(self, currentCube, solveMoveList):
        mixNotation = MixNotation()
        moveList = ["F", "L", "D", "L'", "D'", "F'"]
        one,two = backState(currentCube.down, "yellow")
		
        if (one == 4):
            return True
        if (one == 1):
            mixNotation.mixMove(moveList, currentCube)
            appendLists(solveMoveList, moveList)
        
        one,two = backState(currentCube.down, "yellow")
        if (one == 2 and two == 0):
            mixNotation.mixMove(moveList, currentCube)
            appendLists(solveMoveList, moveList)
        elif (one == 2 and two == 1):
            mixNotation.mixMove(["D'", "F", "L", "D", "L'", "D'", "F'"], currentCube)
            appendLists(solveMoveList, ["D'", "F", "L", "D", "L'", "D'", "F'"])
        elif (one == 2 and two == 2):
            mixNotation.mixMove(["D'", "D'", "F", "L", "D", "L'", "D'", "F'"], currentCube)
            appendLists(solveMoveList, ["D'", "D'", "F", "L", "D", "L'", "D'", "F'"])
        elif (one == 2 and two == 3):
            mixNotation.mixMove(["D", "F", "L", "D", "L'", "D'", "F'"], currentCube)
            appendLists(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
		
        one,two = backState(currentCube.down, "yellow")
        if (one == 3 and two == 0):
            mixNotation.mixMove(moveList, currentCube)
            appendLists(solveMoveList, moveList)
        elif (one == 3 and two == 1):
            mixNotation.mixMove(["D", "F", "L", "D", "L'", "D'", "F'"], currentCube)
            appendLists(solveMoveList, ["D", "F", "L", "D", "L'", "D'", "F'"])
        
        one,two = backState(currentCube.down, "yellow")
        if (one == 4):
            return True