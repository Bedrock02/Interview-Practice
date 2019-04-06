'''
Given a list of float numbers, insert "+", "-", "*" or "/" between each consecutive pair of numbers to find the maximum value you can get. For simplicity, assume that all operators are of equal precedence order and evaluation happens from left to right.

Example:
(1, 12, 3) -> 1 + 12 * 3  = 39
(1, 12, -3) -> = 1 - 12 * -3 = 33

if we have a negative => multiplying two neg is the most valuable
if we have two positive, we want to multiply, unless we have 1 or 0

-1, 0
if 0 don't multiply, divide


num1 num2 ==> +, -, /, * ==> max

negative, 0.01 are possible

This problem was taken from a Peloton Technical Interview
'''

'''
This is a Breadth First Search Approach (Exploring our neighbors)
We are using the queue to hold all potential max candidates
We "empty out" or pop out all the results we want and enqueue the results
we are going to need later

Optimziation: We only take the min and max value to enqueue since these
can potentially have a better chance at creating the biggest outcome.

Runtime: Exponential, Input in queue increases by 2 for every iteration,
which increase the iteration of the next round.

Note: We are not dividing by zero this causes an error
'''


def find_max_value_DFS(input_list):
    queue = [input_list[0]]

    for item in input_list[1:]:
        num_of_candidates = len(queue)
        for _ in range(num_of_candidates):
            candidate_max = queue.pop(0)
            add = item + candidate_max
            sub = item - candidate_max
            mult = item - candidate_max
            results = (add, sub, mult)
            if candidate_max != 0:
                div = item / candidate_max
                results = (add, sub, mult, div)
            queue.append(max(results))
            queue.append(min(results))
    return max(queue)


'''
This is Depth First Search (Go all the way down first)
This is a recurisve solution that passes on a list down to every recursive process

Runtime: Exponential Runtime, as the input increases so does the run time
Every recursive call calls antoher 4 recrusive calls

Space: Too much, in this solution are always rebuilding and copying an array
We can always just point to where we are in the array.
'''


def find_max_value(input_list):
    collection = []

    def find_combinations(current_max, copy_collection):
        if not copy_collection:
            collection.append(current_max)
            return

        next_item = copy_collection[0]

        find_combinations(current_max + next_item, copy_collection[1:])
        find_combinations(current_max * next_item, copy_collection[1:])

        if next_item != 0:
            find_combinations(current_max / next_item, copy_collection[1:])

        find_combinations(current_max - next_item, copy_collection[1:])

    find_combinations(input_list[0], input_list[1:])
    return max(collection)
