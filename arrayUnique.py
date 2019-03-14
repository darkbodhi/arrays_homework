def array_unique():
    while n < len(array):
        array2.append(array[n])
    if array[n + 1] in array2:
        array[n + 1].pop()
    else:
        pass
    n += 1

# сложность программы описывается полиномом