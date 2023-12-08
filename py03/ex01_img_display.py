from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
import time

class ImageProcessor:
    def __init__(self) -> None:
        pass
    def load(self, path):
        if path == None:
            return None
        if path[-4:] != ".png":
            return None
        return np.asarray(Image.open(path))
    def display(self, array):
        plt.imshow(array)
        plt.show()

#i = ImageProcessor()
#imgpl = i.load("./42AI.png")
#i.display(imgpl)