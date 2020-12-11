import sys

from sources.solver.Rubik import Rubik
from sources.solver.CheckFaceColors import CheckFaceColors

def checkPositionOfColor(cubeOrigin, currentCube, colorOne, colorTwo, colorThree="null"):
    checkColor = CheckFaceColors()
    
    if (colorThree == "null"):
        currentCubePositionList = checkColor.two(currentCube, colorOne, colorTwo)
        cubeOriginPositionList = checkColor.two(cubeOrigin, colorOne, colorTwo)
        i = 0
        while (i < len(cubeOriginPositionList)):
            if (cubeOriginPositionList[i] != currentCubePositionList[i]):
                return (False)
            i += 1
        return True
    else:
        currentCubePositionList = checkColor.three(currentCube, colorOne, colorTwo, colorThree)
        cubeOriginPositionList = checkColor.three(cubeOrigin, colorOne, colorTwo, colorThree)
        i = 0
        while (i < len(cubeOriginPositionList)):
            j = 0
            while (j < len(cubeOriginPositionList[0])):
                if (cubeOriginPositionList[i][j] != currentCubePositionList[i][j]):
                    return (False)
                j += 1
            i += 1
        return True