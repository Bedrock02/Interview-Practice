from collections import Counter
'''
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the Ts digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
Output: 9 -> 1 -> 2.That is, 912.
'''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        self.size = 0
        if collection:
            self.create_list(collection)

    def create_list(self, collection):
        for i in collection:
            self.add_node(i)

    def get_last_node(self):
        current_node = self.head
        if not current_node:
            return None

        while current_node.next:
            current_node = current_node.next
        return current_node

    def pop(self):
        if not self.head:
            raise Exception("There is nothing to pop")

        popped_element = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped_element

    def add_node(self, i):
        new_node = Node(i)

        # Brand New
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        last_node = self.get_last_node()
        last_node.next = new_node
        self.size += 1

    def print_linked_list(self):
        current_node = self.head
        elements = ''
        while current_node:
            elements = elements + "{}, ".format(current_node.data)
            current_node = current_node.next
        return elements


'''
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
'''


def add_two_linked_list_numbers(linked_list_1, linked_list_2):
    newLinkedList = LinkedList()
    carry_over = 0

    while linked_list_1.size != 0 or linked_list_2.size != 0:
        additive_1 = linked_list_1.pop() if linked_list_1.size != 0 else 0
        additive_2 = linked_list_2.pop() if linked_list_2.size != 0 else 0

        sum = additive_1 + additive_2 + carry_over

        single_digit = sum % 10
        carry_over = sum // 10
        newLinkedList.add_node(single_digit)

    if carry_over != 0:
        newLinkedList.add_node(carry_over)

    return newLinkedList
