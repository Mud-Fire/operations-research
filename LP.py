import numpy as np

class LP:
    Objective = [1, 3, 1, -2]

    ConstraintA = [
        [2, -1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [3, 0, 2, 0],
    ]
    ConstraintSign = [0, 0, 0, 0]
    ConstraintB = [4, 6, 2, 10]

    Variable = [1, 1, 1, 1]


def StandardLP(LP):

    for i in range(0,len(LP.Variable)):
        if LP.Variable[i] < 0:
            break
    return LP


x = LP()
print(StandardLP(x))
