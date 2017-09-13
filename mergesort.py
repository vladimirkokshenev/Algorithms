
def mergesort(a):
    """ mergesort implementation
    
    :param a: input list
    :return: sorted list
    """

    # base case
    if len(a) == 1:
        return a

    # divide
    a1 = a[0:len(a)/2]
    a2 = a[len(a)/2: len(a)]

    # resolve sub-tasks
    b1 = mergesort(a1)
    b2 = mergesort(a2)

    # merge (combine solution of sub-tasks)
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
        else:
            if i1 == len(b1):
                res.append(b2[i2])
                i2 += 1
            else:
                res.append(b1[i1])
                i1 += 1

    return res
