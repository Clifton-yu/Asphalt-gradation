import numpy as np


def entry2np(entry_vars):
    data = []
    for i in range(len(entry_vars)):
        row_data = [entry_vars[i][j].get() for j in range(len(entry_vars[0]))]
        data.append(row_data)
    return np.array(data)
