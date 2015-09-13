from stack import Stack_Node
def MoveTower(towers,disk, source, destination, spare):
	if disk == 0:
		towers[destination].push(towers[source].pop())
	else:
		MoveTower(towers,disk-1,source,spare,destination)
		towers[destination].push(towers[source].pop())
		MoveTower(towers,disk-1,spare,destination,source)

towers = {}

towers[0] = Stack_Node()
towers[0].set_stack([5,4,3,2,1,0])

towers[1] = Stack_Node()
towers[2] = Stack_Node()

MoveTower(towers,5,0,2,1)

