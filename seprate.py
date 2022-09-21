import pandas as pd
import numpy as np


def frequency(data):
    q = 3
    conv = []
    for i in range(len(data)):
        conv.append(pd.value_counts(pd.qcut(data[i], q)))
    return conv


def wide(data):
    q = 3
    conv = []
    for i in range(len(data)):
        conv.append(pd.value_counts(pd.cut(data[i], q)))
    return conv
