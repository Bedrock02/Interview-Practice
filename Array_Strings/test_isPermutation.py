from isPermutation import *


def test_strings_of_different_lengths():
    assert isPermutation('abc', 'a') == False
    assert isPermutation2('abc', 'a') == False
    assert isPermutation3('abc', 'a') == False
    assert isPermutation4('abc', 'a') == False


def test_invalid_permutations():
    assert isPermutation('abc', 'efg') == False
    assert isPermutation2('abc', 'efg') == False
    assert isPermutation3('abc', 'efg') == False
    assert isPermutation4('abc', 'efg') == False


def test_valid_permutation():
    assert isPermutation('abc', 'cba') == True
    assert isPermutation2('abc', 'cba') == True
    assert isPermutation3('abc', 'cba') == True
    assert isPermutation4('abc', 'cba') == True
