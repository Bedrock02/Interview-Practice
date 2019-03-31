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


def isPermutation(stringA, stringB):
    '''
    Utilizes Zip to find if two strings are Permutations

    Args:
        stringA (str)
        stringB (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''

    if len(stringA) != len(stringB):
        return False

    sortedA = sorted(stringA)
    sortedB = sorted(stringB)

    for a, b in zip(sortedA, sortedB):
        if a != b:
            return False
    return True


def isPermutation2(stringA, stringB):
    '''
    Utilizes Iterates through the string to find if
    two strings are Permutations of each other

    Args:
        stringA (str)
        stringB (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(stringA) != len(stringB):
        return False

    sortedA = sorted(stringA)
    sortedB = sorted(stringB)

    for i in range(0, len(stringA)):
        if sortedA[i] != sortedB[i]:
            return False
    return True


def isPermutation3(stringA, stringB):
    '''
    Cleanest Approach

    Args:
        stringA (str)
        stringB (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(stringA) != len(stringB):
        return False
    return sorted(stringA) == sorted(stringB)


def isPermutation4(stringA, stringB):
    '''
    Utilizes Counter to find if two strings are Permutations

    Args:
        stringA (str)
        stringB (str)

    Returns:
        boolean: True/False if it is a permutation or not
    '''
    if len(stringA) != len(stringB):
        return False
    counter = Counter()

    for char in stringA:
        counter[char] += 1

    for char in stringB:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True
