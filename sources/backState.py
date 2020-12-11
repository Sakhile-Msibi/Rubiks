import sys

def backState(cubeFace, color):
    if cubeFace[0][1] == color and cubeFace[1][1] == color and cubeFace[1][2] == color and cubeFace[1][0] == color and cubeFace[2][1] == color:
        return (4, 0)
    elif cubeFace[1][0] == color and cubeFace[1][1] == color and cubeFace[1][2] == color:
        return (3, 0)
    elif cubeFace[0][1] == color and cubeFace[1][1] == color and cubeFace[2][1] == color:
        return (3, 1)
    elif cubeFace[2][1] == color and cubeFace[1][1] == color and cubeFace[1][2] == color:
        return (2, 0)
    elif cubeFace[1][0] == color and cubeFace[1][1] == color and cubeFace[2][1] == color:
        return (2, 1)
    elif cubeFace[0][1] == color and cubeFace[1][1] == color and cubeFace[1][0] == color:
        return (2, 2)
    elif cubeFace[0][1] == color and cubeFace[1][1] == color and cubeFace[1][2] == color:
        return (2, 3)
    elif cubeFace[1][1] == color:
        return (1, 0)
    return False, False