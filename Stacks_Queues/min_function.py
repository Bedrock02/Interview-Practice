'''How would you design a stack which, in addition to push and pop, 
also has a function min which returns the minimum element? 
Push, pop and min should all operate in O(1) time.'''

'''
Answer:
The stack will hold an individual variable called min, that will keep track of the minimum element
Each time that we push an element onto the stack we look to compare the new element with the current minimum element

However when poping the top off the stack, if we are popping off the minumum value, we need to search
for a new min. we could use the information of the last min to better our search

if we are using a node strucutre we can store a minumum value that is "beneth them"
each time we create a new node and place it on the top we can look at the top's next and see its minumum
before taking that number we compare it to the current top
'''

'''
or keep a seperate stack that will keep track of the mins
sorted data

'''