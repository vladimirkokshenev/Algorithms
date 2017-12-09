INF = 999999999999


def read_graph_from_edge_list_into_adjacency_list(filename):
    """
    Method expects input file containing directed graph in following format:
    1st row - integers N, E, where N is total number of nodes, and E is a total number of edges.
    Each of following rows represent exactly one edge and has a format "from_edge to_edge cost".
    Edges in input file are numbered contiguously starting from 1 to N.
    :param filename: input file name
    :return: graph G represented as adjacency list. 
    Element <i> in the list represent the list of adjacent nodes with node <i>, it is those nodes <j> 
    for which edge <i,j> exists. Element 0 is a list, containing N and E.
    Example:
    Input file:
    3 3     # 3 nodes and 3 edges
    1 2 3   # from node 1 to node 2 with the cost of 3
    1 3 4   # from node 1 to node 3 with the cost of 4
    2 3 5   # from node 2 to node 3 with the cost of 5
    Output list G: [[3, 3], [[2, 3], [3, 4]], [[3, 5]], [] ] 
    """

    fp = open(filename)
    N, E = map(int, fp.readline().split())
    G = [{} for i in range(N+1)]
    G[0]["N"] = N
    G[0]["E"] = E

    one_line = fp.readline()
    while one_line != "":
        [src, dst, cost] = map(int, one_line.split())
        G[src][dst] = cost
        one_line = fp.readline()

    return G


def read_graph_from_edge_list_into_adjacency_matrix(filename):
    """
    Method expects input file containing directed graph in following format:
    1st row - integers N, E, where N is total number of nodes, and E is a total number of edges.
    Each of following rows represent exactly one edge and has a format "from_edge to_edge cost".
    Edges in input file are numbered contiguously starting from 1 to N.
    :param filename: input file name
    :return: graph G represented as adjacency matrix. 
    G[i][j] = c, means that there is edge with the cost of c from i to j (otherwise, G[i][j] = INF).
    G[i][i] = 0.
    G[0][0] = E
    Example:
    Input file:
    3 3     # 3 nodes and 3 edges
    1 2 3   # from node 1 to node 2 with the cost of 3
    1 3 4   # from node 1 to node 3 with the cost of 4
    2 3 5   # from node 2 to node 3 with the cost of 5
    Output list G: [ [3, INF, INF, INF], [3, 0, 3, 4], [3, INF, 0, 5], [3, INF, INF, 0]]
    """

    fp = open(filename)
    N, E = map(int, fp.readline().split())
    G = [[INF for j in range(N+1)] for i in range(N+1)]
    G[0][0] = E

    one_line = fp.readline()
    while one_line != "":
        [src, dst, cost] = map(int, one_line.split())
        G[src][dst] = cost
        one_line = fp.readline()

    return G


def read_graph_from_edge_list_into_in_out_adjacency_list(filename):
    """
    Method expects input file containing directed graph in following format:
    1st row - integers N, E, where N is total number of nodes, and E is a total number of edges.
    Each of following rows represent exactly one edge and has a format "from_edge to_edge cost".
    Edges in input file are numbered contiguously starting from 1 to N.
    :param filename: input file name
    :return: graph G represented as adjacency list. And for each node we will store 
    separate set of IN edges and OUT edges.
    [ {"N": N, "E":E},                                  <- list element 0
      ...
      { "IN": {w: Cwv, ...}, "OUT": {u: Cvu, ...} },    <- list element element v
      ...
    ]
    
    Example:
    Input file:
    3 3     # 3 nodes and 3 edges
    1 2 3   # from node 1 to node 2 with the cost of 3
    1 3 4   # from node 1 to node 3 with the cost of 4
    2 3 5   # from node 2 to node 3 with the cost of 5
    Output list G:
    [ {"N": 3, "E": 3},
      { "IN": {}, "OUT": {2: 3, 3: 4}},
      { "IN": {1: 3}, "OUT": {3: 5}},
      { "IN": {1: 4, 2: 5}, "OUT": {}} ]
    
    """

    fp = open(filename)
    N, E = map(int, fp.readline().split())
    G = [{"IN": {}, "OUT": {}} for i in range(N+1)]
    G[0] = {"N": N, "E": E}

    one_line = fp.readline()
    while one_line != "":
        [src, dst, cost] = map(int, one_line.split())
        G[src]["OUT"][dst] = cost
        G[dst]["IN"][src] = cost
        one_line = fp.readline()

    return G
