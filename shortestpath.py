import readgraph


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


if __name__ == '__main__':
    G = readgraph.read_graph_from_edge_list_into_in_out_adjacency_list('tests/g3.txt')
    n = G[0]["N"]
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



