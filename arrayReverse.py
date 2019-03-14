array = []
n = int(0)
d = int(0)

def arrayReverse():
    while (n + d) < len(array):
        a = array[n]
        b = array[n - d]
        array[n] = b
        array[n - d] = a
        n += 1
        d += 1