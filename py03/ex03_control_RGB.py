from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
import time
from ex02_manipulate_array import ScrapBooker
from ex00_np_array_create import NumPyCreator

class ColorFilter:
    def invert(self, array):
        """
            Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        new_arr = array.copy()
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                for k in range(len(new_arr[i][j]) - 1):
                    new_arr[i][j][k] = 255 - array[i][j][k]
        return new_arr
    def to_blue(self, array):
        """
            Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = array.copy()
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                new_arr[i][j][2] = 255
        return new_arr

    def to_green(self, array):
        """
            Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = array.copy()
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                new_arr[i][j][1] = 255
        return new_arr
    
    def to_red(self, array):
        """
            Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = array.copy()
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                new_arr[i][j][0] = 255
        return new_arr

    def to_celluloid(self, array):
        """
            Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = array.copy()
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                if int(new_arr[i][j][0]) + int(new_arr[i][j][1]) + int(new_arr[i][j][2]) < 150:
                    new_arr[i][j][0] = new_arr[i][j][0] * 0.3
                    new_arr[i][j][1] = new_arr[i][j][1] * 0.3
                    new_arr[i][j][2] = new_arr[i][j][2] * 0.3
        return new_arr
    
    def to_grayscale(self, array, filter, **kwargs):
        """
            Applies a grayscale filter to the image received as a numpy array.
            For filter = ’mean’/’m’: performs the mean of RBG channels.
            For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = array.copy()
        if filter == 'm' or filter == 'mean':
            for i in range(len(new_arr)):
                for j in range(len(new_arr[i])):
                    new_arr[i][j][0] = int((int(new_arr[i][j][0]) + int(new_arr[i][j][1]) + int(new_arr[i][j][2])) / 3)
                    new_arr[i][j][1] = int((int(new_arr[i][j][0]) + int(new_arr[i][j][1]) + int(new_arr[i][j][2])) / 3)
                    new_arr[i][j][2] = int((int(new_arr[i][j][0]) + int(new_arr[i][j][1]) + int(new_arr[i][j][2])) / 3)
            return new_arr
        elif filter == 'weight' or filter == 'w':
            #if len(kwargs) == 3 and kwargs[0] + kwargs[1] + kwargs[2] == 1:
            if len(kwargs) == 1:
                for i in range(len(new_arr)):
                    for j in range(len(new_arr[i])):
                        new_arr[i][j][0] = int((int(new_arr[i][j][0] * kwargs['weights'][0]) + int(new_arr[i][j][1] * kwargs['weights'][1]) + int(new_arr[i][j][2] * kwargs['weights'][2])) / 3)
                        new_arr[i][j][1] = int((int(new_arr[i][j][0] * kwargs['weights'][0]) + int(new_arr[i][j][1] * kwargs['weights'][1]) + int(new_arr[i][j][2] * kwargs['weights'][2])) / 3)
                        new_arr[i][j][2] = int((int(new_arr[i][j][0] * kwargs['weights'][0]) + int(new_arr[i][j][1] * kwargs['weights'][1]) + int(new_arr[i][j][2] * kwargs['weights'][2])) / 3)
                return new_arr
        return None
    

if __name__ == "__main__":
    cf = ColorFilter()
    sb = ScrapBooker()
    npc = NumPyCreator()
    img = np.asarray(Image.open("./elon_musk.png"))
    #plt.imshow(cf.invert(img))
    #plt.imshow(cf.to_blue(img))
    #plt.imshow(cf.to_green(img))
    #plt.imshow(cf.to_red(img))
    #plt.imshow(cf.to_celluloid(img))
    plt.imshow(cf.to_grayscale(img, 'mean'))
    #plt.imshow(cf.to_grayscale(img, 'weight', weights = [0.33, 0.33, 0.34]))
    plt.show()