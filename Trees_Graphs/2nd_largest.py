'''
Write a function to find the 2nd largest element in a binary search tree
Assume that there exist a BSt called tree and that we can access the root and the node's value
'''

def second_largest(tree):
	root = tree.root
	if root is None or root.right_child is None:
		return None

	return find_second_largest(root)

def find_second_largest(node):
	if node.right_child:
		return find_second_largest(node.right_child)

	if node.parent:
		return node.parent

