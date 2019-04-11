'''
Write code to remove dups from an unsorted linked list
'''
from collections import Counter


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, collection):
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

    def add_node(self, i):
        new_node = Node(i)

        # Brand New
        if self.head is None:
            self.head = new_node
            return
        last_node = self.get_last_node()
        last_node.next = new_node

    def print_linked_list(self):
        current_node = self.head
        elements = ''
        while current_node:
            elements = elements + "{}, ".format(current_node.data)
            current_node = current_node.next
        return elements


def remove_dups(linked_list):
    element_count = Counter()
    current_node = linked_list.head
    skip_count = False
    while current_node and current_node.next:
        if skip_count:
            skip_count = False
        else:
            element_count[current_node.data] += 1

        next_element = current_node.next

        if element_count[next_element.data] > 0:
            current_node.next = next_element.next
            skip_count = True
        else:
            current_node = current_node.next


def remove_dups_2(linked_list):
    element_count = Counter()
    current_node = linked_list.head
    element_count[current_node.data] += 1
    while current_node.next:
        if element_count[current_node.next.data] > 0:
            current_node.next = current_node.next.next
            continue
        element_count[current_node.next.data] += 1
        current_node = current_node.next
