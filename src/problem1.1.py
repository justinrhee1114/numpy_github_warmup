import numpy as np

def border_with_zeros(arr):
    '''
    Takes in a 2D numpy array and adds
    a border of zeros around the outer edge

    Example:

        arr = np.array([
            [1,1],
            [1,1]
        ])
        border_with_zeros(arr)

    Would return:

        np.array([
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ])
    '''
    # your code here!

    z = np.zeros(16)
    zr = z.reshape(4,4)
    print(zr)

    zr[1:3,1:3] = arr
    return zr

if __name__ == '__main__':
    # Test your code here!
    arr = np.array([
        [1,1],
        [1,1]
    ])
    print(border_with_zeros(arr))
