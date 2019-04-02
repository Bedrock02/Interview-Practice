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
1. I will iterate through the wordDict, for each item in wordDict
    1.1 Check if word is a substring in the input
    1.2 If word is a substring I will strip that word from the input string
    1.3 If word is not a substring I will return false
'''
def word_break(input, wordDict):
    for word in wordDict:
        if word not in input:
            return False
        startOfWord = input.find(word)
        endOfWord = startOfWord + len(word)
        input = input[:startOfWord] + input[endOfWord:]
    return True
