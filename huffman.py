from operator import itemgetter
import sys
import threading


class HuffmanTree:
    def __init__(self, symbol=-1, weight=0, left_child=None, right_child=None):
        self.left = left_child
        self.right = right_child
        self.symbol = symbol
        self.weight = weight

    def is_metasymbol(self):
        if self.symbol == -1:
            return True
        else:
            return False

    def get_weight(self):
        return self.weight

    def print_tree(self):
        print("Node weight = %d" % self.weight)
        print("Node symbol = %d" % self.symbol)
        if self.left:
            print("Printing left child...")
            self.left.print_tree()
        if self.right:
            print("Printing right child...")
            self.right.print_tree()

    def max_depth(self, depth=0):

        left_depth = depth
        if self.left:
            left_depth = self.left.max_depth(depth+1)

        right_depth = depth
        if self.right:
            right_depth = self.right.max_depth(depth+1)

        return max(left_depth, right_depth)

    def min_depth(self, depth=0):

        left_depth = depth
        if self.left:
            left_depth = self.left.min_depth(depth + 1)

        right_depth = depth
        if self.right:
            right_depth = self.right.min_depth(depth + 1)

        return min(left_depth, right_depth)


def read_symbol_weights(filename):
    """
    Read symbol weights from input file and stores them in a list as [i, w], where i is symbol index, w is weight
    :param filename: source filename
    :return: list of symbols with weights
    """

    fp = open(filename)
    one_line = fp.readline()
    n = int(one_line)

    symbol_weights = []

    one_line = fp.readline()
    i = 0
    while one_line != "":
        weight = int(one_line)
        symbol_weights.append([i, weight])
        one_line = fp.readline()
        i += 1

    symbol_weights.sort(key=itemgetter(1))

    return symbol_weights


def build_symbol_queue(symbol_weights):
    """
    Builds a queue consisting of primary symbols.
    :param symbol_weights: sorted array of symbols and weights (list of [i,w])
    :return: queue of instances of HuffmanTree corresponding to leaves
    """
    symbol_queue = []
    for i in range(len(symbol_weights)):
        symbol_queue.append(HuffmanTree(symbol_weights[i][0], symbol_weights[i][1]))

    return symbol_queue


def get_min_weight_symbol(symbol_queue, super_symbol_queue):
    """
    Pops and returns a symbol objects with min wieght from either symbol_queue or super_symbol_queue
    :param symbol_queue: queue of regular symbols
    :param super_symbol_queue: queue of super symbols
    :return: symbol (instance of HuffmanTree) with min weight
    """

    if len(symbol_queue) + len(super_symbol_queue) == 0:
        return None

    if len(symbol_queue) == 0:
        return super_symbol_queue.pop(0)

    if len(super_symbol_queue) == 0:
        return symbol_queue.pop(0)

    if symbol_queue[0].weight <= super_symbol_queue[0].weight:
        return symbol_queue.pop(0)
    else:
        return super_symbol_queue.pop(0)


def build_huffman_tree(symbol_queue, super_symbol_queue):
    """ """

    sym_a = get_min_weight_symbol(symbol_queue, super_symbol_queue)
    sym_b = get_min_weight_symbol(symbol_queue, super_symbol_queue)

    sym_ab = HuffmanTree(-1, sym_a.get_weight() + sym_b.get_weight(), sym_a, sym_b)

    # if no more symbols left - return sym_ab as a root of Huffman tree
    if len(symbol_queue) + len(super_symbol_queue) == 0:
        return sym_ab
    # else - put new super_symbol in corresponding queue (at the end), and recurse
    else:
        super_symbol_queue.append(sym_ab)
        ht_root = build_huffman_tree(symbol_queue, super_symbol_queue)
        return ht_root


def thread_huffman():
    filename = "tests/huffman.txt"
    symbol_weights = read_symbol_weights(filename)
    symbol_queue = build_symbol_queue(symbol_weights)
    super_symbol_queue = []
    huffman_tree = build_huffman_tree(symbol_queue, super_symbol_queue)
    # huffman_tree.print_tree()
    print("Max codeword = %d" % huffman_tree.max_depth())
    print("Min codeword = %d" % huffman_tree.min_depth())

if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)

    thread = threading.Thread(target=thread_huffman)
    thread.start()
