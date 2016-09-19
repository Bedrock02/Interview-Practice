class List(object):
	def __init__(self,head_data = None):
		
		if head_data is None:
			self.head = None
			self.size = 0
		
		else:
			self.head = Node(head_data)
			self.size = 1

	def append_to_list(self,data):
		if self.head is None:
			self.head = Node(data)
		else:
			self.head.append_to_tail(data)
		
		self.size += 1

		return self

	def get_node(self,data):
		return self.head.find(data)

	def remove_node(self,data):
		self.head.delete_node(data)
		self.size -= 1
		return self

	def pop_node(self):
		popped_node = self.head
		if self.head.next is None:
			self.head = None
		else:
			self.head = self.head.next
			popped_node.next = None
		self.size -= 1
		return popped_node
	
	def peek(self):
		return self.head.data if self.head else None

	def __len__():
		return self.size		
	def __str__(self):
		return self.head.__str__()

class Node(object):

	def __init__(self,data_input):
		self.data = data_input
		self.next = None

	def append_to_tail(self,data):
		end = Node(data)
		n = self
		
		while n.next is not None:
			n = n.next

		n.next = end;
		return self
	
	def find(self,data_input):
		n = self
		if n.data == data_input:
			return self
		
		while n.next != None:
			n = n.next
			if n.data == data_input:
				return n
		return None

	def pop_head(self):
		if self.next is None:
			self.data = None
			self.next = None

		else:
			self.data = self.next.data
			self.next = self.next.next
		return self

	#does not pop off the front
	def delete_node(self,data_input):
		n = self
		if n.data is data_input:
			self.pop_head()

		while n.next is not None:
			if n.next.data is data_input:
				n.next = n.next.next
				return self
			n = n.next
		return self
		
	def __str__(self):
		if self.next is None:
			return str(self.data)
		return str(self.data) + " | " + self.next.__str__()