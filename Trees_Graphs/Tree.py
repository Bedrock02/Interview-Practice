from queue import *


def cmp(a, b):
    return (a > b) - (a < b)


class BST(object):

    __slots__ = "root", "length"

    def __init__(self):
        self.root = BSTNode()
        self.length = 0

    def insert(self, data):
        spot = self.root.search(data)
        if spot.val is None:
            spot.val = data
            spot.left = BSTNode()
            spot.right = BSTNode()
            self.length += 1

    def delete(self, data):
        find_spot = self.root.search(data)
        if find_spot.val is None:
            raise "Data does not exist in tree"

        elif find_spot.left.val is None and find_spot.right.val is None:
            find_spot.val = None
            self.length -= 1

        elif find_spot.left.val is not None and find_spot.right.val is not None:
            min_right = find_spot.right.min()
            new_replacement = min_right.val
            self.delete(new_replacement)
            find_spot.val = new_replacement
            self.length -= 1
        else:
            if find_spot.left.val is None and find_spot.right.val is not None:
                find_spot.val = find_spot.right.val
                find_spot.left = find_spot.right.left
                find_spot.right = find_spot.right.right

            else:
                find_spot.val = find_spot.left.val
                find_spot.left = find_spot.left.left
                find_spot.right = find_spot.left.right
            self.length -= 1

    def in_order_traversal(self):
        self.root.in_order()

    def pre_order_traversal(self):
        self.root.pre_order()

    def post_order_traversal(self):
        self.root.post_order()

    def depth_search(self, data):
        return self.root.depth_first_search(data)

    def breath_search(self, data):
        return self.root.breath_first_search(data)

    def __str__(self):
        output = ""
        breath_queue = Queue_Node()
        breath_queue.enqueue(self.root)
        output += str(self.root.val)
        while not breath_queue.is_empty():
            popped = breath_queue.dequeue()
            if popped.data.val == "\n":
                output += "\n"
                continue
            left_value = popped.data.left.val if popped.data.left else ""
            right_value = popped.data.left.val if popped.data.right else ""
            output += "{} {}".format(left_value, right_value)
            if popped.data.left:
                breath_queue.enqueue(popped.data.left)
            if popped.data.right:
                breath_queue.enqueue(popped.data.right)
            breath_queue.enqueue(BSTNode(val="\n"))


class BSTNode(object):

    __slots__ = "val", "left", "right"

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        if val is not None:
            self.left = left if left is not None else BSTNode()
            self.right = right if right is not None else BSTNode()

    def search(self, query):
        if self.val is None:
            return self

        cmpValue = cmp(self.val, query)

        if cmpValue is 0:
            return self

        elif cmpValue is -1:
            return self.right.search(query)

        else:
            return self.left.search(query)

    def in_order(self):
        if self.left.val is not None:
            self.left.in_order()

        print(self.val)

        if self.right.val is not None:
            self.right.in_order()

    def pre_order(self):
        print(self.val)

        if self.left.val is not None:
            self.left.pre_order()

        if self.right.val is not None:
            self.right.pre_order()

    def post_order(self):
        if self.left.val is not None:
            self.left.post_order()

        if self.right.val is not None:
            self.right.post_order()

        print(self.val)

    def max(self):
        if self.right.val is None:
            return self
        return self.right.max()

    def min(self):
        if self.left.val is None:
            return self
        return self.left.min()

    def depth_first_search(self, data):
        if self.val is data:
            return self

        if self.left.val is not None:
            found = self.left.depth_first_search(data)
            if found:
                return found

        if self.right.val is not None:
            found = self.right.depth_first_search(data)
            if found:
                return found

    def breath_first_search(self, data):
        breath_queue = Queue_Node()
        breath_queue.enqueue(self)
        while not breath_queue.is_empty():
            popped = breath_queue.dequeue()

            if popped.data.val is data:
                return popped.data

            else:
                if popped.data.left.val is not None:
                    breath_queue.enqueue(popped.data.left)

                if popped.data.right.val is not None:
                    breath_queue.enqueue(popped.data.right)

    def __str__(self):
        if self.val is None:
            return "_"
        else:
            return "(%s %s %s)" % (self.left, self.val, self.right)


my_tree = BST()
my_tree.insert(50)
my_tree.insert(25)
my_tree.insert(100)
my_tree.insert(10)
my_tree.insert(30)
my_tree.insert(75)
my_tree.insert(150)
print(my_tree)
