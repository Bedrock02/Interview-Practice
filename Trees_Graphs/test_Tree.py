from tree_2 import *


def test_tree():
    my_tree = Tree()
    my_tree.add(50)
    my_tree.add(10)
    assert my_tree.size == 2
