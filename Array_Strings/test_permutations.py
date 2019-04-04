from permutations import *

def test_permutations():
    result = find_permutations('ab')
    assert len(result) == 2

    result = find_permutations('abc')
    assert len(result) == 6

    result = find_permutations('abcd')
    assert len(result) == 24
