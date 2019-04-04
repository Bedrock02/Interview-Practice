'''
Find all possible permuations

Approach
For every character in word
build
start collection with one character
for every other character possible
 a + find_permutations(given_string - a)
 b +
 c +
 d +

a
b
c
d
'''


def find_permutations(given_string):
    collection = []

    def get_permutations(input, prepend=''):
        if len(prepend) == len(given_string):
            collection.append(prepend)
            return

        for index, char in enumerate(input):
            newInput = input[:index] + input[index+1:]
            get_permutations(newInput, prepend=prepend + char)

    get_permutations(given_string)
    return collection
