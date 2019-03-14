def arrayIncrement():

    my_array = [1, 2, 3]
    n = int(0)
    z = int(0)
    increment_number = int(input("Please, insert the number of increment: "))
    while n < len(my_array):
        my_array[z] += 1
        n += 1
        z += 1