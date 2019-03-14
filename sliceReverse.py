array = []
n = int(0)
d = int(0)

def slicereverse(array, i1, i2):
    array2 = array[i1 : i2]
    while (n + d) < len(array2):
        a = array2[n]
        b = array2[n - d]
        array2[n] = b
        array2[n - d] = a
        n += 1
        d += 1