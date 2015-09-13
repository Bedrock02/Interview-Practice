"""Implement a MyQueue class which implements a queue using two stacks."""
from stack import Stack_Node

class MyQueue(object):

	def __init__(self):
		self.push_queue = Stack_Node()
		self.pop_queue = Stack_Node()

	def enqueue(self,data):
		if self.pop_queue.size > 0:
			while self.pop_queue.size > 0:
				self.push_queue.push(self.pop_queue.pop())
		self.push_queue.push(data)

	def dequeue(self):
		if self.push_queue.size > 0:
			while self.push_queue.size > 0:
				self.pop_queue.push(self.push_queue.pop())
		return self.pop_queue.pop()
	
	def peek(self):
		if self.push_queue.size > 0:
			while self.push_queue.size > 0:
				self.pop_queue.push(self.push_queue.pop())
		return self.pop_queue.peek()

	def __str__(self):
		if self.push_queue.size > 0:
			return self.push_queue.__str__()
		else:
			return self.pop_queue.__str__()