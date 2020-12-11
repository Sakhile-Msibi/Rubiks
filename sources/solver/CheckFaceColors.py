import sys

from sources.solver.Rubik import Rubik

class CheckFaceColors:

    def two(self, cube, colorOne, colorTwo):
        if (cube.upper[0][1] == colorOne and cube.back[0][1] == colorTwo):
            return ([['upper', colorOne, 0, 1],['back', colorTwo, 0, 1]])
        elif (cube.upper[0][1] == colorTwo and cube.back[0][1] == colorOne):
            return ([['upper', colorTwo, 0, 1],['back', colorOne, 0, 1]])

        elif (cube.upper[1][2] == colorOne and cube.right[0][1] == colorTwo):
            return ([['upper', colorOne, 1, 2],['right', colorTwo, 0, 1]])
        elif (cube.upper[1][2] == colorTwo and cube.right[0][1] == colorOne):
            return ([['upper', colorTwo, 1, 2],['right', colorOne, 0, 1]])

        elif (cube.upper[2][1] == colorOne and cube.front[0][1] == colorTwo):
            return ([['upper', colorOne, 2, 1],['front', colorTwo, 0, 1]])
        elif (cube.upper[2][1] == colorTwo and cube.front[0][1] == colorOne):
            return ([['upper', colorTwo, 2, 1],['front', colorOne, 0, 1]])

        elif (cube.upper[1][0] == colorOne and cube.left[0][1] == colorTwo):
            return ([['upper', colorOne, 1, 0],['left', colorTwo, 0, 1]])
        elif (cube.upper[1][0] == colorTwo and cube.left[0][1] == colorOne):
            return ([['upper', colorTwo, 1, 0],['left', colorOne, 0, 1]])

        elif (cube.left[1][2] == colorOne and cube.front[1][0] == colorTwo):
            return ([['left', colorOne, 1, 2],['front', colorTwo, 1, 0]])
        elif (cube.left[1][2] == colorTwo and cube.front[1][0] == colorOne):
            return ([['left', colorTwo, 1, 2],['front', colorOne, 1, 0]])

        elif (cube.left[1][0] == colorOne and cube.back[1][2] == colorTwo):
            return ([['left', colorOne, 1, 0],['back', colorTwo, 1, 2]])
        elif (cube.left[1][0] == colorTwo and cube.back[1][2] == colorOne):
            return ([['left', colorTwo, 1, 0],['back', colorOne, 1, 2]])

        elif (cube.front[1][2] == colorOne and cube.right[1][0] == colorTwo):
            return ([['front', colorOne, 1, 2],['right', colorTwo, 1, 0]])
        elif (cube.front[1][2] == colorTwo and cube.right[1][0] == colorOne):
            return ([['front', colorTwo, 1, 2],['right', colorOne, 1, 0]])

        elif (cube.right[1][2] == colorOne and cube.back[1][0] == colorTwo):
            return ([['right', colorOne, 1, 2],['back', colorTwo, 1, 0]])
        elif (cube.right[1][2] == colorTwo and cube.back[1][0] == colorOne):
            return ([['right', colorTwo, 1, 2],['back', colorOne, 1, 0]])

        elif (cube.down[0][1] == colorOne and cube.front[2][1] == colorTwo):
            return ([['down', colorOne, 0, 1],['front', colorTwo, 2, 1]])
        elif (cube.down[0][1] == colorTwo and cube.front[2][1] == colorOne):
            return ([['down', colorTwo, 0, 1],['front', colorOne, 2, 1]])

        elif (cube.down[1][2] == colorOne and cube.right[2][1] == colorTwo):
           return ([['down', colorOne, 1, 2],['right', colorTwo, 2, 1]])
        elif (cube.down[1][2] == colorTwo and cube.right[2][1] == colorOne):
            return ([['down', colorTwo, 1, 2],['right', colorOne, 2, 1]])

        elif (cube.down[2][1] == colorOne and cube.back[2][1] == colorTwo):
            return ([['down', colorOne, 2, 1],['back', colorTwo, 2, 1]])
        elif (cube.down[2][1] == colorTwo and cube.back[2][1] == colorOne):
            return ([['down', colorTwo, 2, 1],['back', colorOne, 2, 1]])

        elif (cube.down[1][0] == colorOne and cube.left[2][1] == colorTwo):
            return ([['down', colorOne, 1, 0],['left', colorTwo, 2, 1]])
        elif (cube.down[1][0] == colorTwo and cube.left[2][1] == colorOne):
            return ([['down', colorTwo, 1, 0],['left', colorOne, 2, 1]])
        return (False)

    def three(self, cube, colorOne, colorTwo, colorThree):
        if (cube.upper[0][0] == colorOne and cube.left[0][0] == colorTwo and cube.back[0][2] == colorThree):
            return (['upper', colorOne, 0, 0],['left', colorTwo, 0, 0], ['back', colorThree, 0, 2])
        elif (cube.upper[0][0] == colorOne and cube.left[0][0] == colorThree and cube.back[0][2] == colorTwo):
            return (['upper', colorOne, 0, 0],['left', colorThree, 0, 0], ['back', colorTwo, 0, 2])
        elif (cube.upper[0][0] == colorTwo and cube.left[0][0] == colorThree and cube.back[0][2] == colorOne):
            return (['upper', colorTwo, 0, 0],['left', colorThree, 0, 0], ['back', colorOne, 0, 2])
        elif (cube.upper[0][0] == colorTwo and cube.left[0][0] == colorOne and cube.back[0][2] == colorThree):
            return (['upper', colorTwo, 0, 0],['left', colorOne, 0, 0], ['back', colorThree, 0, 2])
        elif (cube.upper[0][0] == colorThree and cube.left[0][0] == colorOne and cube.back[0][2] == colorTwo):
            return (['upper', colorThree, 0, 0],['left', colorOne, 0, 0], ['back', colorTwo, 0, 2])
        elif (cube.upper[0][0] == colorThree and cube.left[0][0] == colorTwo and cube.back[0][2] == colorOne):
            return (['upper', colorThree, 0, 0],['left', colorTwo, 0, 0], ['back', colorOne, 0, 2])

        elif (cube.upper[0][2] == colorOne and cube.right[0][2] == colorTwo and cube.back[0][0] == colorThree):
            return (['upper', colorOne, 0, 2],['right', colorTwo, 0, 2], ['back', colorThree, 0, 0])
        elif (cube.upper[0][2] == colorOne and cube.right[0][2] == colorThree and cube.back[0][0] == colorTwo):
            return (['upper', colorOne, 0, 2],['right', colorThree, 0, 2], ['back', colorTwo, 0, 0])
        elif (cube.upper[0][2] == colorTwo and cube.right[0][2] == colorThree and cube.back[0][0] == colorOne):
            return (['upper', colorTwo, 0, 2],['right', colorThree, 0, 2], ['back', colorOne, 0, 0])
        elif (cube.upper[0][2] == colorTwo and cube.right[0][2] == colorOne and cube.back[0][0] == colorThree):
            return (['upper', colorTwo, 0, 2],['right', colorOne, 0, 2], ['back', colorThree, 0, 0])
        elif (cube.upper[0][2] == colorThree and cube.right[0][2] == colorOne and cube.back[0][0] == colorTwo):
            return (['upper', colorThree, 0, 2],['right', colorOne, 0, 2], ['back', colorTwo, 0, 0])
        elif (cube.upper[0][2] == colorThree and cube.right[0][2] == colorTwo and cube.back[0][0] == colorOne):
            return (['upper', colorThree, 0, 2],['right', colorTwo, 0, 2], ['back', colorOne, 0, 0])

        elif (cube.upper[2][2] == colorOne and cube.right[0][0] == colorTwo and cube.front[0][2] == colorThree):
            return (['upper', colorOne, 2, 2],['right', colorTwo, 0, 0], ['front', colorThree, 0, 2])
        elif (cube.upper[2][2] == colorOne and cube.right[0][0] == colorThree and cube.front[0][2] == colorTwo):
            return (['upper', colorOne, 2, 2],['right', colorThree, 0, 0], ['front', colorTwo, 0, 2])
        elif (cube.upper[2][2] == colorTwo and cube.right[0][0] == colorThree and cube.front[0][2] == colorOne):
            return (['upper', colorTwo, 2, 2],['right', colorThree, 0, 0], ['front', colorOne, 0, 2])
        elif (cube.upper[2][2] == colorTwo and cube.right[0][0] == colorOne and cube.front[0][2] == colorThree):
            return (['upper', colorTwo, 2, 2],['right', colorOne, 0, 0], ['front', colorThree, 0, 2])
        elif (cube.upper[2][2] == colorThree and cube.right[0][0] == colorOne and cube.front[0][2] == colorTwo):
            return (['upper', colorThree, 2, 2],['right', colorOne, 0, 0], ['front', colorTwo, 0, 2])
        elif (cube.upper[2][2] == colorThree and cube.right[0][0] == colorTwo and cube.front[0][2] == colorOne):
            return (['upper', colorThree, 2, 2],['right', colorTwo, 0, 0], ['front', colorOne, 0, 2])

        elif (cube.upper[2][0] == colorOne and cube.left[0][2] == colorTwo and cube.front[0][0] == colorThree):
            return (['upper', colorOne, 2, 0],['left', colorTwo, 0, 2], ['front', colorThree, 0, 0])
        elif (cube.upper[2][0] == colorOne and cube.left[0][2] == colorThree and cube.front[0][0] == colorTwo):
            return (['upper', colorOne, 2, 0],['left', colorThree, 0, 2], ['front', colorTwo, 0, 0])
        elif (cube.upper[2][0] == colorTwo and cube.left[0][2] == colorThree and cube.front[0][0] == colorOne):
            return (['upper', colorTwo, 2, 0],['left', colorThree, 0, 2], ['front', colorOne, 0, 0])
        elif (cube.upper[2][0] == colorTwo and cube.left[0][2] == colorOne and cube.front[0][0] == colorThree):
            return (['upper', colorTwo, 2, 0],['left', colorOne, 0, 2], ['front', colorThree, 0, 0])
        elif (cube.upper[2][0] == colorThree and cube.left[0][2] == colorOne and cube.front[0][0] == colorTwo):
            return (['upper', colorThree, 2, 0],['left', colorOne, 0, 2], ['front', colorTwo, 0, 0])
        elif (cube.upper[2][0] == colorThree and cube.left[0][2] == colorTwo and cube.front[0][0] == colorOne):
            return (['upper', colorThree, 2, 0],['left', colorTwo, 0, 2], ['front', colorOne, 0, 0])

        elif (cube.down[0][0] == colorOne and cube.left[2][2] == colorTwo and cube.front[2][0] == colorThree):
            return (['down', colorOne, 0, 0],['left', colorTwo, 2, 2], ['front', colorThree, 2, 0])
        elif (cube.down[0][0] == colorOne and cube.left[2][2] == colorThree and cube.front[2][0] == colorTwo):
            return (['down', colorOne, 0, 0],['left', colorThree, 2, 2], ['front', colorTwo, 2, 0])
        elif (cube.down[0][0] == colorTwo and cube.left[2][2] == colorThree and cube.front[2][0] == colorOne):
            return (['down', colorTwo, 0, 0],['left', colorThree, 2, 2], ['front', colorOne, 2, 0])
        elif (cube.down[0][0] == colorTwo and cube.left[2][2] == colorOne and cube.front[2][0] == colorThree):
            return (['down', colorTwo, 0, 0],['left', colorOne, 2, 2], ['front', colorThree, 2, 0])
        elif (cube.down[0][0] == colorThree and cube.left[2][2] == colorOne and cube.front[2][0] == colorTwo):
            return (['down', colorThree, 0, 0],['left', colorOne, 2, 2], ['front', colorTwo, 2, 0])
        elif (cube.down[0][0] == colorThree and cube.left[2][2] == colorTwo and cube.front[2][0] == colorOne):
            return (['down', colorThree, 0, 0],['left', colorTwo, 2, 2], ['front', colorOne, 2, 0])

        elif (cube.down[0][2] == colorOne and cube.right[2][0] == colorTwo and cube.front[2][2] == colorThree):
            return (['down', colorOne, 0, 2],['right', colorTwo, 2, 0], ['front', colorThree, 2, 2])
        elif (cube.down[0][2] == colorOne and cube.right[2][0] == colorThree and cube.front[2][2] == colorTwo):
            return (['down', colorOne, 0, 2],['right', colorThree, 2, 0], ['front', colorTwo, 2, 2])
        elif (cube.down[0][2] == colorTwo and cube.right[2][0] == colorThree and cube.front[2][2] == colorOne):
            return (['down', colorTwo, 0, 2],['right', colorThree, 2, 0], ['front', colorOne, 2, 2])
        elif (cube.down[0][2] == colorTwo and cube.right[2][0] == colorOne and cube.front[2][2] == colorThree):
            return (['down', colorTwo, 0, 2],['right', colorOne, 2, 0], ['front', colorThree, 2, 2])
        elif (cube.down[0][2] == colorThree and cube.right[2][0] == colorOne and cube.front[2][2] == colorTwo):
            return (['down', colorThree, 0, 2],['right', colorOne, 2, 0], ['front', colorTwo, 2, 2])
        elif (cube.down[0][2] == colorThree and cube.right[2][0] == colorTwo and cube.front[2][2] == colorOne):
            return (['down', colorThree, 0, 2],['right', colorTwo, 2, 0], ['front', colorOne, 2, 2])

        elif (cube.down[2][2] == colorOne and cube.right[2][2] == colorTwo and cube.back[2][0] == colorThree):
            return (['down', colorOne, 2, 2],['right', colorTwo, 2, 2], ['back', colorThree, 2, 0])
        elif (cube.down[2][2] == colorOne and cube.right[2][2] == colorThree and cube.back[2][0] == colorTwo):
            return (['down', colorOne, 2, 2],['right', colorThree, 2, 2], ['back', colorTwo, 2, 0])
        elif (cube.down[2][2] == colorTwo and cube.right[2][2] == colorThree and cube.back[2][0] == colorOne):
            return (['down', colorTwo, 2, 2],['right', colorThree, 2, 2], ['back', colorOne, 2, 0])
        elif (cube.down[2][2] == colorTwo and cube.right[2][2] == colorOne and cube.back[2][0] == colorThree):
            return (['down', colorTwo, 2, 2],['right', colorOne, 2, 2], ['back', colorThree, 2, 0])
        elif (cube.down[2][2] == colorThree and cube.right[2][2] == colorOne and cube.back[2][0] == colorTwo):
            return (['down', colorThree, 2, 2],['right', colorOne, 2, 2], ['back', colorTwo, 2, 0])
        elif (cube.down[2][2] == colorThree and cube.right[2][2] == colorTwo and cube.back[2][0] == colorOne):
            return (['down', colorThree, 2, 2],['right', colorTwo, 2, 2], ['back', colorOne, 2, 0])

        elif (cube.down[2][0] == colorOne and cube.left[2][0] == colorTwo and cube.back[2][2] == colorThree):
            return (['down', colorOne, 2, 2],['left', colorTwo, 2, 0], ['back', colorThree, 2, 2])
        elif (cube.down[2][0] == colorOne and cube.left[2][0] == colorThree and cube.back[2][2] == colorTwo):
            return (['down', colorOne, 2, 2],['left', colorThree, 2, 0], ['back', colorTwo, 2, 2])
        elif (cube.down[2][0] == colorTwo and cube.left[2][0] == colorThree and cube.back[2][2] == colorOne):
            return (['down', colorTwo, 2, 2],['left', colorThree, 2, 0], ['back', colorOne, 2, 2])
        elif (cube.down[2][0] == colorTwo and cube.left[2][0] == colorOne and cube.back[2][2] == colorThree):
            return (['down', colorTwo, 2, 2],['left', colorOne, 2, 0], ['back', colorThree, 2, 2])
        elif (cube.down[2][0] == colorThree and cube.left[2][0] == colorOne and cube.back[2][2] == colorTwo):
            return (['down', colorThree, 2, 2],['left', colorOne, 2, 0], ['back', colorTwo, 2, 2])
        elif (cube.down[2][0] == colorThree and cube.left[2][0] == colorTwo and cube.back[2][2] == colorOne):
            return (['down', colorThree, 2, 2],['left', colorTwo, 2, 0], ['back', colorOne, 2, 2])
        return (False)