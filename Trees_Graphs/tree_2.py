from queue import Queue_list


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return "( {}__ {} __{} )".format(self.left, self.value, self.right)


class Tree:
    def __init__(self, node=None):
        self.head = node
        self.size = 0

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
        # TODO: Refactor
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
        queue.enqueue(TreeNode(value=None))
        output = ""
        while not queue.is_empty():
            popped = queue.dequeue()
            if popped.value == None:
                output += "\n"
                continue
            output += str(popped.value) + " "
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)
            queue.enqueue(TreeNode(value=None))
        return output

def is_balanced(current_node):
    if not current_node.left and not current_node.right:
        return  True, 0

    left_diff = None
    right_diff = None
    right_balanced = None
    left_balanced = None

    if current_node.left:
        left_balanced, left_diff = is_balanced(current_node.left)
    if current_node.right:
        right_balanced, right_diff = is_balanced(current_node.right)

    if left_balanced is False or right_balanced is False:
        return False, None

    if left_diff is not None and right_diff is None:
        calc_diff = 1 + left_diff

    elif right_diff is not None and left_diff is None:
        calc_diff = 1 + right_diff

    else:
        calc_diff = (1 + right_diff) - (1 + left_diff)

    return (False, None) if abs(calc_diff) > 1 else (True, calc_diff)
