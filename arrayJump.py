random_array = [5, 3, 2, 4, 1, 0]
n = int(0)
nodes_list = []

def array_jump():
    while not n in nodes_list:
        nodes_list.append(n)
        n = random_array[n]
    return n