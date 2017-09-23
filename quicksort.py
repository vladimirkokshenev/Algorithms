

def choose_pivot_first(a, leftind, rightind):
    """Returns index of pivot element in list a between left and right inclusively. 
    First element of sublist is selected as pivot
    
    :param a: input list
    :param leftind: left edge of sublist (belongs to sublist)
    :param rightind: right edge of sublist (belongs to sublist)
    :return: pivot, index - where pivot is a value of pivot element, and index is an index of pivot element
    """

    return a[leftind], leftind


def choose_pivot_last(a, leftind, rightind):
    """Returns index of pivot element in list a between left and right inclusively. 
    Last element of sublist is selected as pivot

    :param a: input list
    :param leftind: left edge of sublist (belongs to sublist)
    :param rightind: right edge of sublist (belongs to sublist)
    :return: pivot, index - where pivot is a value of pivot element, and index is an index of pivot element
    """

    return a[rightind], rightind


def choose_pivot_median(a, leftind, rightind):
    """Returns index of pivot element in list a between left and right inclusively. 
    Median element is selected as pivot (take first, take middle, take last and choose medium of them)

    :param a: input list
    :param leftind: left edge of sublist (belongs to sublist)
    :param rightind: right edge of sublist (belongs to sublist)
    :return: pivot, index - where pivot is a value of pivot element, and index is an index of pivot element
    """

    lpivot = a[leftind]
    rpivot = a[rightind]
    mindex = leftind + (rightind-leftind)/2
    mpivot = a[mindex]

    if rpivot < lpivot:
        tmp = rpivot
        rpivot = lpivot
        lpivot = tmp

        tmp = rightind
        rightind = leftind
        leftind = tmp

    if mpivot < lpivot:
        tmp = mpivot
        mpivot = lpivot
        lpivot = tmp

        tmp = mindex
        mindex = leftind
        leftind = tmp

    if mpivot > rpivot:
        tmp = mpivot
        mpivot = rpivot
        rpivot = tmp

        tmp = mindex
        mindex = rightind
        rightind = tmp

    return mpivot, mindex


def quicksort(a, left_ind, right_ind, choose_pivot):
    """
    
    :param a: input list
    :param left_ind: defines left edge of sublist (is inlcuded into sublist)
    :param right_ind: defins right edge of sublist (is included into sublist)
    :param choose_pivot: defines pivot selection function
    :param comparisons: defines number of comparisons in quicksort
    :return: adjusted number of comparisons
    """

    # base case
    if right_ind - left_ind + 1 < 3:
        # if it is a single element array - do nothing and return 0 number of comparisons
        if right_ind - left_ind + 1 == 1:
            return 0
        # if it is a two element array - sort it and return 1 as number of comparisons
        if right_ind - left_ind + 1 == 2:
            if a[left_ind] > a[right_ind]:
                tmp = a[left_ind]
                a[left_ind] = a[right_ind]
                a[right_ind] = tmp
            return 1

    # add requested m-1 comparisons, where m is the number of elements in sub-array
    comparisons = right_ind - left_ind

    # get pivot element and it's index
    pivot, p_index = choose_pivot(a, left_ind, right_ind)

    # put pivot on the left place
    if p_index != left_ind:
        tmp = a[left_ind]
        a[left_ind] = a[p_index]
        a[p_index] = tmp

    # partition sub-array around the pivot
    i = left_ind + 1
    for j in range(left_ind + 1, right_ind + 1):
        if a[j] < pivot:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i = i+1

    tmp = a[left_ind]
    a[left_ind] = a[i-1]
    a[i-1] = tmp

    l_comp = 0
    r_comp = 0

    if i-2 >= left_ind:
        l_comp = quicksort(a, left_ind, i-2, choose_pivot)
    if i <= right_ind:
        r_comp = quicksort(a, i, right_ind, choose_pivot)

    return comparisons + l_comp + r_comp


if __name__ == '__main__':

    a = []
    for i in range(10000):
        a.append(int(raw_input()))

    b = list(a)
    c = quicksort(b, 0, 9999, choose_pivot_first)
    print("First element as a pivot: %d" % c)

    b = list(a)
    c = quicksort(b, 0, 9999, choose_pivot_last)
    print("Last element as a pivot: %d" % c)

    b = list(a)
    c = quicksort(b, 0, 9999, choose_pivot_median)
    print("Median element as a pivot: %d" % c)
