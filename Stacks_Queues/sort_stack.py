'''Write a program to sort a stack in ascending order. You should not make any assump- tions
 about how the stack is implemented. The following are the only functions
 that should be used to write this program: push | pop | peek | isEmpty.'''

from stack import Stack_Node
def sort_stack(stack):
	
	spare_stack = Stack_Node()
	while not stack.is_empty():
		if spare_stack.is_empty():
			spare_stack.push(stack.pop())

		else:
			element = stack.pop()
			while not spare_stack.is_empty() and element > spare_stack.peek():
				stack.push(spare_stack.pop())
			spare_stack.push(element)
		
	return spare_stack


unsorted_stack = Stack_Node()
unsorted_stack.push(1)
unsorted_stack.push(2)
unsorted_stack.push(8)
unsorted_stack.push(3)
unsorted_stack.push(9)
unsorted_stack.push(4)

print sort_stack(unsorted_stack)