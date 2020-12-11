import sys

def moveOptimization(solution):
    length = len(solution)
    i = 0
    newList = []

    while (i < length):
        counter = 0
        if (i + 2 < length):
            if (solution[i] == solution[i + 1] and solution[i + 1] == solution[i + 2]):
                if solution[i] == "F":
                    newList.append("F'")
                elif solution[i] == "F'":
                    newList.append("F")
                elif solution[i] == "R":
                    newList.append("R'")
                elif solution[i] == "R'":
                    newList.append("R")
                elif solution[i] == "U":
                    newList.append("U'")
                elif solution[i] == "U'":
                    newList.append("U")
                elif solution[i] == "B":
                    newList.append("B'")
                elif solution[i] == "B'":
                    newList.append("B")
                elif solution[i] == "L":
                    newList.append("L'")
                elif solution[i] == "L'":
                    newList.append("L")
                elif solution[i] == "D":
                    newList.append("D'")
                elif solution[i] == "D'":
                    newList.append("D")
                counter = 1
                i += 2
            elif (solution[i] == solution[i + 1]):
                if solution[i] == "F" or solution[i] == "F'":
                    newList.append("F2")
                elif solution[i] == "R" or solution[i] == "R'":
                    newList.append("R2")
                elif solution[i] == "U" or solution[i] == "U'":
                    newList.append("U2")
                elif solution[i] == "B" or solution[i] == "B'":
                    newList.append("B2")
                elif solution[i] == "L" or solution[i] == "L'":
                    newList.append("L2")
                elif solution[i] == "D" or solution[i] == "D'":
                    newList.append("D2")
                counter = 1
                i += 1
        if (counter == 0):
            newList.append(solution[i])
        i += 1
    return (newList)