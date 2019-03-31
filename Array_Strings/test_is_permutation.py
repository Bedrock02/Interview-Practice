from is_permutation import *


def test_strings_of_different_lengths():
    assert is_permutation('abc', 'a') == False
    assert is_permutation2('abc', 'a') == False
    assert is_permutation3('abc', 'a') == False
    assert is_permutation4('abc', 'a') == False


def test_invalid_permutations():
    assert is_permutation('abc', 'efg') == False
    assert is_permutation2('abc', 'efg') == False
    assert is_permutation3('abc', 'efg') == False
    assert is_permutation4('abc', 'efg') == False


def test_valid_permutation():
    assert is_permutation('abc', 'cba') == True
    assert is_permutation2('abc', 'cba') == True
    assert is_permutation3('abc', 'cba') == True
    assert is_permutation4('abc', 'cba') == True
