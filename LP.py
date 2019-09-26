import numpy as np


class LpStruct:

    # 目标函数
    # 目标函数最大值还是最小值（1，max）（0，min）
    ObjectSign = 0
    # 目标函数系数
    Objective = np.array([3, 1, -2])

    # 约束条件
    # 约束条件系数矩阵
    A = np.array([
        [2, -1, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [3, 0, 2, 0],
    ])

    # 约束条件的符号 (-1, <=) (1, >=) (0, =)
    Sign = np.array([-1, 0, 0, 0])
    # 约束条件的右端项
    B = np.array([-4, 6, 2, 10])
    # 变量
    Variable = np.array([1, -1, 0, 1])


def StandardLP(LpStruct):
    # 根据变量符号进行变量转化
    for i in range(0, len(LpStruct.Variable)):
        if LpStruct.Variable[i] < 0:
            LpStruct.A[:, i] = - LpStruct.A[:, i]
            LpStruct.Objective[i] = - LpStruct.Objective[i]
        elif LpStruct.Variable[i] == 0:
            LpStruct.A = np.insert(LpStruct.A, i+1, values=(-LpStruct.A[:, i]), axis=1)
            LpStruct.Objective = np.insert(LpStruct.Objective, i+1, values=(-LpStruct.Objective[i]))

    # 根据符号进行标准化转化
    for i in range(0, len(LpStruct.Sign)):
        V_N = np.zeros(len(LpStruct.Sign))
        if LpStruct.Sign[i] == -1:
            V_N[i] = 1
            LpStruct.A = np.c_[LpStruct.A, V_N]
        elif LpStruct.Sign[i] == -1:
            V_N[i] = -1
            LpStruct.A = np.c_[LpStruct.A, V_N]

    # 右端项转成非负
    for i in range(0, len(LpStruct.B)):
        if LpStruct.B[i] < 0:
            LpStruct.A[i] = - LpStruct.A[i]
            LpStruct.B[i] = - LpStruct.B[i]

    return LpStruct


x = LpStruct()
x = StandardLP(x)
print(x.Objective)
print(x.A[:])
print(x.B)

