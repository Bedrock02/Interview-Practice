from tree_2 import *


def test_tree():
    my_tree = Tree()
    my_tree.add(50)
    my_tree.add(10)
    assert my_tree.size == 2

<<<<<<< HEAD

def test_balance():
=======
def test_is_balanced():
>>>>>>> 85e8a38... Is Balanced Test
    my_tree = Tree()
    my_tree.add(50)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

<<<<<<< HEAD
    my_tree.add(10)
=======
    my_tree.add(20)
>>>>>>> 85e8a38... Is Balanced Test
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(100)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

<<<<<<< HEAD
    my_tree.add(5)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(1)
=======
    my_tree.add(30)
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == True

    my_tree.add(25)
>>>>>>> 85e8a38... Is Balanced Test
    balanced, _ = is_balanced(my_tree.head)
    assert balanced == False
