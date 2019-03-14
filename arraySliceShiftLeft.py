array = []
n = int(0)

def arraysliceshiftleft(array, low, hi):
    if low > hi:
        raise Exception("Error. Indexes have wrong value.")
    else:
        pass
    while low <= hi:
        array[0 - n] = array[(0 - n) + 1]
        n += 1
        low += 1

