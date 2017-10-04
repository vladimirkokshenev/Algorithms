

def max_heapify(A, i, heap_size):
    """
    Maintain heap property for i-th element of array A
    :param A: input array
    :param i: index of element
    :param heap_size: size of the heap in array A
    :return: no return value
    """

    # calculating left and right we need to take into consideration base 0 numbering
    left = 2*(i+1) - 1
    right = 2*(i+1)
    largest = i

    if left <= heap_size and A[left] > A[largest]:
        largest = left
    if right <= heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    """
    Building in-place max heap on array A.
    :param A: input array
    :return: no return value
    """

    # init heap_size to point on last element of A
    heap_size = len(A) - 1

    for i in range((len(A)-1)/2, -1, -1):
        max_heapify(A, i, heap_size)


def heapsort(A):
    """
    Heapsort for input array A
    :param A: input array
    :return: no return value
    """

    build_max_heap(A)
    heap_size = len(A) - 1
    for i in range(len(A)-1, -1, -1):
        heap_size -= 1
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        max_heapify(A, 0, heap_size)