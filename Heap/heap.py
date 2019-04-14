class Heap:
    def __init__(self, collection=[]):
        if collection:
            print("BUILD")
            self.build(collection)
        else:
            self.__heap = [0]

    @property
    def heap(self):
        return self.__heap

    @heap.getter
    def heap(self):
        return self.__heap

    @heap.setter
    def heap(self, collection):
        self.__heap = collection

    @property
    def size(self):
        return self.__heap[0]

    @heap.getter
    def size(self):
        return self.heap[0]

    def build(self, collection):
        self.heap = [len(collection)] + collection
        self.balance()

    def balance(self):
        for x in reversed(range(self.heap[0] // 2)):
            self.heapify(x)

    def heapify(self, i):
        element_index = i + 1
        if element_index > self.size:
            return
        left_index = 2 * element_index
        right_index = 2 * element_index + 1
        max = element_index
        if self.size >= left_index and self.heap[max] < self.heap[left_index]:
            max = left_index
        if self.size >= right_index and self.heap[max] < self.heap[right_index]:
            max = right_index
        if max != i:
            self.heap[max], self.heap[element_index] = self.heap[element_index], self.heap[max]
            self.heapify(max)

    def add_element(self, value):
        self.heap.append(value)
        self.heap[0] += 1
        self.balance()

    def remove_element(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        popped = self.heap.pop()
        self.heap[0] -= 1
        self.balance()
        return popped
