"""
We know a string is Palindrome if it is the same reading from both sides.
Now we define the following string also Palindrome:

A man, a plan, a cana, Panama!

Write a code that returns if a string is aplindrome and it should return true for above input.
In addition we assume the string is very long and we can not keep a copy of this string
or even a copy of preprocessed version of the string. Therefore the result should be returend with the first sweep of the string
"""

def is_palindrome(stringA):
  total_length = len(stringA)
  tail = total_length - 1
  tail_char = stringA[tail]

  if total_length == 1:
    return True

  for idx in xrange(total_length):
    # Make sure that our end is looking at an alpha
    if not tail_char.isalpha():
      while tail > -1 or not tail_char.isalpha():
        tail -= 1
        tail_char = stringA[tail]

    #Make sure that our front is looking at a front
    if not stringA[idx].isalpha():
      continue
    if (tail == idx and tail_char == stringA[idx]) or tail < idx:
      return True

    if stringA[idx] == tail_char:
      tail -= 1
      tail_char = stringA[tail]
      continue
    else:
      return False


