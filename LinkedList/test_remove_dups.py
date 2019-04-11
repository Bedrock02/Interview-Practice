from remove_dups import *


def test_remove_no_dups():
    sample_list = LinkedList([1, 2, 3, 4])
    remove_dups(sample_list)
    assert sample_list.print_linked_list() == '1, 2, 3, 4, '


def test_remove_dups():
    sample_list = LinkedList([1, 2, 2, 3, 4])
    remove_dups(sample_list)
    assert sample_list.print_linked_list() == '1, 2, 3, 4, '

    sample_list = LinkedList([1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 0, 0, 4])
    remove_dups(sample_list)
    assert sample_list.print_linked_list() == '1, 2, 3, 4, 0, '


def test_remove_dups_2():
    sample_list = LinkedList([1, 2, 2, 3, 4])
    remove_dups_2(sample_list)
    assert sample_list.print_linked_list() == '1, 2, 3, 4, '

    sample_list = LinkedList([1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 0, 0, 4])
    remove_dups_2(sample_list)
    assert sample_list.print_linked_list() == '1, 2, 3, 4, 0, '
