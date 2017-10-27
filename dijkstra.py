INF = 1000000

def read_graph_from_file(filename):
    """
    Read G from file containing list of edges, costs. 
    :param filename: input file name, containing adjacency list <src dst1,c1 ... dstk,ck>
    :return: G
    """

    fp = open(filename)

    G = []

    adj_line = fp.readline()
    while adj_line != "":
        adj_line = adj_line.split()

        src_node = int(adj_line[0]) - 1

        # extend graph G in case if src_node is not yet there
        while src_node + 1 > len(G):
            G.append([])

        for i in range(1, len(adj_line)):
            edge = adj_line[i].split(',')
            dst_node = int(edge[0]) - 1
            edge_cost = int(edge[1])
            G[src_node].append({"DEST": dst_node, "COST": edge_cost})

        adj_line = fp.readline()

    fp.close()

    return G


def dijkstra(G, s):
    """
    Computes shortest paths on graph G from node i to all other nodes.
    :param G: graph as a adjacency matrix
    :param i: source node
    :return: list of shortest paths
    """

    shortest_path = [INF for i in range(len(G))]
    shortest_path[s] = 0

    visited_nodes = set([s])

    while len(visited_nodes) < len(G):
        # choose an edge using dijkstra greedy score
        dgreedy_min = INF
        src = s
        dst = s
        need_break = True
        for i in visited_nodes:
            for edge in G[i]:
                if shortest_path[i] + edge["COST"] < dgreedy_min and edge["DEST"] not in visited_nodes:
                    dgreedy_min = shortest_path[i] + edge["COST"]
                    src = i
                    dst = edge["DEST"]
                    need_break = False

        if not need_break:
            # put shortest path cost for current node
            shortest_path[dst] = dgreedy_min
            visited_nodes.add(dst)
        else:
            break

    return shortest_path


if __name__ == '__main__':

    G = read_graph_from_file('tests/dijkstraData.txt')

    shortest_path = dijkstra(G, 0)

    print("Path to %d == %d" % (6, shortest_path[6]))
    print("Path to %d == %d" % (36, shortest_path[36]))
    print("Path to %d == %d" % (58, shortest_path[58]))
    print("Path to %d == %d" % (81, shortest_path[81]))
    print("Path to %d == %d" % (98, shortest_path[98]))
    print("Path to %d == %d" % (114, shortest_path[114]))
    print("Path to %d == %d" % (132, shortest_path[132]))
    print("Path to %d == %d" % (164, shortest_path[164]))
    print("Path to %d == %d" % (187, shortest_path[187]))
    print("Path to %d == %d" % (196, shortest_path[196]))
