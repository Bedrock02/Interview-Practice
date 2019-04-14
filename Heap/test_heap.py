from heap import *


def test_build_heap():
    test_collection = [4, 2, 10]
    my_heap = Heap(test_collection)
    assert my_heap.heap == [3, 10, 2, 4]


def test_add_to_heap():
    test_collection = [4, 2, 10]
    my_heap = Heap(test_collection)
    my_heap.add_element(15)
    assert my_heap.heap == [4, 15, 10, 4, 2]


def test_remove_from_heap():
    test_collection = [4, 2, 10]
    my_heap = Heap(test_collection)
    my_heap.add_element(15)
    assert my_heap.remove_element() == 15
    assert my_heap.heap == [3, 10, 2, 4]
