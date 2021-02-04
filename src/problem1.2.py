import numpy as np

def only_odds(arr):
    '''
    Takes an array of integers and returns
    a numpy array containing only the odd elements

    Example:

        arr = np.array([0,1,2,3,4,5])
        only_odds(arr)

    Would return:

        np.array([1,3,5])
    '''
    # your code here!
    return arr[arr % 2 == 1]


if __name__ == '__main__':
    # Test your code here!
    arr = np.array([0,1,2,3,4,5])
    print(only_odds(arr))
