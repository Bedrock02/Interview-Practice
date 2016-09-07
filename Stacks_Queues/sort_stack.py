'''Write a program to sort a stack in ascending order. You should not make any assump- tions
 about how the stack is implemented. The following are the only functions
 that should be used to write this program: push | pop | peek | isEmpty.'''

# Solution Explanation
# In order to sort a stack we need another stack
# 1 - if the spare stack is empty we want to push the top element of hte given stack
# to the spare stack
# 2 - else if we have items in the spare stack and we are sorting by acsending order
#	While we don't run out of items to check against the spare stack and the element 
# is greater than the top element in the spare stack, keep poping the spare stack
# 3 - Once we either run out of items or find that the element is < the top element
# in the spare stack then we want to push that element onto the spare stack
# We continue to repeat this step (hence the while) until the given stack is empty
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

sorted_stack = sort_stack(unsorted_stack)
print sorted_stack
print sorted_stack.peek()