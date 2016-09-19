def move_to_front(list_a, index):
  """
  takes in a list position and places that element in position x and move sto front
  """
  print "MOVE"
  element = list_a[index]
  del list_a[index]
  return [element] + list(list_a)

def sort_move_to_front(list_a):
  for idx,element in enumerate(list_a):
    next_element = idx + 1
    if next_element < len(list_a) and element > list_a[idx + 1]:
      new_list = move_to_front(list_a, next_element)
      return sort_move_to_front(new_list)
  return list_a

print sort_move_to_front([5,4,3,2,1])