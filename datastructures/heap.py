# Reference: Pythons docs, and Python Cookbook

# Heap queue algorithm, AKA priority queue algorithm

# Heaps are binary trees in which each parent is less than or equal
# to any of his children

# Pyhthon's implementation uses arrays

# The algorithm is implemented as followed:
# heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

# The smallest element in the heap is always the root heap[0]

# Python's implementation of the heap is zero based indexing which
# treats the heap as a list in the sense we can access elements in the same
# way

# Im this implementation of the heap, pop will return the smallest element,
# known as the min heap queue
import heapq

heap = [2, 4, 1, 55, -45, -88, 34, 5, 6, 7]

heapq.heapify(heap)

print(heap)  # [-88, -45, 1, 5, 4, 2, 34, 55, 6, 7]

smallest = heapq.nsmallest(3, heap)
largest = heapq.nlargest(3, heap)

print(smallest)  # [-88, -45, 1]
print(largest)  # [55, 34, 7]


# Priority queue:
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    # negative priority will send item to the front of the queue, while
    # index ensures the order in case priority is the same in queue
    # since index will never be the same. More on this on page 10 of
    # Python Cookbook
    def push(self, priority, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]  # returns item name in _queue


priority_queue = PriorityQueue()

priority_queue.push(2, Item('hello'))
priority_queue.push(30, Item('hi'))
priority_queue.push(44, Item('there'))


print(priority_queue._queue)
# [(-44, 2, Item(there)), (-2, 0, Item(hello)), (-30, 1, Item(hi))]

# As seen below, Pythons implements a min heap queue, so pop will return the
# smallest item in the queue
print(priority_queue.pop())  # Item(there)
print(priority_queue.pop())  # Item(hi)
print(priority_queue.pop())  # Item(hello)
