array = []
n = int(0)

def arrayShiftRight(array):
    while n < len(array):
        array.pop([n])
        array[0 + n] = array[-1 + n]
        n += 1
