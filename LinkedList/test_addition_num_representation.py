from addition_num_rep import *


def test_add_two_linked_list():
    number_1 = LinkedList([7, 1, 6])
    number_2 = LinkedList([5, 9, 2])
    result = add_two_linked_list_numbers(number_1, number_2)
    assert result.print_linked_list() == '2, 1, 9, '

    number_1 = LinkedList([7, 1])
    number_2 = LinkedList([1])
    result = add_two_linked_list_numbers(number_1, number_2)
    assert result.print_linked_list() == '8, 1, '
