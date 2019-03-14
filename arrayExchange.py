array = []
n = int(0)

def arrayexchange(array):
    while (n + 1) < len(array):
        a = array[n]
        b = array[n + 1]
        array[n] = b
        array[n + 1] = a
        n += 2