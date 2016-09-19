"""
Given two sorted linked lists of integers write an algorithm to merge the two linked lists 
such that the resulting linked list is in sorted order. 
You are expected to define the data structure for linekd lists as well. 
Analyze the time an dspace complexity of hte merge algorithm
Time complexity: O(n), basically need to make n comparisons and append n times to the new list
Space complexity: O(n), as you add more items to your list you are growing n times
"""
from Node import List
list_one = List()
list_two = List()

list_one.append_to_list(1)
list_one.append_to_list(3)
list_one.append_to_list(4)
list_one.append_to_list(6)
list_one.append_to_list(13)
list_one.append_to_list(17)

list_two.append_to_list(2)
list_two.append_to_list(4)
list_two.append_to_list(5)
list_two.append_to_list(7)
list_two.append_to_list(8)
list_two.append_to_list(11)

# iterate one by one
def merge_linked_lists(A, B):
  new_list = List()
  new_list.append_to_list(sort_linked_list(A, B))
  return new_list

def sort_linked_list(A, B):
  peekA = A.peek()
  peekB = B.peek()
  
  if peekA >= 0 and peekB is None:
    return A.head
  if peekB >= 0 and peekA is None:
    return B.head

  if peekA > peekB:
    popped = B.pop_node()
    popped.next = sort_linked_list(A, B)
  
  if peekA <= peekB:
    popped = A.pop_node()
    popped.next = sort_linked_list(A, B)
  return popped
print merge_linked_lists(list_one, list_two)