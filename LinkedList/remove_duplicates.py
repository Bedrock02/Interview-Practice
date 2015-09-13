'''
Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

first approach: would be to have a hash or map that keeps track of what is in the 
linked list. If we already have a key within our map then we need to remove that Node

second approach: have two pointers, one pointer looking at the data and another traversing the list
to see if there exists any duplicates.
'''
from Node import *


def remove_duplicate(head):
	data = {}
	n = head

	data[n.data] = 1
	while n.next != None:
		print data
		if data.has_key(n.next.data):
			if n.next.next != None:
				n.next = n.next.next
			else:
				break
		else:
			data[n.next.data] = 1

		n = n.next

head = Node(1)
head.append_to_tail(2)
head.append_to_tail(4)
head.append_to_tail(7)
head.append_to_tail(4)

remove_duplicate(head)
print head