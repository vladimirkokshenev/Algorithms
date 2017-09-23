
def count_inversions(a):
    """ count inversions implementation

    :param a: input list
    :return: c, b where c is the number of inversions in a, b is sorted version of a
    """

    # base case
    if len(a) == 1:
        return 0, a

    # divide
    a1 = a[0:len(a) / 2]
    a2 = a[len(a) / 2: len(a)]

    # resolve sub-tasks (sort sub-lists and count non-split inversions)
    c1, b1 = count_inversions(a1)
    c2, b2 = count_inversions(a2)

    # merge (combine solution of sub-tasks) and count split-inversions
    cs = 0
    i1 = 0
    i2 = 0
    res = []
    for i in range(len(a)):
        if i1 < len(b1) and i2 < len(b2):
            if b1[i1] < b2[i2]:
                res.append(b1[i1])
                i1 += 1
            else:
                res.append(b2[i2])
                i2 += 1
                cs = cs + len(b1) - i1
        else:
            if i1 == len(b1):
                res.append(b2[i2])
                i2 += 1
            else:
                res.append(b1[i1])
                i1 += 1

    return c1+c2+cs, res


if __name__ == '__main__':
    a = []
    for i in range(100000):
        a.append(int(raw_input()))

    c, b = count_inversions(a)

    print("Number of inversions = %d" % c)