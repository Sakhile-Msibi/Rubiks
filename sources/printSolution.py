import sys

from sources.solver.Rubik import Rubik

def printSolution(cube, moveList, flag):
    for i, move in enumerate(moveList):
        if move == 'U':
            cube.moveU()
        elif move == 'D':
            cube.moveD()
        elif move == 'R':
            cube.moveR()
        elif move == 'L':
            cube.moveL()
        elif move == 'F':
            cube.moveF()
        elif move == 'B':
            cube.moveB()

        elif move == "U'":
            cube.moveBackU()
        elif move == "D'":
            cube.moveBackD()
        elif move == "R'":
            cube.moveBackR()
        elif move == "L'":
            cube.moveBackL()
        elif move == "F'":
            cube.moveBackF()
        elif move == "B'":
            cube.moveBackB()

        elif move == 'U2':
            cube.moveDoubleU()
        elif move == 'D2':
            cube.moveDoubleD()
        elif move == 'R2':
            cube.moveDoubleR()
        elif move == 'L2':
            cube.moveDoubleL()
        elif move == 'F2':
            cube.moveDoubleF()
        elif move == 'B2':
            cube.moveDoubleB()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("#", i, " ", move)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        if (flag == "-g"):
            cube.printRubik()
        else:
            cube.printRubikText()