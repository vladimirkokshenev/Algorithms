from operator import itemgetter


def read_edges(filename):
    fp = open(filename)

    one_line = fp.readline()
    N = int(one_line)
    print("N = %d" % N)

    edges = []

    one_line = fp.readline()

    while one_line != "":
        str_edge = one_line.split()
        # we use 0-based node numbering
        edge_from = int(str_edge[0])-1
        edge_to = int(str_edge[1])-1
        edge_cost = int(str_edge[2])
        edges.append({"SRC": edge_from, "DST": edge_to, "COST": edge_cost})
        one_line = fp.readline()

    fp.close()

    return N, edges


def get_int(bin_rep):
    num = bin_rep[0]
    for i in range(1, len(bin_rep)):
        num = num << 1
        if bin_rep[i] == 1:
            num += 1
    return num


def read_edges_2(filename):
    fp = open(filename)

    one_line = fp.readline().split()
    N = int(one_line[0])
    B = int(one_line[1])
    print("N = %d, B = %d" % (N, B))

    nodes = []

    one_line = fp.readline()

    while one_line != "":
        str_rep = one_line.split()
        bin_rep = [int(str_rep[i]) for i in range(len(str_rep))]
        val = get_int(bin_rep)
        nodes.append(val)
        one_line = fp.readline()

    fp.close()

    return N, B, nodes


class DisjointSet:
    def __init__(self, n):
        """
        Init disjoint set for n elements
        :param n: number of elements (elements ids are from 0 to N-1)
        """
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.size = n

    def find(self, x):
        """
        Finds to which "leader" set belongs element x. Path compression optimization is handled in parallel.
        :param x: element for which we'll find a set it belongs to.
        :return: set leader id
        """

        path_compression_list = []
        current_element = x

        while self.parent[current_element] != current_element:
            path_compression_list.append(current_element)
            current_element = self.parent[current_element]

        for i in range(len(path_compression_list)):
            self.parent[path_compression_list[i]] = current_element

        return current_element

    def join(self, x, y):
        """
        Join two sets where x and y are leaders.
        :param x: leader of the first set
        :param y: leader of the second set
        :return: 
        """

        if self.rank[x] == self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y

        self.size -= 1

        if self.size % 1000 == 0:
            print("Current size of Disjoint set is %d" % self.size)


def get_distance(x, y):
    """
    get Hamming distance between x and y
    :param x: first arg (int)
    :param y: second arg (int)
    :return: Hamming distance
    """

    c = x ^ y
    dist = 0
    while c!= 0:
        dist += c&1
        c = c>>1

    return dist


def generate_edges(max_d, nodes):
    """
    generate those edges, that have distance 0, 1, ..., max_d
    :param nodes: list of nodes' data
    :param max_d: max edge cost
    :return: list of lists
    """

    edges = [[] for i in range(0, max_d+1)]

    for i in range(len(nodes)-1):
        if i%10 == 0:
            print("Handling bucket = %d" % i)
        for j in range(i+1, len(nodes)):
            dist = get_distance(nodes[i], nodes[j])
            if dist<=max_d:
                edges[dist].append([i, j])

    return edges


def clustering1():
    n, edges = read_edges('tests/clustering1.txt')

    dj_set = DisjointSet(n)
    edges.sort(key=itemgetter("COST"))

    cur = 0
    while dj_set.size > 4:
        src = edges[cur]["SRC"]
        dst = edges[cur]["DST"]
        src_leader = dj_set.find(src)
        dst_leader = dj_set.find(dst)
        if src_leader != dst_leader:
            dj_set.join(src_leader, dst_leader)

        # print("Step id - %d" % cur)
        # print(dj_set.parent)
        # print(dj_set.rank)
        # raw_input()

        cur += 1

    while dj_set.find(edges[cur]["SRC"]) == dj_set.find(edges[cur]["DST"]):
        cur += 1

    print("Max spacing for k-clustering where k==4 is %d" % edges[cur]["COST"])


def clustering2():
    N, B, nodes = read_edges_2('tests/clustering_big.txt')

    if N != len(nodes):
        print("Input Error!")
        exit(1)

    dj_set = DisjointSet(N)

    distinct_values = {}

    for i in range(N):
        if nodes[i] in distinct_values:
            distinct_values[nodes[i]].append(i)
        else:
            distinct_values[nodes[i]] = [i]

    visited = [False for i in range(N)]

    # handle clusters in BFS-style
    for node in range(N):
        if not visited[node]:
            queue = [node]
            cluster_root = node
            while queue:
                cur_node = queue.pop(0)
                visited[cur_node] = True

                # handle distance 0
                if nodes[cur_node] in distinct_values:
                    for i in range(len(distinct_values[nodes[cur_node]])):
                        src_leader = dj_set.find(cluster_root)
                        dst_leader = dj_set.find(distinct_values[nodes[cur_node]][i])
                        if src_leader != dst_leader:
                            dj_set.join(src_leader, dst_leader)
                    distinct_values.pop(nodes[cur_node])

                # handle distance 1
                for i in range(24):
                    xor_arg = 1 << i
                    # ***
                    new_value = nodes[cur_node] ^ xor_arg
                    if new_value in distinct_values:
                        join_list = distinct_values.pop(new_value)
                        for k in range(len(join_list)):
                            src_leader = dj_set.find(cluster_root)
                            dst_leader = dj_set.find(join_list[k])
                            if src_leader != dst_leader:
                                dj_set.join(src_leader, dst_leader)
                        queue.extend(join_list)

                # handle distance 2
                for i in range(23):
                    xor_i = 1 << i
                    for j in range(i+1, 24):
                        xor_j = 1 << j
                        xor_arg = xor_i | xor_j
                        # ***
                        new_value = nodes[cur_node] ^ xor_arg
                        if new_value in distinct_values:
                            join_list = distinct_values.pop(new_value)
                            for k in range(len(join_list)):
                                src_leader = dj_set.find(cluster_root)
                                dst_leader = dj_set.find(join_list[k])
                                if src_leader != dst_leader:
                                    dj_set.join(src_leader, dst_leader)
                            queue.extend(join_list)

    print("Number of cluster = %d" % dj_set.size)


if __name__ == '__main__':
    clustering1()
    clustering2()



