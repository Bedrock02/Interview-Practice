class Node:
    def __init__(self, value):
        self._data = value
        self._left, self._right = None, None

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @left.setter
    def left(self, node):
        self._left = node


class Tree:
    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def insert(self, value, current_node=None, first_pass=True):
        if first_pass and current_node is None:
            current_node = self._root
        if self._size == 0:
            self._root = Node(value)
            self._size += 1
            return
        elif current_node.data > value:
            if current_node.left is None:
                current_node.left = Node(value)
                self._size += 1
            else:
                self.insert(value, current_node.left, False)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
                self._size += 1
            else:
                self.insert(value, current_node.right, False)

    def traverse_level(self):
        output = ""
        queue = [self._root, None]
        while queue:
            # Get all nodes in level
            while queue[0] is not None:
                popped = queue.pop(0)
                output += "{} ".format(popped.data)
                if not popped.left and not popped.right:
                    continue
                if popped.left:
                    queue.append(popped.left)

                if popped.right:
                    queue.append(popped.right)
            # After all Nodes in Level gathered
            # Start New Level, remove None (indicator)
            output += "\n"
            queue.pop(0)
            # If there are still items to print out
            # Indicate a new level
            if queue:
                queue.append(None)
        return output

    def find_kth_in_order_item(self, k, current_node=None):
        '''
        Find Kth Item in Order
        Create a count to see where the kth item is
        '''
        if current_node is None:
            current_node = self._root

        count = 0
        if not current_node.left and not current_node.right:
            return False, 1

        if current_node.left:
            found, result = self.find_kth_in_order_item(k, current_node.left, )
            if found:
                return True, result
            else:
                count += result

            if count == k:
                return True, current_node.left.data

        count += 1
        if count == k:
            return True, current_node.data

        if current_node.right:
            found, result = self.find_kth_in_order_item(k, current_node.right)
            if found:
                return True, result
            else:
                count += result

            if count == k:
                return True, current_node.right.data
        return False, count
