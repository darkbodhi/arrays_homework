array1 = []
array2 = []
n = int(0)

def arrayequal(s1, s2):
    if len(array1) == len(array2):
        pass
    else:
        raise Exception("The arrays are not equal.")
    while n < len(array1):
        if array1(n) == array2(n):
            n += 1
            pass
        else:
            print("The array are not equal")
        return True