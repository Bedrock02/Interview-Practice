from word_break import *

def test_word_break():
    tests = [
        ('leetcode', ["leet", "code"], True),
        ('applepenapple', ["apple", "pen"], True),
        ('catsandog', ["cats", "dog", "sand", "and", "cat"], False),
    ]
    for input, wordDict, expectation in tests:
        assert word_break(input, wordDict) == expectation
