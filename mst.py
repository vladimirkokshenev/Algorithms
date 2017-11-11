
INF = 1000000000


def read_graph(filename):
    fp = open(filename)

    one_line = fp.readline()
    str_NE = one_line.split()
    N = int(str_NE[0])
    E = int(str_NE[1])
    print("N = %d, E = %d" % (N, E))

    G = [[] for i in range(N)]

    one_line = fp.readline()

    while one_line != "":
        str_edge = one_line.split()
        # we use 0-based node numbering
        edge_from = int(str_edge[0])-1
        edge_to = int(str_edge[1])-1
        edge_cost = int(str_edge[2])
        G[edge_from].append([edge_to, edge_cost])
        # reverse edge - as G is undirected
        if [edge_from, edge_cost] not in G[edge_to]:
            G[edge_to].append([edge_from, edge_cost])
        one_line = fp.readline()

    return G


class MinHeap:
    """ Min Heap implementation """
    def __init__(self, values=[]):
        """ initializes the heap from list of input values"""
        self.heap = [{"key": values[i], "index": i} for i in range(len(values))]
        self.heap_position = [i for i in range(len(values))]

        if len(self.heap) > 1:
            for i in range(len(self.heap)/2, -1, -1):
                self.heapify(i)

    def heapsize(self):
        """ return heap size """
        return len(self.heap)

    def swap_elements(self, index1, index2):
        """ properly swap element maintaining both heap and heap_position"""

        if index1 >= self.heapsize() or index2 >= self.heapsize():
            # here should be raise exception
            return

        # update heap_position indexes
        pos_ind1 = self.heap[index1]["index"]
        pos_ind2 = self.heap[index2]["index"]
        tmp = self.heap_position[pos_ind1]
        self.heap_position[pos_ind1] = self.heap_position[pos_ind2]
        self.heap_position[pos_ind2] = tmp

        # exchange heap elements (parent with child)
        tmp_element = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = tmp_element

    def insert(self, x):
        """ inserts element x in the heap """
        insert_key = x
        insert_index = self.heapsize()
        self.heap.append({"key": insert_key, "index": insert_index})
        self.heap_position.append(insert_index)

        i = self.heapsize() - 1

        # bubble up inserted element swapping it with parent as long as element key < parent key
        while i > 0 and self.heap[(i-1)/2]["key"] > self.heap[i]["key"]:
            self.swap_elements((i-1)/2, i)
            i = (i-1)/2

    def minimum(self):
        """ returns minimum element (without extraction)"""
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def pop(self):
        """ pops minimum element from the heap """

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            self.heap_position[0] = -1
            return self.heap.pop(0)

        self.swap_elements(0, self.heapsize()-1)
        min_index = self.heap[-1]["index"]
        self.heap_position[min_index] = -1
        ret = self.heap.pop(-1)
        self.heapify(0)
        return ret

    def heapify(self, i):
        """ maintain heap property for i-th element """
        if len(self.heap) == 0:
            return

        heapsize = len(self.heap)
        left = i*2 + 1
        right = i*2 + 2
        smallest = i

        if left < heapsize and self.heap[left]["key"] < self.heap[smallest]["key"]:
            smallest = left

        if right < heapsize and self.heap[right]["key"] < self.heap[smallest]["key"]:
            smallest = right

        if smallest != i:
            self.swap_elements(smallest, i)
            self.heapify(smallest)

    def change_key(self, position_index, new_key):
        """ we change key of specified element if the new key is smaller than current key"""
        i = self.heap_position[position_index]
        if new_key >= self.heap[i]["key"]:
            return

        self.heap[i]["key"] = new_key

        while i > 0 and self.heap[(i-1)/2]["key"] > self.heap[i]["key"]:
            self.swap_elements((i-1)/2, i)
            i = (i-1)/2

if __name__ == '__main__':
    G = read_graph('tests/edges_mst.txt')

    # we add last node to the list of covered nodes
    X = set([len(G) - 1])

    # we create list to initialize heap
    initial_greedy_score = [INF for i in range(len(G)-1)]
    mst_heap = MinHeap(initial_greedy_score)

    for i in range(len(G[-1])):
        edge_to = G[-1][i][0]
        edge_cost = G[-1][i][1]
        mst_heap.change_key(edge_to, edge_cost)

    mst_cost = 0

    while len(X) != len(G):

        next_node = mst_heap.pop()
        X.add(next_node["index"])
        mst_cost += next_node["key"]

        for i in range(len(   G[next_node["index"]]   )):
            edge_to = G[next_node["index"]][i][0]
            edge_cost = G[next_node["index"]][i][1]

            if edge_to not in X:
                mst_heap.change_key(edge_to, edge_cost)

    print("MST cost = %d" % mst_cost)

