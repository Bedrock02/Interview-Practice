from merge_sorted import *


def test_merge_sorted_empty_states():
    assert merge_sorted_arrays([], []) == []


def test_merge_sorted_one_empty():
    assert merge_sorted_arrays([1, 2, 3, 4, 5], []) == [1, 2, 3, 4, 5]
    assert merge_sorted_arrays([], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_sorted_easy_merge():
    assert merge_sorted_arrays([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_merge_sorted_overlap():
    assert merge_sorted_arrays([1, 2, 3, 4, 5, 6], [3, 5, 7, 8]) == [1, 2, 3, 3, 4, 5, 5, 6, 7, 8]
    assert merge_sorted_arrays_no_slice([1, 2, 3, 4, 5, 6], [3, 5, 7, 8]) == [
        1, 2, 3, 3, 4, 5, 5, 6, 7, 8]

    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    list_b = [0, 2, 4, 6, 7, 8, 9]
    assert merge_sorted_arrays(list_a, list_b) == sorted(list_a + list_b)
    assert merge_sorted_arrays_no_slice(list_a, list_b) == sorted(list_a + list_b)


def test_merge_sorted_overlap_no_dups():
    assert merge_sorted_arrays_no_dups([1, 2, 3, 4, 5, 6], [3, 5, 7, 8]) == [
        1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sorted_arrays_no_dups_no_slice([1, 2, 3, 4, 5, 6], [3, 5, 7, 8]) == [
        1, 2, 3, 4, 5, 6, 7, 8]

    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
    list_b = [0, 2, 4, 6, 7, 8, 9]
    assert merge_sorted_arrays_no_dups(list_a, list_b) == sorted(list(set(list_a + list_b)))
    assert merge_sorted_arrays_no_dups_no_slice(
        list_a, list_b) == sorted(list(set(list_a + list_b)))
