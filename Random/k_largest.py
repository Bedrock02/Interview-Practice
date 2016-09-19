"""
Find the kth largest item in an unsorted array
Hint: create a priority queue (min priority)
"""

class Queue(object):
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.insert_sort(item)
    return self

  def dequeue(self):
    if not self.queue:
      return None
    popped_item = self.queue[0]
    self.queue = self.queue[1:]
    return popped_item

  def peek(self):
    return self.queue[0]

  def insert_sort(self, item):
    placement = None
    for idx in xrange(len(self.queue)):
      if self.queue[idx] > item:
        placement = idx
        break
    if placement is None:
      self.queue.append(item)
    else:
      self.queue = self.queue[:placement] + [item] + self.queue[placement:]
    return self

  # 0 == largest
  # 1 == second to largest
  # kth largest = queue[len(queue) - 1 - kth]
  def find_k_largest(self, kth):
    total_length = len(self.queue)
    return self.queue[total_length - 1 - kth]

  def __len__(self):
    return len(self.queue)

  def __str__(self):
    return str(self.queue)
