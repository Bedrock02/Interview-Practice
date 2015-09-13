#Array Implementation
from node import *
class Stack_Array(object):

	def __init__(self,stack_input =[]):
		self.stack = stack_input

	def push(self,data):
		self.stack.append(data)
		return self
	
	def pop(self):
		item_popped = self.peek()
		self.stack = self.stack[:-1]
		return item_popped

	def peek(self):
		return self.stack[-1]
	
	def __str__(self):
		return self.stack.__str__()

class Stack_Node(object):

	def __init__(self,threshold = None):
		self.top = None
		self.size = 0
		self.threshold = threshold

	def set_stack(self,current_stack):
		for element in current_stack:
			self.push(element)
		return self

	def pop(self):
		if self.top != None:
			item_popped = self.top.data
			self.top = self.top.next
			self.size -= 1
			return item_popped
		else:
			return None

	def peek(self):
		return self.top.data

	def push(self,data_input):
		
		if (self.threshold is not None and self.size < self.threshold) or self.threshold is None:
			new_node = Node(data_input)
			

			if self.top is None:
				self.top = new_node
			

			else:
				new_node.next = self.top
				self.top = new_node

			self.size += 1
		
		else:
			return "Your stack is full"
	
	def is_full(self):
		if self.size < self.threshold:
			return False
		return True

	def is_empty(self):
		if self.size == 0:
			return True
		return False

	def __str__(self):
		return self.top.__str__()