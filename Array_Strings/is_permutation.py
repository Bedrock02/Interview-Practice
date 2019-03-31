from collections import Counter
'''
Given two strings, write a method to decide if one is a permutation of the other.

My Solution:

abcd
dcba
adcb
bcda

What makes a permutation of another string
1. size of string is equal
2. should contain same number of all characters

My Solution:
1. Check the length of both strings, if not equal ==> false
2. Sort both strings, iterate through both strings and assure that they are equal

Questions To Ask
- Should we compare if it is case sensitive?
- Also known as anagrams
'''


def is_permutation(string_A, string_B):
    '''
    Utilizes Zip to find if two strings are Permutations

    Args:
        string_A (str)
        string_B (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''

    if len(string_A) != len(string_B):
        return False

    sorted_A = sorted(string_A)
    sorted_B = sorted(string_B)

    for a, b in zip(sorted_A, sorted_B):
        if a != b:
            return False
    return True


def is_permutation2(string_A, string_B):
    '''
    Utilizes Iterates through the string to find if
    two strings are Permutations of each other

    Args:
        string_A (str)
        string_B (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(string_A) != len(string_B):
        return False

    sorted_A = sorted(string_A)
    sorted_B = sorted(string_B)

    for i in range(0, len(string_A)):
        if sorted_A[i] != sorted_B[i]:
            return False
    return True


def is_permutation3(string_A, string_B):
    '''
    Cleanest Approach

    Args:
        string_A (str)
        string_B (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(string_A) != len(string_B):
        return False
    return sorted(string_A) == sorted(string_B)


def is_permutation4(string_A, string_B):
    '''
    Utilizes Counter to find if two strings are Permutations

    Args:
        string_A (str)
        string_B (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(string_A) != len(string_B):
        return False
    counter = Counter()

    for char in string_A:
        counter[char] += 1

    for char in string_B:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True
