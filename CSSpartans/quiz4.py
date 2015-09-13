'''
Implement getWords(arr1, arr2)
Write an algorithm that will take in 2 arrays of strings and returns a list of unique strings that are in both of the input arrays
The array lengths will always be: arr1.length <= arr2.length
What is the runtime of your algorithm?
Example:
Input:
arr1 = ["a", "b", "b"]
arr2 = ["a", "b", "c", "a", "b"]
Output:
["a", "b"]
Note: The output does not need to be in any specific order
The answer will be posted on Saturday

'''

def getWords(list1,list2):
	return set(list1) & set(list2)

arr1 = ["a", "b", "b"]
arr2 = ["a", "b", "c", "a", "b"]
print getWords(arr1, arr2)