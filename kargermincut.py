import random
import math


def read_graph(filename):
    """
    Read graph G from input file
    :param filename: source file name
    :return: graph G as a list of elements [i, [i1,i2,...,ik] ], where i is the node, and i1,...,ik are incident nodes.
    """

    fp = open(filename)
    G = []
    ln = fp.readline()
    while ln != "":
        ln = ln.split()
        new_element = [int(ln[0]), []]
        for i in range(1, len(ln)):
            new_element[1].append(int(ln[i]))
        G.append(new_element)
        ln = fp.readline()

    return G


def get_edges(G):
    """
    Extract list of edges from input graph G
    :param G: graph G as a list of elements [i, [i1,i2,...,ik] ], where i is the node, and i1,...,ik are incident nodes.
    :return: list of edges [u, v], where u<=v, u,v are nodes
    """
    edges = []
    for i in range(len(G)):
        for k in range(len(G[i][1])):
            if G[i][0] <= G[i][1][k]:
                edges.append([G[i][0], G[i][1][k]])
    return edges


def remove_self_loops(edges):
    """
    Removes self-loop edges from edges (i.e. those [u,v] elements, where u==v)
    :param edges: list of edges [u, v], where u<=v, u,v are nodes
    :return: edges without self loops
    """

    if len(edges) == 0:
        return edges

    i = 0
    while i < len(edges):
        if edges[i][0] == edges[i][1]:
            edges.pop(i)
        else:
            i += 1

    return edges


def mincut(G):
    """
    Calculates mincut of graph G and returns the result (i.e. number of crossing edges, and two sets representing cut parts)
    :param G: input graph G 
    :return: value corresponding to min cut
    """

    # create sets for nodes
    cuts = []
    for i in range(len(G)):
        cuts.append(set())
        cuts[-1].add(G[i][0])

    edges = get_edges(G)
    edges = remove_self_loops(edges)

    i = 0

    while i < len(G)-2 and len(edges) > 0:
        # pop random edge
        edge = edges.pop(random.randint(0, len(edges)-1))
        # merge node edge[1] into node edge[0]
        for k in range(0, len(edges)):
            if edges[k][0] == edge[1]:
                edges[k][0] = edge[0]
            if edges[k][1] == edge[1]:
                edges[k][1] = edge[0]
        edges = remove_self_loops(edges)

        i += 1

    return len(edges)


if __name__ == '__main__':

    filename = 'Tests/kargerMinCut.txt'

    G = read_graph(filename)

    min_cut_value = len(G)

    # int(math.ceil(len(G)*len(G)*math.log(len(G))))
    for i in range(2000):
        new_cut = mincut(G)
        if new_cut < min_cut_value:
            min_cut_value = new_cut

    print("Min cut = %d" % min_cut_value)

