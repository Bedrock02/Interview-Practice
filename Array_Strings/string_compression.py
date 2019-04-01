'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3.
If the "compressed" string would not become smaller than the
original string, your method should return the original string

My Solution
1. Iterat through string
2. If it is the first time we are seeing the character we add that to new string
3. Keep track of what character we saw previously
4. Continue iterating until you see a new character (while keeping count)
5. Once you see a new character place the count on string being built
6. Repeat steps 2 to 6


Things to note:
- copying a string is a runtime  O(N+M) operation, since we are appending the same word we
are lookingat O(m^2). Concatenation basically copies over a string
'''


def compress_string(input):
    prev_char = None
    prev_count = 0
    result = ""

    def compress(resultString, extra=''):
        return (resultString + str(prev_count) if prev_char is not None else '') + extra

    for char in input:
        if char is not prev_char:
            result = compress(result, extra=char)
            prev_count, prev_char = 1, char
        else:
            prev_count += 1
    result = compress(result)
    return result
