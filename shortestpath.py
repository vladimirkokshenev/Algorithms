import readgraph
from mst import MinHeap
from copy import deepcopy


def bellman_ford(G, src):
    """ 
    Implementation of Bellman-Ford algorithm to find shortest paths from source node to all other nodes.
    :param G: input graph G as in/out adjacency list
    :param src: src node number
    :return: list A of shortest paths from src node to all other nodes, using Bellman-Ford algorithm, 
    or empty list if negative cycles are detected in input graph G.
    """

    A = [[readgraph.INF for i in range(G[0]["N"]+1)] for j in range(G[0]["N"]+1)]

    A[0][src] = 0

    for i in range(1, G[0]["N"]+1):
        for v in range(1, G[0]["N"]+1):
            min_val = A[i-1][v]
            for w in G[v]["IN"]:
                if A[i-1][w] + G[v]["IN"][w] < min_val:
                    min_val = A[i-1][w] + G[v]["IN"][w]
            A[i][v] = min_val

    for i in range(1, G[0]["N"]+1):
        if A[G[0]["N"]-1][i] != A[G[0]["N"]][i]:
            return []

    return A


def floyd_warshall(G):
    """
    Implementation of Floyd_Warshall algorithm to find all shortest paths in graph G.
    :param G: input graph G as in/out adjacency list
    :return: list A (with all recurrent solutions obtained)
    """

    n = G[0]["N"]

    A_prev = [[readgraph.INF for i in range(n+1)] for j in range(n+1)]

    for i in range(1, n+1):
        A_prev[i][i] = 0
        for j in G[i]["OUT"]:
            A_prev[i][j] = G[i]["OUT"][j]

    A_cur = [[readgraph.INF for i in range(n+1)] for j in range(n+1)]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                A_cur[i][j] = min(A_prev[i][j], A_prev[i][k] + A_prev[k][j])

        A_prev = A_cur
        A_cur = [[readgraph.INF for i in range(n + 1)] for j in range(n + 1)]

        if k%10==0:
            print("%d percents completed" % (k/10))

    return A_prev


def dijkstra(G, s):
    """
    Computes shortest paths on graph G from node i to all other nodes.
    :param G: graph as a adjacency matrix
    :param i: source node
    :return: list of shortest paths
    """

    n = G[0]["N"]

    shortest_path = [readgraph.INF for i in range(n+1)]
    shortest_path[s] = 0

    min_heap_init = list(shortest_path)

    for d in G[s]["OUT"]:
        min_heap_init[d] = G[s]["OUT"][d]

    mheap = MinHeap(min_heap_init)

    visited_nodes = set([s])

    while len(visited_nodes) < n:
        # choose an edge using dijkstra greedy score

        next_node = mheap.pop()
        visited_nodes.add(next_node["index"])
        shortest_path[next_node["index"]] = next_node["key"]

        for d in G[next_node["index"]]["OUT"]:
            mheap.change_key(d, next_node["key"] + G[next_node["index"]]["OUT"][d])

    return shortest_path


def johnson_1_extra_node(G):
    """
    Implementaion of step 1 of Johnson's algorithm. It adds new node <n+1> to graph G.
    Node <n+1> has connections to all other nodes, with the cost of 0.
    :param G: input graph G as in/out adjacency list
    :return: new graph Gm
    """

    Gm = deepcopy(G)
    Gm[0]["E"] += Gm[0]["N"]
    Gm[0]["N"] += 1
    Gm.append({"IN":{}, "OUT":{}})
    for i in range(1, Gm[0]["N"]):
        Gm[i]["IN"][Gm[0]["N"]] = 0
        Gm[Gm[0]["N"]]["OUT"][i] = 0

    return Gm


def johnson_3_adjust_edge_costs(G, bfsp):
    """
    Step 3 of Johnson's algorithm. It uses shortest paths from extra node to all other nodes, obtained on step 2,
    to adjust edge costs (u,v) as Ce_new = Ce + bfsp[u] - bfsp[v]
    :param G: input graph G as in/out adjacency list
    :param bfsp: bellman-ford shortest paths from new node to all existing nodes
    :return: new graph Gm with updated edge costs
    """

    Gm = deepcopy(G)
    n = Gm[0]["N"]

    for u in range(1, n+1):
        for v in Gm[u]["OUT"]:
            new_edge_cost = Gm[u]["OUT"][v] + bfsp[-1][u] - bfsp[-1][v]
            Gm[u]["OUT"][v] = new_edge_cost
            Gm[v]["IN"][u] = new_edge_cost

    return Gm


def johnson_5_adjust_shortest_paths_values(ssp, bfsp):
    """
    Step 5 of Johnson's algorithm. It adjusts back shortest path values ssp obtained by dijkstra algorithm
    on step 4 back. ssp[u][v] = ssp[u][v] - bfsp[u] + bfsp[v]
    :param ssp: shortest paths obtained by dijkstra
    :param bfsp: bellman-ford computations from step 2
    :return: modified ssp
    """
    n = len(ssp)
    for u in range(1, n):
        for v in range(1, n):
            ssp[u][v] = ssp[u][v] - bfsp[-1][u] + bfsp[-1][v]

    return ssp


def johnson(G):
    """
    Implementation of Johnson's algorithm to find all shortest paths in graph G.
    :param G: input graph G as in/out adjacency list
    :return: list A (with all solutions obtained from dijkstra)
    """

    # step 1 - add extra node
    Gm = johnson_1_extra_node(G)

    # step 2 - run bellman-ford from this extra node
    A = bellman_ford(Gm, Gm[0]["N"])
    if not A:
        print("Negative cycle detected!")
        exit(1)

    # step 3 - adjust edge costs
    Gm = johnson_3_adjust_edge_costs(G, A)

    # step 4 - run dijkstra on Gm for each node
    ssp = []
    ssp.append([])
    for s in range(1, Gm[0]["N"]+1):
        shortest_paths_from_s = dijkstra(Gm, s)
        ssp.append(shortest_paths_from_s)
        if s%10 == 0:
            print("%d percents completed" % (s/10))

    # step 5 - modify ssp back
    ssp = johnson_5_adjust_shortest_paths_values(ssp, A)

    return ssp


if __name__ == '__main__':
    G = readgraph.read_graph_from_edge_list_into_in_out_adjacency_list('tests/g3.txt')
    n = G[0]["N"]
    ssp = johnson(G)

    min_val = ssp[1][1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if ssp[i][j] < min_val:
                min_val = ssp[i][j]

    print("Shortest shortest path is % d" % min_val)







    """
    A = bellman_ford(G, 1)
    if not A:
        print("negative cycle detected by Belman-Ford")
    else:
        print("NO negative cycle detected by Belman-Ford, starting Floyd-Warshall")
        del A
        A = floyd_warshall(G)
        min_val = A[1][1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if A[i][j] < min_val:
                    min_val = A[i][j]
        print("shortest shortest path is %d" % min_val)
    """


