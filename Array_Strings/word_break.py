'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

'''

Approach
1. Create memoization
2. take word Dict, sort it from big to little
3. Begin to break down word with the given input
4. If word we are looking to break down result in memo return result
5. Copy word we are going to break down in order to manipulate
6. for every word in wordDict, see if we can make the given word  smaller
7. If no change happened continue to the next word
8. If there is nothing to break down or we can continue to break it down to nothing return True and save True
9. If all the words failed then return False, set to false.
'''

def word_break(input, wordDict):
    wordDict = sorted(wordDict, key=lambda x: len(x), reverse=True)
    memoization = {}
    if not wordDict:
        return False

    def break_down_word(given_word):
        if given_word in memoization.keys():
            return memoization[given_word]

        copy_given_word = given_word

        for word in wordDict:
            copy_given_word = copy_given_word.replace(word, " ").strip()
            # If nothing happened, check another word
            if copy_given_word == given_word:
                continue

            if len(copy_given_word) == 0 or break_down_word(copy_given_word):
                memoization[copy_given_word] = True
                return True

        memoization[copy_given_word] = False
        return False
    return break_down_word(input)
