class Vector:
    def __init__(self, lst):
        if isinstance(lst, list):
            if len(lst) == 1:
                self.values = [[]]
                for i in lst[0]:
                    pass
                    try:
                        self.values[0].append(float(i))
                    except ValueError:
                        raise ValueError("Vector constructor takes a list of floats")
                self.size = len(lst[0])
                self.shape = (1, self.size)
            else:
                self.values = []
                for i in lst:
                    try:
                        self.values.append([float(i[0])])
                    except ValueError:
                        raise ValueError("Vector constructor takes a list of floats")
                self.size = len(lst)
                self.shape = (self.size, 1)
        elif isinstance(lst, int):
            self.values = []
            i = 0
            while i < lst:
                self.values.append([float(i)])
                i += 1
            self.size = lst
            self.shape = (self.size, 1)
        elif isinstance(lst, tuple) and len (lst) == 2:
            try:
                float(lst[0])
                float(lst[1])
            except ValueError:
                raise ValueError("Vector constructor takes a range of floats")
            self.values = []
            if list(lst)[0] > list(lst)[-1]:
                raise ValueError("range must be increasing")
            i = lst[0]
            while i < lst[1]:
                self.values.append([float(i)])
                i += 1
            self.size = lst[1] - lst[0]
            self.shape = (self.size, 1)
        else:
            raise ValueError("Vector constructor takes a list, an int or a range")
    def dot(self, v2):
        if isinstance(v2, Vector):
            if self.shape != v2.shape:
                raise ValueError("to apply .dot method, both vectors must have the same shape")
            elif self.shape == (self.size, 1):
                ret = []
                i = 0
                while i < self.size:
                    ret.append([self.values[i][0] * v2.values[i][0]])
                    i += 1
                return Vector(ret)
            else:
                ret = [[]]
                i = 0
                while i < self.size:
                    ret[0].append(self.values[0][i] * v2.values[0][i])
                    i += 1
                return Vector(ret)
        else:
            raise ValueError(".dot method takes a Vector")
    def T(self):
        if self.shape == (1, self.size):
            ret = []
            for i in self.values[0]:
                ret.append([i])
            return Vector(ret)
        else:
            ret = [[]]
            for i in self.values:
                ret[0].append(i[0])
            return Vector(ret)
    def __str__(self):
        if self.shape == (1, self.size):
            return "Vector({})".format(self.values[0])
        else: 
            return "Vector({})".format(self.values)
    def __add__(self, v2):
        if isinstance(v2, Vector):
            if self.shape == v2.shape:
                if self.shape == (self.size, 1):
                    ret = []
                    i = 0
                    while i < self.size:
                        ret.append([self.values[i][0] + v2.values[i][0]])
                        i += 1
                    return Vector(ret)
                else:
                    ret = [[]]
                    i = 0
                    while i < self.size:
                        ret[0].append(self.values[0][i] + v2.values[0][i])
                        i += 1
                    return Vector(ret)
            else:
                raise ValueError("to add two vectors, they must have the same shape")
        else:
            raise ValueError("Addition is only defined between two vectors")
    def __radd__(self, v2):
        return self.__add__(v2)
    def __sub__(self, v2):
        if isinstance(v2, Vector):
            if self.shape == v2.shape:
                if self.shape == (self.size, 1):
                    ret = []
                    i = 0
                    while i < self.size:
                        ret.append([self.values[i][0] - v2.values[i][0]])
                        i += 1
                    return Vector(ret)
                else:
                    ret = [[]]
                    i = 0
                    while i < self.size:
                        ret[0].append(self.values[0][i] - v2.values[0][i])
                        i += 1
                    return Vector(ret)
            else:
                raise ValueError("to substract two vectors, they must have the same shape")
        else:
            raise ValueError("Substraction is only defined between two vectors")
    def __rsub__(self, v2):
        return self.__sub__(v2)
    def __truediv__(self, num):
        if isinstance(num, float) or isinstance(num, int):
            if num != 0:
                if self.shape == (self.size, 1):
                    ret = []
                    i = 0
                    while i < self.size:
                        ret.append([self.values[i][0] / num])
                        i += 1
                    return Vector(ret)
                else:
                    ret = [[]]
                    i = 0
                    while i < self.size:
                        ret[0].append(self.values[0][i] / num)
                        i += 1
                    return Vector(ret)
            else:
                raise ValueError("Division by zero")
        else:
            raise ValueError("Division is only defined between a vector and a number")
    def __rtruediv__(self, v2):
        return self.__truediv__(v2)
    