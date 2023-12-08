import numpy as np
import random

class NumPyCreator:
    def from_list(self, lst, dtype=None):
        return np.array(list(lst), dtype)
    def from_tuple(self, tpl, dtype=None):
        return np.array(tpl, dtype)
    def from_iterable(self, itr, dtype=None):
        return np.array(itr, dtype)
    def from_shape(shape, value=0, dtype=None):
        return np.array([[value for i in range(shape[0])] for j in range(shape[1])], dtype)
    def random(self, shape):
        return np.array([[random.random() for i in range(shape[0])] for j in range(shape[1])])
    def identity(self, n):
        return np.array([[1 if i == j else 0 for i in range(n)] for j in range(n)])

if __name__ == "__main__":
    npc = NumPyCreator()
    u = npc.identity((15))
    v=npc.from_shape((2,3))
    w=npc.random((5,5))
    print(np.array2string((w), separator=", "))