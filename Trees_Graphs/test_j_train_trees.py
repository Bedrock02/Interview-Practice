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


def test_tree_find_kth_in_order():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(1)
    my_tree.insert(4)

    assert my_tree.find_kth_in_order_item(1) == (True, 1)
    assert my_tree.find_kth_in_order_item(2) == (True, 3)
    assert my_tree.find_kth_in_order_item(3) == (True, 4)
    assert my_tree.find_kth_in_order_item(4) == (True, 5)
    assert my_tree.find_kth_in_order_item(5) == (True, 6)
    assert my_tree.find_kth_in_order_item(6) == (False, my_tree.size)


def test_tree_find_kth_in_order_with_list():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(1)
    my_tree.insert(4)

    assert my_tree.find_kth_in_order_item_with_list(1) == 1
    assert my_tree.find_kth_in_order_item_with_list(2) == 3
    assert my_tree.find_kth_in_order_item_with_list(3) == 4
    assert my_tree.find_kth_in_order_item_with_list(4) == 5
    assert my_tree.find_kth_in_order_item_with_list(5) == 6
    assert my_tree.find_kth_in_order_item_with_list(6) == None


def test_tree_find_kth_in_order_iteratively():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(1)
    my_tree.insert(4)

    assert my_tree.find_kth_in_order_item_iterative(1) == 1
    assert my_tree.find_kth_in_order_item_iterative(2) == 3
    assert my_tree.find_kth_in_order_item_iterative(3) == 4
    assert my_tree.find_kth_in_order_item_iterative(4) == 5
    assert my_tree.find_kth_in_order_item_iterative(5) == 6
    assert my_tree.find_kth_in_order_item_iterative(6) == None


def test_tree_find_kth_pre_order_iteratively():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(1)
    my_tree.insert(4)

    assert my_tree.find_kth_pre_order_item_iterative(1) == 5
    assert my_tree.find_kth_pre_order_item_iterative(2) == 3
    assert my_tree.find_kth_pre_order_item_iterative(3) == 1
    assert my_tree.find_kth_pre_order_item_iterative(4) == 4
    assert my_tree.find_kth_pre_order_item_iterative(5) == 6
    assert my_tree.find_kth_pre_order_item_iterative(6) == None


def test_tree_find_kth_post_order_iteratively():
    my_tree = Tree()
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(6)
    my_tree.insert(1)
    my_tree.insert(4)
    assert my_tree.find_kth_post_order_item_iterative(1) == 1
    assert my_tree.find_kth_post_order_item_iterative(2) == 4
    assert my_tree.find_kth_post_order_item_iterative(3) == 3
    assert my_tree.find_kth_post_order_item_iterative(4) == 6
    assert my_tree.find_kth_post_order_item_iterative(5) == 5
    assert my_tree.find_kth_post_order_item_iterative(6) == None
