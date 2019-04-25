from children_hopping import *


def test_children_hopping():
    assert running_up_stairs(1) == 1
    assert running_up_stairs(2) == 2
    assert running_up_stairs(3) == 4
    assert running_up_stairs(4) == 7
