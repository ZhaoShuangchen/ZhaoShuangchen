import numpy as np
import pandas as pd
import sklearn.naive_bayes as bay
import seprate as s


def fun(y, dict):  # conv target name to number
    for i in range(len(y)):
        y[i] = dict[y[i]]
    return y


def refactor_file(method, x):
    fre = s.frequency(x)
    wide = s.wide(x)
    if method == 'wide':
        for i in range(len(x)):
            for j in range(len(x[0])):
                if wide[0].index[0].left < x[i][j] <= wide[0].index[0].right:
                    x[i][j] = 0
                elif wide[0].index[1].left < x[i][j] <= wide[0].index[1].right:
                    x[i][j] = 1
                else:
                    x[i][j] = 2
    elif method == 'frequency':
        for i in range(len(x)):
            for j in range(len(x[0])):
                if fre[0].index[0].left < x[i][j] <= fre[0].index[0].right:
                    x[i][j] = 0
                elif fre[0].index[1].left < x[i][j] <= fre[0].index[1].right:
                    x[i][j] = 1
                else:
                    x[i][j] = 2
    return x


def trans(data, target_loc, feature_num):
    if target_loc == 'right':
        x, y = np.split(ary=data, axis=1, indices_or_sections=[len(data.T)-1, ])
    elif target_loc == 'left':
        y, x = np.split(ary=data, axis=1, indices_or_sections=[1, ])
    x, y = x.values, y.values.flatten()
    x1 = []
    for i in range(len(x)):
        x1.append([])
        for j in range(feature_num):
            x1[i].append(j)
    for i in range(len(x)):
        for j in range(4):
            x1[i][j] = x[i][j]
    return x1, y


if __name__ == '__main__':
    # data = 读文件
    x, y = trans(data=data, target_loc='right', feature_num=4)
    dict = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    iris_y = fun(y, dict)
    print(y)
    separate_x = refactor_file(method='frequency', x=x)
