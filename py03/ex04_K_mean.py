import sys
import numpy as np
from getcsv import CsvReader
import random
from ex00_np_array_create import NumPyCreator as npc

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            None.
        Raises:
        -------
            This function should not raise any Exception.
        """
        self.centroids = random.sample(range(len(X) - 1), self.ncentroid)
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        #code
        groups = [[i, i, 0] for i in range(len(X) - 1)]
        
        #print(groups)
        for i in range(len(X) - 1):
            if i not in self.centroids:
                min_distance = -1
                c = 1
                for j in range(len(self.centroids)):
                    #print(X[self.centroids][j])
                    distance = np.sqrt((X[self.centroids[j]][1] - X[i][1])**2 + (X[self.centroids[j]][2] - X[i][2])**2 + (X[self.centroids[j]][3] - X[i][3])**2)
                    if min_distance == -1:
                        min_distance = distance
                        c = self.centroids[j]
                    elif distance < min_distance:
                        min_distance = distance
                        c = self.centroids[j]
                groups[i][1] = c
                #print("EEEEEEE",groups[i][1])
                groups[i][2] = min_distance
                #groups[c][2] += min_distance
            #print(groups[i])
        #print(self.centroids)
        return np.array(groups)



if len(sys.argv) == 3:
    try:
        kc = KmeansClustering(int(sys.argv[2]))
    except:
        print("Arguments 2 must be a positive integer")
        exit()
elif len(sys.argv) == 4:
    try:
        kc = KmeansClustering(int(sys.argv[2]), int(sys.argv[3]))
    except:
        print("Arguments 2 and 3 must be positive integers")
        exit()
elif len(sys.argv) == 2:
    kc = KmeansClustering()
else:
    print("To use this program:\n\t- python3 ex04.py 'data_set' [max_iter=20] [ncentroid=5]")
array = np.array(CsvReader(sys.argv[1], skip_top=1).getdata(), dtype=float)
if kc.ncentroid > 0 and kc.max_iter > 0 and kc.ncentroid < len(array):
    p = []
    sum_c = []
    #dif_c = npc.from_shape((kc.ncentroid, kc.max_iter), dtype=float)
    nb_c = npc.from_shape((kc.ncentroid, kc.max_iter), dtype=int)
    #sum_c = np.array([[(kc.centroids[i], 0) for i in range(kc.ncentroid)] for j in range(len(array))], dtype=float)
    for i in range(kc.max_iter):
        kc.fit(array)
        p.append(kc.predict(array))
        sum_c.append(kc.centroids)
    sum_c = np.array(sum_c)
    for i in range(len(p)):
        for j in range(len(array) - 1):
            for k in range(len(sum_c[i])):
                if sum_c[i][k] == p[i][j][1]:
                    #dif_c[i][k] += p[i][j][2]
                    nb_c[i][k] += 1
    if kc.ncentroid == 4:
        for iter in range(kc.max_iter):
            print("Iteration number", iter + 1, ":")
            type_c = npc.from_shape((kc.ncentroid, kc.max_iter), dtype=object)
            bone_d = 0
            tallest = 0
            slender = 0
            for i in range(1, 4):
                if array[sum_c[iter][i]][3] > array[sum_c[iter][i]][3]:
                    bone_d = i
            type_c[iter][bone_d] = "Asteroids’ Belt colonies."
            if bone_d == 0:
                tallest = 1
            for i in range(1, 4):
                if i != bone_d:
                    if array[sum_c[iter][i]][3] > array[sum_c[iter][i]][3]:
                        tallest = i
            type_c[iter][tallest] = "Mars Republic."
            if tallest == 1:
                slender = 2
            for i in range(1, 4):
                if i != bone_d and i != tallest:
                    if array[sum_c[iter][i]][3] > array[sum_c[iter][i]][3]:
                        slender = i
            type_c[iter][slender] = "The flying cities of Venus."
            for i in range(4):
                if i != bone_d and i != tallest and i != slender:
                    type_c[iter][i] = "United Nations of Earth."
            for i in range(kc.ncentroid):
                print("\tCentroid ", sum_c[iter][i], " : ",nb_c[iter][i], "associatedvalue\t\t---> from ", type_c[iter][i])
    else:
        for iter in range(kc.max_iter):
            print("Iteration number", iter + 1, ":")
            for i in range(kc.ncentroid):
                print("\tCentroid ", sum_c[iter][i], " : ",nb_c[iter][i], "associatedvalue")
else:
    print("Arguments 2 and 3 must be positive integers while argument 3 must be less than the number of data")
    exit()