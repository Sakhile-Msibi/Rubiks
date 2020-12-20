import sys

from sources.solver.algorithm.SolverOne import SolverOne
from sources.solver.algorithm.SolverTwo import SolverTwo
from sources.solver.algorithm.SolverThree import SolverThree
from sources.solver.algorithm.SolverFour import SolverFour
from sources.solver.algorithm.SolverFive import SolverFive
from sources.solver.algorithm.SolverSix import SolverSix
from sources.solver.algorithm.SolverSeven import SolverSeven
from sources.solver.Rubik import Rubik

class Algorithm:

    def __init__(self, cube):
        self.cube = cube
        self.solveMoveList = list()
    
    def run(self):
        cubeOrigin = Rubik(3)

        solverOne = SolverOne(cubeOrigin)
        solverTwo = SolverTwo(cubeOrigin)
        solverThree = SolverThree(cubeOrigin)
        solverFour = SolverFour()
        solverFive = SolverFive(cubeOrigin)
        solverSix = SolverSix(cubeOrigin)
        solverSeven = SolverSeven(cubeOrigin)

        solverOne.run(self.cube, self.solveMoveList)
        solverTwo.run(self.cube, self.solveMoveList)
        solverThree.run(self.cube, self.solveMoveList)
        solverFour.run(self.cube, self.solveMoveList)
        solverFive.run(self.cube, self.solveMoveList)
        solverSix.run(self.cube, self.solveMoveList)
        solverSeven.run(self.cube, self.solveMoveList)
        return (self.solveMoveList)