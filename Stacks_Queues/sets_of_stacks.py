from functools import reduce


class SetsOfStacks:
    def __init__(self, threshold=10, collection=[]):
        self._current_stack = 0
        self._sets_of_stacks = [[]]
        self._threshold = threshold
        if collection:
            self.build(collection)

    @property
    def current_stack(self):
        return self._sets_of_stacks[self._current_stack]

    def build(self, collection):
        for item in collection:
            self.push(item)

    def next_stack(self):
        self._current_stack += 1
        if len(self._sets_of_stacks) == self._current_stack:
            self._sets_of_stacks.append([])

    def prev_stack(self):
        del self._sets_of_stacks[self._current_stack]
        self._current_stack -= 1

    def pop(self):
        # If we have absolutely nothing don't do anything
        if not self.current_stack and self._current_stack == 0:
            raise Exception("Nothing in stack to pop")

        # If there is nothing to pop and there is another stack, go back
        if not self.current_stack and self._current_stack > 0:
            self.prev_stack()

        popped = self.current_stack.pop()

        # If after the pop we have an empty stack with other stacks, go back
        if not self.current_stack and self._current_stack > 0:
            self.prev_stack()

        return popped

    def push(self, item):
        if len(self.current_stack) == self._threshold:
            self.next_stack()
        self.current_stack.append(item)

    def peek(self):
        return self.current_stack[-1]

    def pop_at(self, index):
        if index < 0 or index >= len(self._sets_of_stacks):
            raise Exception("Index out of Range")

        tail_end = self._sets_of_stacks[index + 1:]
        for i in range(index + 1, len(self._sets_of_stacks)):
            self._sets_of_stacks[i] = []
        self._current_stack = index
        popped = self.pop()
        self.build(reduce(lambda x, y: x + y, tail_end))
        return popped

    def __repr__(self):
        output = []
        num_of_stacks = len(self._sets_of_stacks)
        for i in range(num_of_stacks):
            output.extend(self._sets_of_stacks[i])
        return str(output)
