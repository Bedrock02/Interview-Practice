from stack import Stack_Node
class Stack_Set(object):
	def __init__(self,threshold_input = 5):
		self.stacks = {}
		self.threshold = threshold_input

	def push(self,data):
		if len(self.stacks) == 0:
			self.stacks[len(self.stacks) + 1] = Stack_Node(5)
			self.stacks[len(self.stacks)].push(data)
		
		elif self.stacks[len(self.stacks)].is_full():
			self.stacks[len(self.stacks) + 1] = Stack_Node(5)
			self.stacks[len(self.stacks)].push(data)

		else:
			self.stacks[len(self.stacks)].push(data)
		return self

	def pop(self):
		if self.stacks[len(self.stacks)].size == 1:
			del self.stacks[len(self.stacks)]
		else:
			self.stacks[len(self.stacks)].pop()
		return self

	def number_of_stacks(self):
		return len(self.stacks)

	def popAt(stack_index):
		self.stacks[stack_index].pop()
	
	def __str__(self):
		output = ""
		for stack in self.stacks:
			output+= str(stack) + ": " + self.stacks[stack].__str__() + "\n"
		return output
