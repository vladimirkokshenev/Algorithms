import sys
import threading
import datetime
from operator import itemgetter


def read_graph_from_file(filename):
    """
    Read G from file containing list of edges. Construct Grev in parallel.
    :param filename: input file name, containing list of edges (each edge is a pair of integers, each edge on a new line)
    :return: G, Grev
    """

    fp = open(filename)

    edges = []

    max_node = 0

    edge_as_line = fp.readline()
    while edge_as_line != "":
        edge_as_line = edge_as_line.split()

        src_node = int(edge_as_line[0]) - 1
        dst_node = int(edge_as_line[1]) - 1

        if src_node > max_node:
            max_node = src_node

        if dst_node > max_node:
            max_node = dst_node

        edges.append([src_node, dst_node])

        edge_as_line = fp.readline()

    G = [[] for i in range(max_node + 1)]
    Grev = [[] for i in range(max_node + 1)]

    for i in range(len(edges)):

        src_node = edges[i][0]
        dst_node = edges[i][1]

        # building G
        if dst_node not in G[src_node]:
            G[src_node].append(dst_node)

        # building Grev
        if src_node not in Grev[dst_node]:
            Grev[dst_node].append(src_node)

    fp.close()

    return G, Grev


def dfs1(Grev, i, explored_nodes, fintime_nodes, cur_ft):
    """
    First pass DFS recursive function to establish finishing time order for SCC alg. Runs on graph Grev.
    :param Grev: graph Grev (as adjacency  list)
    :param i: current node number
    :param explored_nodes: list of boolean numbers, where true is for explored nodes, and false is for unexplored.
    :param fintime_nodes: list of finishing times.
    :param cur_ft: current finishing time.
    :return: updated current finishing time.
    """

    # mark i as explored
    explored_nodes[i] = True

    # check all nodes adjacent with i
    for j in Grev[i]:
        if not explored_nodes[j]:
            cur_ft = dfs1(Grev, j, explored_nodes, fintime_nodes, cur_ft)

    # assign finishing time for i and adjust cur_ft
    fintime_nodes[i] = cur_ft
    cur_ft = cur_ft + 1

    # return adjusted cur_ft value, is it will be required in up-the-call-stack instances
    return cur_ft


def dfs2(G, i, explored_nodes, scc_membership, leader, scc_size):
    """
    Second pass recursive DFS for computing SCC alg. Mark nodes according to SCC membership (using leader id).
    And counts number of nodes in an SCC.
    :param G: input graph G (as adjacency list)
    :param i: current node number
    :param explored_nodes: list of boolean numbers, where true is for explored nodes, and false is for unexplored.
    :param scc_membership: leader id is used to represent scc membership
    :param leader: leader node id (all nodes in this scc will be marked with leader id)
    :param scc_size: current SCC size
    :return: adjusted SCC size
    """

    # mark i as explored
    explored_nodes[i] = True
    scc_size = scc_size + 1
    scc_membership[i] = leader

    # check all nodes adjacent with i
    for j in G[i]:
        if not explored_nodes[j]:
            scc_size = dfs2(G, j, explored_nodes, scc_membership, leader, scc_size)

    # return adjusted scc_size value, as it will be required in up-the-call-stack instances
    return scc_size


def dfs1_loop(Grev):
    """
    DFS loop function for the first pass of an SCC 
    :param Grev: graph Grev (as adjacency list)
    :return: fintime_nodes which is a list of caluclated finishing times for all nodes
    """

    n = len(Grev)
    explored_nodes = [False for i in range(n)]
    fintime_nodes = [n for i in range(n)]
    cur_ft = 0

    # DFS-loop for the first pass - to get finishing times
    for i in range(n - 1, -1, -1):
        if not explored_nodes[i]:
            cur_ft = dfs1(Grev, i, explored_nodes, fintime_nodes, cur_ft)

    return fintime_nodes


def dfs2_loop(G, search_order):
    """
    DFS loop function for the second pass of an SCC alg. Colors SCCs, and calculate it's sizes
    :param G: input graph G (as adjacency list)
    :param search_order: list of node ids, established on the first pass of algorithm.
    :return: list of SCC sizes, membership list
    """

    n = len(G)

    explored_nodes = [False for i in range(n)]
    scc_membership = [-1 for i in range(n)]

    scc_sizes = []

    for i in search_order:
        if not explored_nodes[i[0]]:
            scc_size = 0
            leader = i[0]
            scc_size = dfs2(G, i[0], explored_nodes, scc_membership, leader, scc_size)
            scc_sizes.append(scc_size)

    return scc_sizes, scc_membership


def get_search_order_for_second_pass(fintime_nodes):
    """
    Get remaped order for 2nd DFS loop.
    :param fintime_nodes: finishing time list calculated by the first pass
    :return: list representing order for the second pass
    """

    search_order = []

    for i in range(len(fintime_nodes)):
        search_order.append([i, fintime_nodes[i]])

    search_order = sorted(search_order, key=itemgetter(1), reverse=True)

    return search_order


def scc():
    filename = 'Tests/SCC.txt'

    print("Started reading graph:")
    print(datetime.datetime.now().ctime())

    G, Grev = read_graph_from_file(filename)

    print("Done reading graph:")
    print(datetime.datetime.now().ctime())

    fintime_nodes = dfs1_loop(Grev)

    print("Done with 1st pass:")
    print(datetime.datetime.now().ctime())

    search_order = get_search_order_for_second_pass(fintime_nodes)

    scc_sizes, scc_membership = dfs2_loop(G, search_order)

    print("Done with 2nd pass:")
    print(datetime.datetime.now().ctime())

    scc_sizes.sort(reverse=True)

    print("Top 5 SCC sizes are:")

    for i in range(5):
        if i < len(scc_sizes):
            print(scc_sizes[i])
        else:
            print(0)


if __name__ == '__main__':

    threading.stack_size(67108864)
    sys.setrecursionlimit(2**20)

    thread = threading.Thread(target=scc)
    thread.start()

