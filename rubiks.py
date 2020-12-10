import sys

from sources.fileReader import fileReader
from sources.printErrorMsg import printErrorMsg
from sources.solver.mix.MixValidation import MixValidation
from sources.solver.mix.MixNotation import MixNotation
from sources.solver.Rubik import Rubik
from sources.solver.CheckFaceColors import CheckFaceColors
from sources.solver.algorithm.Algorithm import Algorithm
from sources.printSolution import printSolution
from sources.moveOptimization import moveOptimization

usage = "Usage: rubik.py String or [-i or -f or --help or -h][number or filename][-gt or wc]"

if (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++                                       +++++")
    print("+++++             Rubiks usage              +++++")
    print("+++++               OPTIONS                 +++++")
    print("+++++     Available moves [F B R L U D]     +++++")
    print("+++++     Move modificators ['] and [2]     +++++")
    print("+++++      Example: rubik.py F2 B' U2       +++++")
    print("+++++       -i is a random generator        +++++")
    print("+++++      -gt print a rubik solution       +++++")
    print("+++++      Example: rubik.py -i 10 -gt      +++++")
    print("+++++         -f read from a file           +++++")
    print("+++++   Example: rubik.py -f fileName -gt   +++++")
    print("+++++       -wc print a mix solution        +++++")
    print("+++++       Example: -f fileName -wc        +++++")
    print("+++++                                       +++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    sys.exit(-1)
if (len(sys.argv) != 4 and len(sys.argv) != 2):
    printErrorMsg(usage)
if (len(sys.argv) == 4 and ((sys.argv[1] != "-f" and sys.argv[1] != "-i") or (sys.argv[3] != "-gt" and sys.argv[3] != "-wc"))):
    printErrorMsg(usage)

if ((len(sys.argv) == 4) and sys.argv[1] == "-f"):
    bufferReader = fileReader(sys.argv[2])
    mixValidator = MixValidation(bufferReader)
    mixValidator.run()
elif (len(sys.argv) == 2):
    bufferReader = sys.argv[1]
    mixValidator = MixValidation(sys.argv[1])
    mixValidator.run()

mixNotation = MixNotation()
moveList = list()
if ((len(sys.argv) == 4) and sys.argv[1] == "-i"):
    try:
        number = int(sys.argv[2])
        if (number <= 0):
            sys.exit(-1)
        moveList = mixNotation.randomMoveGenerator(int(sys.argv[2]))
    except:
        printErrorMsg("Please enter a positive number")
else:
    moveList = bufferReader.split(" ")

cube = Rubik(3)
mixNotation.mixMove(moveList, cube)
cube.cubeFaceHash()
algorithm = Algorithm(cube)
cubeOrigin = Rubik(3)
if (len(sys.argv) == 4 and sys.argv[3] != "-wc"):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Mix notation list")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    for x in moveList:
        print(x, end=" ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    #print("")
    print("Mixed rubik")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    if (sys.argv[3] == "-g"):
        cube.printRubik()
    else:
        cube.printRubikText()
if (cubeOrigin.hash == cube.hash):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++      The rubik is already solved      +++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")
    sys.exit(-1)
solution = algorithm.run()
subSolution = moveOptimization(solution)
mixNotation.mixMove(moveList, cubeOrigin)
if (len(sys.argv) == 4 and sys.argv[3] != "-wc"):
    printSolution(cubeOrigin, subSolution, sys.argv[3])
else:
    i = 0
    for x in subSolution:
        if (i != 0 and i != len(subSolution)):
            print(end=" ")
        print(x, end="")
        i += 1
    print("")