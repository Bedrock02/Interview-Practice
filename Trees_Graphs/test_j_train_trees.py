from j_train_trees import *

def test_tree_insert():
    my_tree = Tree()

    assert my_tree.size == 0
    my_tree.insert(5)
    assert my_tree.size == 1
    my_tree.insert(6)
    assert my_tree.size == 2

def test_tree_level_traverse():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(6)
    my_tree.insert(7)

    assert my_tree.traverse_level() == "5 \n6 \n7 \n"

    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(2)
    my_tree.insert(7)
    my_tree.insert(1)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(8)

    assert my_tree.traverse_level() == "5 \n2 7 \n1 3 6 8 \n"
