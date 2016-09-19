# Find kth smallest
# [ 1 1 1 1 1 1 ]: 1

# [ 1 2 2 4 5]: 2

# [9, 4, 35, 4 3, 2,]: 3

# Find the smaller ones
# Find the larger ones
# Find the middle ones
def find_kth_smallest(some_a, kth):
  if len(some_a) == 1:
    return some_a[0]
  get_midpoint_idx = len(some_a)/2

  smalls = [ele for ele in some_a if some_a[get_midpoint_idx] > ele]
  middle = [ele for ele in some_a if some_a[get_midpoint_idx] == ele]
  larger = [ele for ele in some_a if some_a[get_midpoint_idx] < ele]

  # if kth_idx is larger than the small then
  # we toss the smalls and look at middle and larger
  if len(smalls) < kth:
    new_kth = kth - len(smalls)
    # check for middle
    if len(middle) >= new_kth:
      return middle[0]
    else:
      return find_kth(larger, new_kth)
  else:
    return find_kth(smalls, kth)


som_list = [1, 5, 8, 9, 7, 5]
print(find_kth(som_list, 2))