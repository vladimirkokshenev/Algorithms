import numpy
import itertools
import gc
import sys
import threading


INF = numpy.float32(999999999.9)


def read_points(filename):

    fp = open(filename)

    n = int(fp.readline())
    points = {}
    one_line = fp.readline()
    i = 1

    while one_line != "":
        [x, y] = map(float, one_line.split())
        points[i] = [x, y]
        i += 1
        one_line = fp.readline()

    return points


def get_distances(points):

    distances = {}

    for i in points:
        for j in points:
            if i == j:
                distances[(i, j)] = 0.0
            else:
                d = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0])
                d += (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
                res = numpy.sqrt(d)
                distances[(i, j)] = numpy.float32(res)
                distances[(j, i)] = numpy.float32(res)

    return distances


def get_set_mask(s, n):

    msk = 0

    for i in range(1, n+1):
        if i in s:
            msk = (msk << 1) | 1
        else:
            msk = msk << 1

    return msk


def tsp_thread():
    filename = 'tests/tsp.txt'
    points = read_points(filename)
    # print(points)
    distances = get_distances(points)
    # print(distances)

    n = len(points)
    A_prev = {(get_set_mask([1], n), 1): numpy.float32(0.0)}
    A_cur = {}

    pids = [i for i in points]

    # print pids

    # 2^n sub-problems
    for m in range(2, n + 1):
        # s_combinations = list(itertools.combinations(pids, m))
        for s in itertools.combinations(pids, m):
            if 1 in s:
                # dynamic programming solution for each sub-problem
                for j in s:
                    if j != 1:
                        s_no_j = set(s)
                        s_no_j.remove(j)
                        s_no_j = frozenset(s_no_j)
                        s_no_j = get_set_mask(s_no_j, n)

                        min_val = INF
                        for k in s:
                            if k != j:
                                if (s_no_j, k) in A_prev:
                                    cur_dist = A_prev[(s_no_j, k)] + distances[(k, j)]
                                else:
                                    cur_dist = INF
                                if cur_dist < min_val:
                                    min_val = cur_dist
                        A_cur[(get_set_mask(s, n), j)] = numpy.float32(min_val)
                        # print("done")
        del A_prev
        A_prev = A_cur
        A_cur = {}
        # print A_prev
        gc.collect()
        print("Done with m=%d" % m)

    min_val = INF
    for j in range(2, n + 1):
        if A_prev[(get_set_mask(pids, n), j)] + distances[(j, 1)] < min_val:
            min_val = A_prev[(get_set_mask(pids, n), j)] + distances[(j, 1)]

    print("TSP shortest tour is %f" % min_val)

    """
    A_prev = {(frozenset([1]), 1): 0.0}
    A_cur = {}
    n = len(points)

    pids = [i for i in points]

    #print pids

    # 2^n subproblems
    for m in range(2, n+1):
        s_combinations = list(itertools.combinations(pids, m))
        for s in s_combinations:
            if 1 in s:
                # dynamic programming solution for each subproblem
                for j in s:
                    if j != 1:
                        s_no_j = set(s)
                        s_no_j.remove(j)
                        s_no_j = frozenset(s_no_j)

                        min_val = INF
                        for k in s:
                            if k != j:
                                if (s_no_j, k) in A_prev:
                                    cur_dist = A_prev[(s_no_j, k)] + distances[(k, j)]
                                else:
                                    cur_dist = INF
                                if cur_dist < min_val:
                                    min_val = cur_dist
                        A_cur[(frozenset(s), j)] = min_val
                        #print("done")
        del A_prev
        A_prev = A_cur
        A_cur = {}
        #print A_prev
        print("Done with m=%d" % m)

    min_val = INF
    for j in range(2, n+1):
        if A_prev[(frozenset(pids), j)] + distances[(j, 1)] < min_val:
            min_val = A_prev[(frozenset(pids), j)] + distances[(j, 1)]

    print("TSP shortest tour is %f" % min_val)
    """

if __name__ == '__main__':
    #threading.stack_size(67108864)
    #sys.setrecursionlimit(2 ** 20)

    #thread = threading.Thread(target=tsp_thread)
    #thread.start()

    filename = 'tests/tsp.txt'
    points = read_points(filename)
    # print(points)
    distances = get_distances(points)
    # print(distances)

    n = len(points)
    A_prev = {(get_set_mask([1], n), 1): numpy.float32(0.0)}
    A_cur = {}

    pids = [i for i in range(2, n+1)]

    # print pids

    # 2^n sub-problems
    for m in range(1, n):
        s_combinations = list(itertools.combinations(pids, m))
        for ss in s_combinations:
            s = list(ss)
            s.insert(0, 1)
            if 1 in s:
                # dynamic programming solution for each sub-problem
                for j in s:
                    if j != 1:
                        s_no_j = set(s)
                        s_no_j.remove(j)
                        s_no_j = frozenset(s_no_j)
                        s_no_j = get_set_mask(s_no_j, n)

                        min_val = INF
                        for k in s:
                            if k != j:
                                if (s_no_j, k) in A_prev:
                                    cur_dist = A_prev[(s_no_j, k)] + distances[(k, j)]
                                else:
                                    cur_dist = INF
                                if cur_dist < min_val:
                                    min_val = cur_dist
                        A_cur[(get_set_mask(s, n), j)] = numpy.float32(min_val)
                        # print("done")
        del A_prev
        A_prev = A_cur
        A_cur = {}
        # print A_prev
        gc.collect()
        print("Done with m=%d" % m)

    min_val = INF
    pids.insert(0, 1)
    for j in range(2, n + 1):
        if A_prev[(get_set_mask(pids, n), j)] + distances[(j, 1)] < min_val:
            min_val = A_prev[(get_set_mask(pids, n), j)] + distances[(j, 1)]

    print("TSP shortest tour is %f" % min_val)






