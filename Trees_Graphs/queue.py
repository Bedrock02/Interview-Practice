from node import *
class Queue_Node(object):

	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def enqueue(self,data):
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
		
		if self.first != None:
			item_removed = self.first
			self.first = self.first.next
			self.size -= 1
			return item_removed
		else:
			return None
	
	def peek(self):
		return self.first.data

	def is_empty(self):
		if self.size is 0:
			return True
		return False

	def __str__(self):
		return self.first.__str__()
