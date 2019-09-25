import numpy as np


class LpStruct:
    Objective = np.array([1, 3, 1, -2])

    A = np.array([
        [2, -1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [3, 0, 2, 0],
    ])
    Sign = np.array([0, 0, 0, 0])
    B = np.array([4, 6, 2, 10])

    Variable = np.array([1, -1, 0, 1])


def StandardLP(LpStruct):
    # 根据变量符号进行变量转化
    for i in range(0, len(LpStruct.Variable)):
        if LpStruct.Variable[i] < 0:
            LpStruct.A[:, i] = - LpStruct.A[:, i]
        elif LpStruct.Variable[i] == 0:
            LpStruct.A = np.insert(LpStruct.A, i+1, values=(-LpStruct.A[:, i]), axis=1)
    return LpStruct


x = LpStruct()
x = StandardLP(x)
print(x.A[:])
