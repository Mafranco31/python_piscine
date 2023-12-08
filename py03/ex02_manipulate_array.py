import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        '''
            Crops the image as a rectangle via dim arguments (being the new height
            and width of the image) from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return: 
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        '''
        return [[array[i + position[0]][j + position[1]] for j in range(dim[0])] for i in range(dim[1])]

    def thin(self, array, n, axis):
        '''
            Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        '''
        if n < 1 or axis not in [0, 1]:
            return None
        return np.delete(array, n, axis)
    
    def juxtapose(self, array, n, axis):
        '''
            Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        '''
        if n < 1 or axis not in [0, 1]:
            return None
        ret = array
        for _ in range(n - 1):
            ret = np.concatenate((ret, array), axis)
        return ret
        
    def mosaic(self, array, dim):
        '''
                Makes a grid with multiple copies of the array. The dim argument specifies
                the number of repetition along each dimensions.
            Args:
            -----
                array: numpy.ndarray.
                dim: tuple of 2 integers.
            Return:
            -------
                new_arr: mosaic numpy.ndarray.
                None (combinaison of parameters not compatible).
        '''
        return [[np.array(array) for j in range(dim[0])] for i in range(dim[1])]

if __name__ == "__main__":
    sb = ScrapBooker()
    arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    print(arr, end="\n\n")
    #print(sb.crop(arr, (5,5), (4, 4)))
    #print(sb.thin(arr, range(7), 1))
    arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(sb.juxtapose(arr2, 4, 0))
    arr3 = np.array([[1, 2, 3]])
    print(sb.mosaic(arr3, (3, 3)))