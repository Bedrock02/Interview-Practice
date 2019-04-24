from queue import Queue_list


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return "( {}__ {} __{} )".format(self.left, self.value, self.right)


class Tree:
    def __init__(self, node=None, collection=[]):
        self.head = node
        self.size = 0
        if collection:
            collection.sort()
            self.build(collection)

    def build(self, collection):
        if not collection:
            return
        mid_point = len(collection) // 2
        self.add(collection[mid_point])
        self.build(collection[0: mid_point])
        self.build(collection[mid_point + 1:])

    def add(self, value):
        if self.head == None:
            self.head = TreeNode(value=value)
            self.size += 1
            return
        if self.in_tree(value):
            raise Exception("Item Already Exists")

        self.insert(value, current_node=self.head)

    def in_tree(self, value, current_node=None):
        if current_node == None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return in_tree(value, current_node.left)

        return in_tree(value, current_node.right)

    def insert(self, value, current_node):
        child_name = "left" if value < current_node.value else "right"
        child = getattr(current_node, child_name)
        if child == None:
            setattr(current_node, child_name, TreeNode(value=value))
            self.size += 1
            return
        self.insert(value, child)

    def __str__(self):
        queue = Queue_list()
        queue.enqueue(self.head)
        queue.enqueue(TreeNode())
        output = ""
        while not queue.is_empty():
            popped = queue.dequeue()
            if not popped or popped.value == None:
                output += "\n"
                continue
            print("POPPED {}".format(popped.value))
            output += str(popped.value) + " "
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)
            queue.enqueue(TreeNode(value=None))
        return output


def is_balanced(node=None):
    if node is None:
        return True, None

    if node.left is None and node.right is None:
        return True, 0

    left_balanced, left_value = is_balanced(node.left)
    right_balanced, right_value = is_balanced(node.right)

    if not left_balanced or not right_balanced:
        return False, None

    if left_value and left_value > 1 or right_value and right_value > 1:
        return False, None

    if left_value is None:
        left_height = 0

    right_height = 0 if right_value is None else 1 + right_value
    left_height = 0 if left_value is None else 1 + left_value

    diff = abs(right_height - left_height)

    if diff > 1:
        return False, None
    return True, diff
