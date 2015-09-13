class Node(object):

	def __init__(self,data_input):
		self.data = data_input
		self.next = None
	
	def __str__(self):
		if self.next is None:
			return str(self.data)
		return str(self.data) + " | " + self.next.__str__()
