'''
Write a method to replace all spaces in a string with'%20'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string.

EXAMPLE
Input: "Mr John Smith
Output: "Mr%20Dohn%20Smith"
'''


def replace_space(input, char='%20'):
    '''
    Replace using string split and join
    Args:
        input (string): This is the string that will be modified
        char (string): This is what we are going to swap

    Returns:
    A string with the spaces swapped for another character
    '''
    return char.join(input.split(" "))


def replace_space_2(input, char='%20'):
    '''
    Building a string from scratch based on an existing string
    Args:
        input (string): This is the string that will be modified
        char (string): This is what we are going to swap

    Returns:
    A string with the spaces swapped for another character
    '''
    resultInput = ""
    for index, char in enumerate(input):
        resultInput += "%20" if char is ' ' else char
    return resultInput


def replace_space_3(input, char='%20'):
    '''
    Using replace method
    Args:
        input (string): This is the string that will be modified
        char (string): This is what we are going to swap

    Returns:
    A string with the spaces swapped for another character
    '''
    return input.replace(" ", char)
