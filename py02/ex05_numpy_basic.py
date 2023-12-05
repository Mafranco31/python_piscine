import numpy as np

class TyniStatistician:
    def mean(self, x):
        if x == None:
            return None
        ret = 0.0
        for i in x:
            ret += i
        return ret / len(x)

    def median(self, x):
        if x == None:
            return None
        sorted_x = sorted(x)
        if len(x) % 2 == 0:
            return (sorted_x[len(x) // 2] + sorted_x[(len(x) // 2) - 1]) / 2
        else:
            return sorted_x[len(x) // 2]


    def quartile(self, x):
        if x == None:
            return None
        if len(x) == 1:
            return [float(x[0]), float(x[0])]
        s = sorted(x)
        n = len(x) - 1
        q1_f = n / 4
        q1_i = int(q1_f)
        q1_diff = q1_f - q1_i
        q1 = s[q1_i] + (s[q1_i + 1] - s[q1_i]) * q1_diff
        print(n, q1_f, q1_i, q1_diff, q1)
        q3_f = n / 4 * 3
        q3_i = int(q3_f)
        q3_diff = q3_f - q3_i
        q3 = s[q3_i] + (s[q3_i + 1] - s[q3_i]) * q3_diff
        return [q1, q3]

    def var(self, x):
        if x == None:
            return None
        n = len(x)
        mean = self.mean(x)
        sum = 0
        for i in x:
            sum += pow(i - mean, 2)
        var = sum / n
        return var

            
    def std(self, x):
        if x == None:
            return None
        return pow(self.var(x), 0.5)

#tstat = TyniStatistician()
#x = [1, 42, 300, 10, 59]
#z = [1, 4, 100, 5, 49, 1000000, 13290801293409218, 1203984, 102935]
#y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#w = [1, 2, 3, 4, 5]
#print(tstat.var(w))
#print(np.var(w))
#print(tstat.std(w))
#print(np.std(w))