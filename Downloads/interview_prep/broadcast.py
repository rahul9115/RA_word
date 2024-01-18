import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
print(sigmoid(np.array([[1,2,3],[1,2,3]])))
