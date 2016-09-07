from node import *
class Queue_Node(object):

	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def enqueue(self, data):
		new_node = Node(data)
		if self.first is None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node
		
		self.size += 1
		return self
	
	def dequeue(self):
		if self.first is None:
			return None
		item_removed = self.first
		self.first = self.first.next
		self.size -= 1
		return item_removed

	def peek(self):
		return self.first.data

	def is_empty(self):
		return self.size is 0

	def __str__(self):
		return self.first.__str__()

class Queue_list(object):

	def __init__(self):
		self.queue = []
		self.size = 0

	def enqueue(self, data):
		self.queue.append(data)
		self.size += 1
		return self
	
	def dequeue(self):
		if self.queue is None:
			return None
		item_removed = self.queue[0]
		self.queue = self.queue[1:]
		self.size -= 1
		return item_removed
	
	def peek(self):
		return self.queue[0]

	def is_empty(self):
		return not self.queue

	def __str__(self):
		return self.queue.__str__()
