
class MinHeap:
    """ Min Heap implementation """
    def __init__(self, values=[]):
        """ initializes the heap from list of input values"""
        self.data = values

        if len(self.data) > 1:
            for i in range(len(self.data)/2, -1, -1):
                self.heapify(i)

    def heapsize(self):
        """ return heapsize """
        return len(self.data)

    def insert(self, x):
        """ inserts element x in the heap """
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0 and self.data[(i-1)/2] > self.data[i]:
            tmp = self.data[(i-1)/2]
            self.data[(i - 1) / 2] = self.data[i]
            self.data[i] = tmp
            i = (i-1)/2

    def minimum(self):
        """ returns minimum element (without extraction)"""
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def pop(self):
        """ pops minimum element from the heap """

        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop(0)

        ret = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.heapify(0)
        return ret

    def heapify(self, i):
        """ maintain heap property for i-th element """
        if len(self.data) == 0:
            return

        heapsize = len(self.data)
        left = i*2 + 1
        right = i*2 + 2
        smallest = i

        if left < heapsize and self.data[left] < self.data[smallest]:
            smallest = left

        if right < heapsize and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != i:
            tmp = self.data[i]
            self.data[i] = self.data[smallest]
            self.data[smallest] = tmp
            self.heapify(smallest)


class MaxHeap:
    """ Max Heap implementation """
    def __init__(self, values=[]):
        """ initializes the heap from list of input values"""
        self.data = values

        if len(self.data) > 1:
            for i in range(len(self.data)/2, -1, -1):
                self.heapify(i)

    def heapsize(self):
        """ return heapsize """
        return len(self.data)

    def insert(self, x):
        """ inserts element x in the heap """
        self.data.append(x)
        i = len(self.data) - 1
        while i > 0 and self.data[(i-1)/2] < self.data[i]:
            tmp = self.data[(i-1)/2]
            self.data[(i - 1) / 2] = self.data[i]
            self.data[i] = tmp
            i = (i-1)/2

    def maximum(self):
        """ returns maximum element (without extraction)"""
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def pop(self):
        """ pops minimum element from the heap """

        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop(0)

        ret = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.heapify(0)
        return ret

    def heapify(self, i):
        """ maintain heap property for i-th element """
        if len(self.data) == 0:
            return

        heapsize = len(self.data)
        left = i*2 + 1
        right = i*2 + 2
        largest = i

        if left < heapsize and self.data[left] > self.data[largest]:
            largest = left

        if right < heapsize and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            tmp = self.data[i]
            self.data[i] = self.data[largest]
            self.data[largest] = tmp
            self.heapify(largest)



