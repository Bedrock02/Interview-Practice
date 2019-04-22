from tree_2 import *


def test_tree():
    my_tree = Tree()
    my_tree.add(50)
    my_tree.add(10)
    assert my_tree.size == 2

def test_is_balanced():
    my_tree = Tree()
    my_tree.add(50)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(20)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(100)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(30)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(25)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == False
