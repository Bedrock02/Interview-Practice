from sets_of_stacks import *


def test_build_stack():
    items = [1, 2, 3, 4, 5, 6, 9]
    stack = SetsOfStacks(threshold=3, collection=reversed(items))
    assert str(stack) == '[9, 6, 5, 4, 3, 2, 1]'


def test_peek_stack():
    items = [1, 2, 3, 4, 5, 6, 9]
    stack = SetsOfStacks(threshold=3, collection=reversed(items))
    assert stack.peek() == 1


def test_push_stack():
    items = [1, 2, 3, 4, 5, 6, 9]
    stack = SetsOfStacks(threshold=3, collection=reversed(items))
    stack.push(100)
    assert stack.peek() == 100


def test_pop_stack():
    items = [1, 2, 3, 4, 5, 6, 9]
    stack = SetsOfStacks(threshold=3, collection=reversed(items))
    assert stack.pop() == 1
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 3


def test_pop_at():
    items = [1, 2, 3, 4, 5, 6, 9]
    stack = SetsOfStacks(threshold=3, collection=reversed(items))
    assert stack.pop_at(0) == 5
    assert stack.peek() == 1
