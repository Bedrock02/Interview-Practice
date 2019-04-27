'''
A child is running up a staircase with n steps,
and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can
run up the stairs.
'''
# ASSUME STAIRCASE N = 10
# [possible steps]
# 3 3 3 1
# 2 2 1

# Exponential time complexity, O(3^n)
# Better time complexity, with Dynamic Programming
# Recording the possible number of ways to get to a specific step


def running_up_stairs(number_of_steps):
    map = [-1] * number_of_steps
    if number_of_steps < 0:
        return 0
    if number_of_steps == 0:
        return 1

    def hop(current_step):
        if current_step == number_of_steps:
            return 1
        if current_step > number_of_steps:
            return 0
        if map[current_step] > -1:
            return map[current_step]
        map[current_step] = hop(current_step + 1) + hop(current_step + 2) + hop(current_step + 3)
        return map[current_step]
    return hop(0)
