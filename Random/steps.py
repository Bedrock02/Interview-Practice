'''
Implement stairs(N) that (collect the solutions in a list)
print all the ways to climb up a N-step-stairs
where on can either take a single step or double step.
We'll use 1 to respresent a single step, and 2 to represent a double step
'''

def remove_item_from_dict(items, some_dict):
  for item in items:
    del some_dict[item]
  items = []

def find_steps(N):
  solutions = []
  set_steps = {'': 0}
  
  if N == 0:
    return solutions
  
  while set_steps:
    # increment steps
    for key in set_steps.keys():
      set_steps[key + str(1)] = set_steps[key] + 1
      set_steps[key + str(2)] = set_steps[key] + 2
      del set_steps[key]
    # validate this
    for key in set_steps.keys():
      if set_steps[key] > N:
        del set_steps[key]
      elif set_steps[key] == N:
        solutions.append(key)
        del set_steps[key]
  
  return solutions
for x in find_steps(10):
  print x