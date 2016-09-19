#Array Implementation
from node import *
class Stack_Array(object):

	def __init__(self, stack_input =[]):
		self.stack = stack_input

	def push(self, data):
		self.stack.append(data)
		return self
	
	def pop(self):
		item_popped = self.peek()
		self.stack = self.stack[:-1]
		return item_popped

	def peek(self):
		return self.stack[-1]
	
	def is_empty(self):
		return self.__len__() == 0

	def __len__(self):
		return self.stack.__len__()
	
	def __str__(self):
		return self.stack

class Stack_Node(object):

	def __init__(self, threshold=None):
		self.top = None
		self.size = 0
		self.threshold = threshold

	def set_stack(self, current_stack):
		for element in current_stack:
			self.push(element)
		return self

	def pop(self):
		if not self.top:
			return None
		item_popped = self.top.data
		self.top = self.top.next
		self.size -= 1
		return item_popped

	def peek(self):
		return self.top.data

	def push(self, data_input):
		if self.threshold is not None and self.size > self.threshold:
			return "Your stack is full"
		new_node = Node(data_input)
		if self.top is None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node
		self.size += 1
	
	def is_full(self):
		return self.size < self.threshold

	def is_empty(self):
		return self.size == 0

	def __str__(self):
		return self.top.__str__()