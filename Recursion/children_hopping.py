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


def running_up_stairs(number_of_steps):
    def hop(current_step):
        if current_step == number_of_steps:
            return 1
        if current_step > number_of_steps:
            return 0
        return hop(current_step + 1) + hop(current_step + 2) + hop(current_step + 3)
    return hop(0)
