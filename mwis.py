

def read_path_graph(filename):
    """
    Reads path graph from a file.
    :param filename: source file name (first line specifies number of nodes, subsequent lines represent nodes' weights)
    :return: list of nodes' weights of a path graph
    """

    path_graph = []

    fp = open(filename)
    one_line = fp.readline()
    n = int(one_line)

    path_graph.append(n)

    one_line = fp.readline()
    while one_line != "":
        weight = int(one_line)
        path_graph.append(weight)
        one_line = fp.readline()

    if n != len(path_graph)-1:
        print("Inconsistent input: n doesn't match actual number of nodes!")

    return path_graph


def max_weighted_independent_set(path_graph):
    """
    Computes maximum weighted independent set of a path_graph
    :param path_graph: list of nodes' weights of a path_graph
    :return: max_weight and membership list (True/False)
    """

    A = [0 for i in range(len(path_graph))]

    A[0] = 0
    A[1] = path_graph[1]

    for i in range(2, len(path_graph)):
        A[i] = max(A[i-1], A[i-2] + path_graph[i])

    mwis = [False for i in range(len(path_graph))]

    i = len(path_graph)-1

    while i > 1:
        if A[i-1] >= A[i-2] + path_graph[i]:
            i -= 1
        else:
            mwis[i] = True
            i -= 2

    if i == 1:
        mwis[1] = True

    return A[-1], mwis


if __name__ == '__main__':
    filename = "tests/mwis.txt"
    path_graph = read_path_graph(filename)

    m, mwis = max_weighted_independent_set(path_graph)

    print("Max weight = %d" % m)
    #for i in range(1, len(path_graph)+1):
    #    print("Node %d - %r" % (i, mwis[i]))

    print(mwis[1])
    print(mwis[2])
    print(mwis[3])
    print(mwis[4])
    print(mwis[17])
    print(mwis[117])
    print(mwis[517])
    print(mwis[997])
