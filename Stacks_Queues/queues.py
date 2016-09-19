from node import *
from stack import Stack_Array
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
		
		else:
			return None
	
	def peek(self):
		return self.first.data

	def __str__(self):
		return self.first.__str__()

class Queue_Stack(object):
	def __init__(self):
		self.stack_one = Stack_Array()
		self.stack_two = Stack_Array()

	# if we want to push something and it is empty add to stack_one
	# if we want to push and we have elements in stack_one but not stack_two just push
	# If we want to push and we have no elements in stack_one
	def enqueue(self, data):
		if self.stack_two.is_empty() or self.is_empty():
			self.stack_one.push(data)
		elif self.stack_one.is_empty():
			self.transfer()
			self.stack_one.push(data)

	def transfer(self):
		if self.stack_one.is_empty() and self.stack_two.is_empty():
			return
		stack_to_empty = self.stack_two if self.stack_one.is_empty() else self.stack_one
		stack_to_fill = self.stack_one if self.stack_one.is_empty() else self.stack_one
		while not stack_to_empty.is_empty():
			popped_item = stack_to_empty.pop()
			stack_to_fill.push(popped_item)

	def size(self):
		return self.stack_one.__len__() + self.stack_two.__len__()

	def __str__(self):
		if self.stack_one.is_empty() and self.stack_two.is_empty():
			return [].__str__()
		if self.stack_two.is_empty():
			print(self.stack_one)
		if not self.stack_one.is_empty():
			self.transfer()
			return self.stack_one.__str__()
	def is_empty(self):
		return self.stack_one.is_empty() and self.stack_two.is_empty()

some_queue = Queue_Stack()
some_queue.enqueue(5)
print(some_queue)
