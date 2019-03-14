array = []
array2 = []
n = int(0)


def arrayshift(array, shift):
    while len(array2) < len(array):
        array2[n - shift] = array[n]
        n += 1