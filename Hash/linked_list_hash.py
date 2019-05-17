'''
Hash is meant for strings only
'''

class Node:
    def __init__(self, key = None, value = None, next = None):
        self._key = key
        self._value = value
        self._next = next

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

class linked_hash:
    def __init__(self):
        self._hash_map = {}
        self._size = 0

    def add_to_list(self, key, value):
        prev_node = None
        curr_node = self._hash_map[key[0]]
        while curr_node is not None:
            if curr_node.key == key:
                curr_node.value = value
                return
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = Node(key, value)
        self._size += 1

    def insert(self, key, value):
        if key[0] in self._hash_map:
            self.add_to_list(key, value)
        else:
            self._hash_map[key[0]] = Node(key, value)
            self._size += 1

    def delete(self, key):
        if key[0] not in self._hash_map:
            raise Exception("Key: {}, does not exist".format(key))

        prev_node = None
        curr_node = self._hash_map[key[0]]

        while curr_node and curr_node.key is not key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            raise Exception("Key: {}, does not exist".format(key))

        if prev_node and curr_node:
            prev_node.next = curr_node.next
            return

        if curr_node.next is not None:
            self._hash_map[key[0]] = curr_node.next
        else:
            del self._hash_map[key[0]]

        self._size -= 1


    def __setitem__(self, key, value):
        self.insert(key,value)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self._size

    def __str__(self):
        output = ""
        for item in self._hash_map:
            curr_node = self._hash_map[item]
            while curr_node:
                output += "{}:{}, ".format(curr_node.key, curr_node.value)
                curr_node = curr_node.next
        return "{ " + output + "}"
