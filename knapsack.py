import sys
import threading

class Knapsack:

    def __init__(self, items):
        """
        Initializes instance of the class from the list of items. Each element of the list must contain
        a list of two elements [Vi, Wi], where Vi is the Value of i-th item, and Wi is its weight.
        List element number 0 must contain pair [W, N], where W is the Knapsack size and N is the total number of items.
        :param items: list of items
        """
        self.items = items
        self.budget = items[0][0]
        self.amount = items[0][1]
        self.counter_recursive_calls = 0
        self.counter_cache_hits = 0
        self.counter_base_case = 0
        self.cache = {}
        self.optimal_solution = 0

        weight = 1
        self.min_weight = self.items[1][weight]
        for i in range(2, self.amount+1):
            if self.items[i][weight] < self.min_weight:
                self.min_weight = self.items[i][weight]

    def reset(self):
        """
        Resets counters, cache and optimal result.
        :return: 
        """
        self.counter_recursive_calls = 0
        self.counter_cache_hits = 0
        self.counter_base_case = 0
        self.cache = {}
        self.optimal_solution = 0

    def get_counter_recursive_calls(self):
        return self.counter_recursive_calls

    def get_counter_cache_hits(self):
        return self.counter_cache_hits

    def get_counter_base_case(self):
        return self.counter_base_case

    def get_cache_size(self):
        return len(self.cache)

    def get_optimal_solution(self):
        return self.optimal_solution

    def dynamic_programming_alg(self):

        sln = [[0 for j in range(self.budget+1)] for i in range(self.amount+1)]
        weight = 1
        value = 0

        for i in range(1, self.amount+1):
            for w in range(self.budget+1):
                if self.items[i][weight] > w:
                    sln[i][w] = sln[i-1][w]
                else:
                    if sln[i-1][w] > sln[i-1][w - self.items[i][weight]] + self.items[i][value]:
                        sln[i][w] = sln[i-1][w]
                    else:
                        sln[i][w] = sln[i-1][w - self.items[i][weight]] + self.items[i][value]

        self.optimal_solution = sln[self.amount][self.budget]

    def recursive_caching_alg(self, i, j):

        self.counter_recursive_calls += 1

        if i == 0 or j < self.min_weight:
            self.counter_base_case += 1
            return 0

        if (i-1, j) in self.cache:
            self.counter_cache_hits += 1
            s1 = self.cache[(i-1, j)]
        else:
            s1 = self.recursive_caching_alg(i-1, j)
            self.cache[(i-1, j)] = s1

        if (i-1, j-self.items[i][1]) in self.cache:
            self.counter_cache_hits += 1
            s2 = self.cache[(i - 1, j-self.items[i][1])]
        else:
            s2 = self.recursive_caching_alg(i-1, j-self.items[i][1])
            self.cache[(i-1, j-self.items[i][1])] = s2

        if self.items[i][1] > j:
            sln = s1
        else:
            sln = max(s1, s2 + self.items[i][0])
        self.cache[(i, j)] = sln

        return sln

    def trigger_recursive_caching_alg(self):
        self.reset()
        self.optimal_solution = self.recursive_caching_alg(self.amount, self.budget)


def read_items(filename):
    fp = open(filename)
    items = []
    one_line = fp.readline()

    while one_line != "":
        one_line = one_line.split()
        item = [int(one_line[0]), int(one_line[1])]
        items.append(item)
        one_line = fp.readline()

    return items


def knapsack_thread():
    items = read_items('tests/knapsack1.txt')
    ks1 = Knapsack(items)
    ks1.dynamic_programming_alg()
    print("Optimal solution for task 1 is %d" % ks1.get_optimal_solution())

    items = read_items('tests/knapsack_big.txt')
    ks2 = Knapsack(items)
    ks2.trigger_recursive_caching_alg()
    print("Optimal solution for task 2 is %d" % ks2.get_optimal_solution())

    print("Counter_base_case = %d" % ks2.get_counter_base_case())
    print("Counter_cache_hits = %d" % ks2.get_counter_cache_hits())
    print("Counter_recursive_calls = %d" % ks2.get_counter_recursive_calls())
    print("Cache size = %d" % ks2.get_cache_size())


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)

    thread = threading.Thread(target=knapsack_thread)
    thread.start()
