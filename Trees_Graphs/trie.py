class TrieNode:
    def __init__(self, data=None):
        self._data = data
        self._children = [None] * 26
        self._is_an_end = False

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def children(self):
        return self._children

    @property
    def is_an_end(self):
        return self._is_an_end

    @is_an_end.setter
    def is_an_end(self, value):
        self._is_an_end = value

class Trie:
    def __init__(self):
        self._children = [None] * 26
        self._is_empty = True

    def search(self, given_string, current_node = None):
        # We are at the top
        children = self._children if current_node is None else current_node.children

        if not given_string:
            return current_node and current_node.is_an_end

        child_index = child_index = ord(given_string[0].lower()) - 97
        if children[child_index] is None:
            return False

        return self.search(given_string[1:], children[child_index])


    def insert(self, given_string, current_node = None):
        if current_node is None:
            first_node = TrieNode(given_string[0])
            child_index = child_index = ord(given_string[0].lower()) - 97
            self._children[child_index] = first_node
            self.insert(given_string[1:], self._children[child_index])
            self._is_empty = False
            return

        if not given_string:
            current_node.is_an_end = True
            return

        child_index = ord(given_string[0].lower()) - 97

        # If character already exists, then continue inserting, else create a node
        if current_node.children[child_index]:
            self.insert(given_string[1:], current_node.children[child_index])
        else:
            new_node = TrieNode(given_string[0])
            current_node.children[child_index] = new_node
            self.insert(given_string[1:], new_node)
