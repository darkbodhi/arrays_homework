array = []
n = int(0)


def arraysort():
    while n < len(array):
        while n < len(array):
            if array[n] <= array[n + 1]:
                a = array[n]
                b = array[n + 1]
                array[n] = b
                array[n + 1] = a
                n += 1
            else:
                return n == 0
        n += 1