
def read_data(filename):
    """
    Read data from file containing list of integers. 
    :param filename: input file name, containing array of integers
    :return: list
    """

    fp = open(filename)

    A = []

    one_line = fp.readline()
    while one_line != "":
        x = int(one_line)
        A.append(x)
        one_line = fp.readline()

    return A


def hash_table_based():
    filename = "tests/2sum.txt"
    M = 10000

    fp = open(filename)

    A = set([])

    B = [t for t in range(10000, -10001, -1)]
    B = set(B)

    t_count = 0
    one_line = fp.readline()
    A.add(int(one_line))
    one_line = fp.readline()

    i = 0

    while one_line != "":
        x = int(one_line)

        C = set([])
        for t in B:

            if x != t-x and (t-x) in A:
                t_count += 1
                C.add(t)

        B.difference_update(C)
        A.add(x)

        one_line = fp.readline()
        i += 1
        if i%1000 == 0:
            print("Done %d" % i)
            print("current counter = %d" % t_count)

    print("Total: %d" % t_count)


def binary_search(A, b):
    if (b < A[0]) or (b > A[-1]):
        return -1

    low = 0
    high = len(A)

    while low < high:
        mid = (low+high)/2
        if b < A[mid]:
            high = mid
        else:
            low = mid + 1

    return high


def binary_search_based():
    filename = "tests/2sum.txt"
    M = 10000
    A = read_data(filename)
    A.sort()

    B = set([])

    for i in range(len(A)):
        x = A[i]
        left_border = 0-M-x
        right_border = M-x

        j = binary_search(A, left_border)

        if j != -1:
            while (j < len(A)) and (A[j] <= right_border):
                B.add(x+A[j])
                j += 1

    print("Count = %d" % len(B))

if __name__ == '__main__':

    binary_search_based()

