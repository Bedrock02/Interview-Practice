from Node import *

'''
Implement an algorithm to find the nth to last element of a singly linked list.
'''

def nth_to_last(number,list_input):
	if number > list_input.size:
		return "List is not large enough"
	
	distance = list_input.size - number

	n = list_input.head
	if distance == 0:
		return list_input.head

	node_count = 1 
	while n.next != None and node_count <= distance:
		node_count += 1
		n = n.next
	
	return n

linkedList = List(Node(6))
linkedList.append_to_list(5)
linkedList.append_to_list(4)
linkedList.append_to_list(3)
linkedList.append_to_list(2)
linkedList.append_to_list(32)
linkedList.append_to_list(1)

print nth_to_last(3,linkedList)