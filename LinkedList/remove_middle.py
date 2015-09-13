'''
Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
'''
from Node import *

def remove_middle(middle):
	n = middle
	while n.next != None:
		n.data = n.next.data
		if n.next.next is None:
			n.next = None
			break
		n = n.next

linkedList = List("a")
linkedList.append_to_list("b")
linkedList.append_to_list("c")
linkedList.append_to_list("d")
linkedList.append_to_list("e")

middle_node = linkedList.get_node("c")
remove_middle(middle_node)

print linkedList