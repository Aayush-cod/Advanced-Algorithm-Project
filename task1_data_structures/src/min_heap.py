from city_data import CityData


class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, city: CityData):
        self.heap.append(city)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[i].distance < self.heap[self._parent(i)].distance:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def peek_min(self):
        return self.heap[0] if self.heap else None

    def extract_min(self):
        if not self.heap:
            return None
        min_city = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return min_city

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = self._left(i), self._right(i)
            if left < n and self.heap[left].distance < self.heap[smallest].distance:
                smallest = left
            if right < n and self.heap[right].distance < self.heap[smallest].distance:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    @classmethod
    def heapify(cls, cities):
        h = cls()
        h.heap = list(cities)
        n = len(h.heap)
        for i in range(n // 2 - 1, -1, -1):
            h._sift_down(i)
        return h
